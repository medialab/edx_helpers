module.exports = function(grunt) {
  var files = [
    'index.js'
  ];

  // Project configuration.
  grunt.initConfig({

    // Configuration to be run (and then tested).
    artoo: {
      dev: {
        options: {
          url: '//localhost:8000/lib/artoo.concat.js',
          settings: {
            scriptUrl: '//localhost:8000/index.js'
          }
        }
      },
      prod: {
        options: {
          clipboard: false
        },
        src: files
      }
    },
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-artoo');

  // By default, compiling artoo build
  grunt.registerTask('default', ['artoo']);
};
