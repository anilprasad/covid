;(function($) {

    $(document).on("app:ready", function() {
        app = window.app;

        app.common = {
            init: function() {
                app.common.moment();
            },
            moment: function() { // Moment.js util
                var locale = 'en';

                if (typeof app.settings.app.locale != 'undefined') {
                    locale = app.settings.app.locale;
                }

                moment.locale(locale);
                moment.tz.setDefault(app.settings.app.timezone);

                $('.moment-format').each(function(){
                    var text = $(this).text();

                    if (moment(text).isValid()) {
                        var d = moment(text).tz('Europe/Berlin').fromNow();
                        $(this).text(d);
                    }
                })
            },
        };

        app.common.init();
    });

}( jQuery ));