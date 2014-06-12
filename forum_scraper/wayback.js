var request = require('request'),
    async = require('async'),
    _ = require('lodash');

var src = '/home/yomgui/backup/ForumMOOC/',
    waybackUrl = 'https://web.archive.org/save/',
    folders = [
      'S01-Blog section',
      'S02-Bubble exercise',
      'S03-Socio-technical Analysis',
      'S04-Explore controversy',
      'S06-Visualize anthropocene',
      'S07-Public Debate Report'
    ];

function flatten(a) {
  return Array.prototype.concat.apply([], a);
}

var externalUrls = _.uniq(flatten(folders.map(function(f) {
  return require(src + f + '/externalUrls.json');
})));

function save(url, cb) {
  request(waybackUrl + url, function(error, response, body) {
    console.log((response || {}).statusCode || 'unknown', url);
    cb();
  }).setMaxListeners(10000);
}

async.parallelLimit(
  externalUrls.map(function(u) {
    return function(callback) {
      save(u, callback);
    }
  }),
  10,
  function(err) {
    console.log('Done saving urls in the wayback machine!');
  }
);
