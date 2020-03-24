;(function($) {

    $(document).on("app:ready", function() {
        app = window.app;

        app.reports = {
            init: function() {
                this.initFilters();
            },
            initFilters: function() {
                let filterInput = $('#filter-reports');

                if (filterInput.length === 0) {
                    return;
                }

                filterInput.on('keyup', function(){
                    let keyword = $(this).val().toLowerCase();

                    $('.report-container').each(function(){
                        let location = $(this).data('location');

                        if (location.toLowerCase().indexOf(keyword) === -1) {
                            $(this).addClass('d-none');
                        } else {
                            $(this).removeClass('d-none');
                        }
                    });
                });
            },
        };

        app.reports.init();
    });

}( jQuery ));