;(function($) {

    $(document).on("app:ready", function() {
        app = window.app;

        app.alert = function (alertType, alertTitle, alertMessage, iTimer) {
             return swal({
                 title: alertTitle ? alertTitle : '',
                 text: alertMessage,
                 type: alertType,
                 confirmButtonText: gettext('Close'),
                 timer: iTimer ? iTimer : 5000,
                 allowOutsideClick: false
             });
        };

    });

}( jQuery ));