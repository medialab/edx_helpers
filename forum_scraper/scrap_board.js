;(function(undefined) {
  var _root = this;

  var urls = {
    page: location.href +
      '/search?ajax=1&sort_key=date&sort_order=desc&commentable_ids='
  };

  // Retrieving board information
  var boards = artoo.scrape(
    '.board-name:contains(S0)',
    function($) {
      var data = JSON.parse($(this).attr('data-discussion_id'));
      return {
        title: data.sort_key,
        id: data.id
      };
    }
  );

  // Make one ajax call
  function ajaxCall(id, page, cb) {
    artoo.log.verbose('Getting page ' + page + ' for ' + id);
    $.get(urls.page + id + '&page=' + page, cb);
  }

  // Loop and get through
  var results = {};
  boards.map(function(b) { results[b.id] = []; });

  function loop(id, page) {
    page = page || 1;

    ajaxCall(id, page, function(data) {
      data.discussion_data.map(function(i) {
        results[id].push(i.id);
      });

      if (page !== +data.num_pages) {
        setTimeout(function() {
          loop(id, page + 1);
        }, 2000);
      }
      else {
        artoo.log.verbose('Finished id ' + id);
        boardsLoop();
      }
    });
  }

  var idx = -1;
  function boardsLoop() {
    idx++;
    if (boards[idx] !== undefined) {
      loop(boards[idx].id);
    }
    else {
      finished();
    }
  }

  boardsLoop();

  function finished() {
    artoo.log.info('Finished, saving...');
    _root.output = results;
    artoo.store.setObject('threads', results);
    artoo.savePrettyJson(results);
  }
}).call(this);
