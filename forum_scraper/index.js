;(function($, undefined) {

  var DOWNLOAD = true,
      externalUrls = [],
      posts = [],
      imageIndex = 0,
      current;

  function pad(i) {
    return ('' + i).length > 1 ? '' + i : '0' + i;
  }

  var today = new Date(),
      waybackDate = ''+ today.getUTCFullYear() +
                    (pad(today.getUTCMonth() + 1)) +
                    pad(today.getUTCDate()) +
                    '000000';

  // Main
  function archive(nb) {
    current = nb;
    var $forumButton = $('.board-name:contains(S0' + nb + ')');
    externalUrls = [];
    posts = [];
    imageIndex = 0;

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

      // Typically scrapeOne material here
      var data = {
        id: $post.attr('data-id'),
        title: $post.find('h1:first').text(),
        author: $post.find('.username:first').text(),
        nb_comments: $post.find('.discussion-response').length,
        nb_votes: +$post.find('.votes-count-number:first').text()
      };

      posts.push(data);

      // Removing Useless parts
      $post.find('.discussion-reply-new').remove();
      $post.find('.moderator-actions').remove();
      $post.find('.discussion-flag-abuse').remove();
      $post.find('.discussion-pin').remove();
      $post.find('.action-follow').remove();
      $post.find('.vote-btn').remove();
      $post.find('.new-comment').remove();
      $post.find('.action-endorse').remove();

      // Cleaning up some links
      $post.find('.post-context > a').attr('href', '#');

      // Creating a dummy html for the post
      var $dummy = $(document.implementation.createHTMLDocument());

      // Head
      $dummy.find('head')
            .append('<meta charset="utf-8" />')
            .append('<link href="../style.css" rel="stylesheet" type="text/css" />')
            .append('<title>' + $post.find('h1').text() + '</title>');

      $dummy.find('body').append('<div class="container"><div class="discussion-body"><div class="discussion-column"></div></div></div>');

      //2. Dealing with images
      $post.find('img').each(function() {
        var name = (imageIndex++) + $(this).attr('src').split('/').slice(-1)[0].split('?')[0];

        if (DOWNLOAD)
          artoo.saveResource($(this).attr('src'), {filename: name});

        $(this).attr('src', name);
      });

      //3. Dealing with anchors
      $post.find('a').each(function() {
        var href = $(this).attr('href');

        if (href.charAt(0) !== '/' && href.charAt(0) !== '#' &&
            !~href.indexOf('javascript:')) {
          externalUrls.push(href);
          $(this).attr('href', 'http://web.archive.org/web/' + waybackDate + '/' + href);
        }

        if(href.charAt(0) === '/')
          $(this).attr('href', '#');
      });

      //4. Cloning Body
      $dummy.find('.discussion-column').append($post.clone());

      //7. Downloading
      if (DOWNLOAD)
        artoo.saveHtml($dummy.get(0).documentElement.innerHTML, {
          filename: data.id
        });

      if (typeof next === 'function')
        next();
    });
  }

  function finished(err) {
    artoo.log.info('Finished archiving forum n°' + current);

    // Creating a summary
    var $summary = $(document.implementation.createHTMLDocument());

    $summary.find('head')
            .append('<meta charset="utf-8" />')
            .append('<title>Summary</title>');

    $summary.find('body')
            .append('<ul id="post-list"></ul>');

    posts.sort(function(a, b) {
      return b.nb_votes - a.nb_votes;
    }).forEach(function(p) {
      $summary.find('#post-list').append('<li><a href="' + p.id + '.html">' + p.title + '</a> - <em>' + p.author+ '</em> (Votes: ' + p.nb_votes + ', Comments: ' + p.nb_comments + ')</li>');
    });

    if (DOWNLOAD) {
      artoo.saveHtml($summary.get(0).documentElement.innerHTML, {filename: 'summary.html'});
      artoo.savePrettyJson(externalUrls, {filename: 'externalUrls.json'});
      artoo.savePrettyJson(posts, {filename: 'posts.json'});
    }
  }

  this.archive = archive;
  this.scrapePost = scrapePost;
}).call(this, artoo.$);
