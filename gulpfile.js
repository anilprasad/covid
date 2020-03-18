var gulp = require('gulp'); // Require gulp

// Sass dependencies
var compass = require('compass-importer');
var merge = require('merge-stream');
var sass = require('gulp-sass'); // Compile Sass into CSS
var minifyCSS = require('gulp-clean-css'); // Minify the CSS

// Minification dependencies
var minifyHTML = require('gulp-minify-html'); // Minify HTML
var concat = require('gulp-concat'); // Join all JS files together to save space
var stripDebug = require('gulp-strip-debug'); // Remove debugging stuffs
//var uglify = require('gulp-uglify'); // Minify JavaScript
var uglify = require("gulp-terser");
var imagemin = require('gulp-imagemin'); // Minify images

// Other dependencies
var size = require('gulp-size'); // Get the size of the project
var browserSync = require('browser-sync'); // Reload the browser on file changes
var jshint = require('gulp-jshint'); // Debug JS files
var stylish = require('jshint-stylish'); // More stylish debugging
var copy = require('gulp-copy');
var filesExist = require('files-exist');
var replace = require('gulp-replace');

function touchPy() {
    gulp.src('./source/__init__.py')
        .pipe(gulp.dest('./source/__init__.py'));
}

// Tasks -------------------------------------------------------------------- >

// Task to compile Sass file into CSS, and minify CSS into build directory
gulp.task('styles', function(done) {
  var sassStream, cssStream;

  gulp.src(['./node_modules/@fortawesome/fontawesome-free/webfonts/*.*'])
        .pipe(copy('./source/static-dev/assets/frontend/webfonts/', { prefix: 5}));

  sassStream = gulp.src('./source/static-dev/assets/frontend/scss/app.scss')
      .pipe(sass({compass: true, importer: compass})
      .on('error', sass.logError))
      .pipe(minifyCSS());


  cssFiles = [
      './node_modules/bootstrap/dist/css/bootstrap.css',
      './node_modules/@fortawesome/fontawesome-free/css/all.css',
      './node_modules/slick-carousel/slick/slick.css',
      './node_modules/slick-carousel/slick/slick-theme.css',
      './node_modules/sweetalert2/dist/sweetalert2.min.css',
      './node_modules/multiple-select/dist/multiple-select.min.css',
      './node_modules/dropzone/dist/min/dropzone.min.css',
      './node_modules/rateyo/min/jquery.rateyo.min.css',
      './node_modules/fancybox/dist/css/jquery.fancybox.css',

      './source/static-dev/assets/frontend/css/app.css',
  ];

  cssStream = gulp.src(filesExist(cssFiles))
    .pipe(minifyCSS());

  var result = merge(sassStream, cssStream)
      .pipe(concat('app.min.css'))
      .pipe(replace('multiple-select.png', '../img/multiple-select.png'))
      .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  done();

  return result;
});

gulp.task('scripts', function(done) {
    // Task to concat, strip debugging and minify JS files
    var vendorFiles = [
      './node_modules/jquery/dist/jquery.js',
      './node_modules/bootstrap/dist/js/bootstrap.bundle.js',
      './node_modules/slick-carousel/slick/slick.min.js',
      './node_modules/sweetalert2/dist/sweetalert2.all.min.js',
      './node_modules/multiple-select/dist/multiple-select.min.js',
      './node_modules/sortablejs/Sortable.min.js',
      './node_modules/localforage/dist/localforage.min.js',
    ];

    var momentFiles = [
      './node_modules/moment/min/moment-with-locales.min.js',
      './node_modules/moment-timezone/builds/moment-timezone-with-data.min.js',
    ]

    var appFiles = [
      './source/static-dev/assets/frontend/js/app.js',
      './source/static-dev/assets/frontend/js/app/*.js',
      './source/static-dev/assets/frontend/js/app/api/*.js',
    ];

  gulp.src(filesExist(appFiles))
    .pipe(concat('app.min.js'))
    //.pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist(vendorFiles))
    .pipe(concat('vendor.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist(momentFiles))
    .pipe(concat('moment.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist(['./node_modules/dropzone/dist/min/dropzone.min.js']))
    .pipe(concat('dropzone.min.js'))
    .pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist(['./node_modules/tus-js-client/dist/tus.min.js']))
    .pipe(concat('tus.min.js'))
    .pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist(['./node_modules/moment/min/moment-with-locales.min.js']))
    .pipe(concat('moment-with-locales.min.js'))
    .pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

  gulp.src(filesExist([
      './node_modules/rateyo/min/jquery.rateyo.min.js',
  ]))
    .pipe(concat('reviews-bundle.min.js'))
    .pipe(stripDebug())
    .pipe(uglify())
    .pipe(gulp.dest('./source/static-dev/assets/frontend/dist/'));

    done();
});

gulp.task('watch', function(done) {
    gulp.watch('./source/static-dev/assets/frontend/js/**/*.js', gulp.series('scripts'))
    gulp.watch('./source/static-dev/assets/frontend/scss/**/*.scss', gulp.series('styles'))
    done();
});

gulp.task('build', gulp.series('styles', 'scripts'))
