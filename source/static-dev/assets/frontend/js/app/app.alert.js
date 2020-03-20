;(function($) {

    $(document).on("app:ready", function() {
        app = window.app;
        app.modals = [];

        app.alert = function (alertType, alertTitle, alertMessage, iTimer) {
             Swal.fire({
                 title: alertTitle ? alertTitle : '',
                 html: app.alert.parseMessage(alertMessage),
                 type: alertType,
                 confirmButtonText: gettext('Close'),
                 timer: iTimer ? iTimer : 5000,
                 allowOutsideClick: false,
                 zIndex: 99999999
             });
        };

        app.alert.queue = function (alertType, alertTitle, alertMessage, iTimer) {
            app.modals.push({
                 title: alertTitle ? alertTitle : '',
                 html: app.alert.parseMessage(alertMessage),
                 type: alertType,
                 confirmButtonText: gettext('Close'),
                 timer: iTimer ? iTimer : 5000,
                 allowOutsideClick: false,
                 zIndex: 99999999
             })
        };

        app.alert.trigger = function() {
            Swal.queue(app.modals)
            app.modals = []
        };

        app.confirm = function (alertType, alertTitle, alertMessage, confirmButtonText, cancelButtonText, callback) {

            Swal.fire({
                title: alertTitle,
                html: alertMessage,
                type: alertType,
                showCancelButton: true,
                confirmButtonText: confirmButtonText,
                cancelButtonText: cancelButtonText,
                reverseButtons: false
            }).then((result) => {
                if (result.value) {
                    callback(true, result);
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    callback(false, result);
                }
            });
        };

        app.alert.parseMessage = function(message) {
            return message;
        };

        app.alert.toast = function(title, toast_type, timer, callback) {
            var _toast = Swal.mixin({
                toast: true,
                position: 'center',
                showConfirmButton: false,
                timer: timer ? timer : 3000
            })

            _toast.fire({
                type: toast_type ? toast_type : 'success',
                title: title,
                onAfterClose: function() {
                    if (callback) {
                        callback();
                    }
                }
            })
        };
    });

}( jQuery ));