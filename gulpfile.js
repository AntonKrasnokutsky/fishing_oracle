const { src, dest, watch, parallel, series } = require('gulp');
const scss                  = require('gulp-sass');
const concat                = require('gulp-concat');
const browserSync           = require('browser-sync').create();
const uglify                = require('gulp-uglify-es').default;
const autoprefixer          = require('gulp-autoprefixer');
const imagemin              = require('gulp-imagemin')
const del                   = require('del');
const exec                  = require('child_process').exec;

function runserver() {
    var proc = exec('venv/bin/python3.9 manage.py runserver');
}

function migrate() {
    exec('venv/bin/python3.9 manage.py makemigrations');
    exec('venv/bin/python3.9 manage.py migrate');
}

function browsersync() {
    browserSync.init({
        notify: false,
        proxy: 'localhost:8000',
        host: 'localhost:8000',
        open: 'external'
        // server: {
        //     baseDir: 'app/'
        // }
    })
}

function cleanDist() {
    return del('dist')
}

function images() {
    return src('app/images/**/*')
        .pipe(imagemin([
            imagemin.gifsicle({interlaced: true}),
            imagemin.mozjpeg({quality: 75, progressive: true}),
            imagemin.optipng({optimizationLevel: 5}),
            imagemin.svgo({
                plugins: [
                    {removeViewBox: true},
                    {cleanupIDs: false}
                ]
            })
        ]))
        .pipe(dest('dist/images'))
}

function styles(){
    return src('fishing/static/scss/style.scss')
        .pipe(scss({outputStyle: 'compressed'}))
        .pipe(concat('style.min.css'))
        .pipe(autoprefixer({
            overrideBrowserslist: ['last 10 version'],
            grid: true
        }))
        .pipe(dest('fishing/static/css'))
        .pipe(browserSync.stream())
}

function scripts() {
    return src(['node_modules/jquery/dist/jquery.js',
        'node_modules/jquery-datetimepicker/build/jquery.datetimepicker.full.js',
        'fishing/static/js/main.js'])
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .pipe(dest('fishing/static/js'))
        .pipe(browserSync.stream())
}

function watching() {
    watch(['fishing/static/scss/**/*.scss'], styles);
    watch(['fishing/static/js/**/*.js', '!fishing/static/js/main.min.js'], scripts);
    watch(['fishing/templates/**/*.html', 'templates/**/*.html', 'accounts/templates/**/*.html', 'blog/templates/**/*.html']).on('change', browserSync.reload);
    watch(['accounts/**/*.py', 'blog/**/*.py', 'users/**/*.py', 'fishing/**/*.py', 'fishing_oracle/**/*.py']).on('change', browserSync.reload);
    // watch(['blog/templates/**/*.html']).on('change', browserSync.reload);
}

function build() {
    return src([
        'app/css/style.min.css',
        'app/fonts/**/*',
        'app/js/main.min.js',
        'app/*.html'],
        {base: 'app'})
        .pipe(dest('dist'))
}

exports.styles = styles;
exports.watching = watching;
exports.browsersync = browsersync;
exports.scripts = scripts;
exports.images = images;
exports.cleanDist = cleanDist;
exports.runserver = runserver;
exports.migrate = migrate;

exports.build = series(cleanDist, images, build);
exports.default = parallel(runserver, styles, watching, browsersync, scripts);