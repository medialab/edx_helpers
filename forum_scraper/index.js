;(function($, undefined) {

  // Main
  function archive(nb) {
    var forumButton = $('.board-name:contains(S0' + nb + ')');

    // Clicking the button
    forumButton.simulate('click');
  }

  this.archive = archive;
}).call(this, artoo.$);
