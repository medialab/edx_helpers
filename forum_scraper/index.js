;(function($, undefined) {

  var externalUrls;

  // Main
  function archive(nb) {
    var $forumButton = $('.board-name:contains(S0' + nb + ')');
    externalUrls = [];

    // Clicking the button
    $forumButton.simulate('click');
    artoo.log.debug('Opening the desired forum (' + nb + ')');

    // Waiting for the posts to expand
    artoo.waitFor(hasFinishedLoading, expand);
  }

  function hasFinishedLoading() {
    return !$('.loading').length;
  }

  function expand() {
    artoo.log.debug('Now expanding the posts...');

    artoo.autoExpand({
      expand: '.more-pages > a',
      canExpand: '.more-pages',
      elements: '.post-list .list-item',
      done: postLoop
    });
  }

  function postLoop() {
    artoo.async.while(
      function(i) {
        return i < $('.list-item').length;
      },
      scrapePost,
      finished
    );
  }

  function scrapePost(i, next) {

    // Here, we need to open the post, wait for it to be fully loaded
    // (including commentaries), then retrieve its html in a full fragment
    // strategy plus transforming images into dataURL then stocking external
    // URL so we can archive them later.

    //1. Opening post
    if (i !== undefined)
      $('.list-item:eq(' + i + ') > a').simulate('click');
    artoo.waitFor(hasFinishedLoading, function() {
      var $post = $('.discussion-article:first');

      // Removing Useless parts
      $post.find('.discussion-reply-new').remove();
      $post.find('.moderator-actions').remove();
      $post.find('.discussion-flag-abuse').remove();
      $post.find('.discussion-pin').remove();
      $post.find('.action-follow').remove();
      $post.find('.vote-btn').remove();

      // Cleaning up some links
      $post.find('.post-context > a').attr('href', '#');

      // Creating a dummy html for the post
      var $dummy = $(document.implementation.createHTMLDocument());

      // Head
      $dummy.find('head')
            .append('<meta charset="utf-8" />')
            .append('<title>' + $post.find('h1').text() + '</title>');

      // Body
      $dummy.find('body').append($post.clone());

      // Downloading
      artoo.saveHtml($dummy.get(0).documentElement.innerHTML, {
        filename: $post.attr('data-id')
      });

      if (typeof next === 'function')
        next('break');
    });
  }

  function finished(err) {
    console.log('finished')
    // artoo.savePrettyJson(externalUrls, {filename: 'externalURL.json'});
  }

  this.archive = archive;
  this.scrapePost = scrapePost;
}).call(this, artoo.$);
