/**
 * Application plugin (jQuery)

 * @author Signitive <https://signitive.io/>
 * @since 08 May 2018
 */
;(function($) {

    $.app = function(options) {

        var defaults = {
            propertyName: 'value',
            onSomeEvent: function() {}
        }

        var plugin = this;

        plugin.settings = {}

        var init = function() {
            plugin.settings = $.extend({}, defaults, options);
            plugin.api_headers = {
                "APIKEY"  : options.app.api.key,
                "APILANG" : options.app.api.locale,
                "ACCESS-TOKEN" : options.app.api.access_token,
                "TIMEZONE" : options.app.api.timezone,
                "X-CSRFToken" : options.app.api.csrf_token
            };
        }

        plugin.api = {}

        init();

        plugin.ready = function() {
            $(document).trigger('app:ready');
        }
    }

})(jQuery);