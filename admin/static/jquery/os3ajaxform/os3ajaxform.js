(function ( $ ) {
    function Os3AjaxForm(select, options) {
    	var $this = this;
    	this.$select = $(select);
    	this.opt = options;

    	this.initialize = function(){
    		$($this.$select).submit(function() {
    			$.ajax({
    		        data: $(this).serialize(),
    		        async: true,
    		        type: $(this).attr('method'),
    		        url: $(this).attr('action'),
    		        success: function(response) {
    		        	$this.opt.success(response);
    		        },
    		        timeout: 120000
    		    }).fail( function(xhr, textStatus, errorThrown) {
    		    	$this.opt.fail(xhr,textStatus,errorThrown);
    	        });
        		$this.opt.loading();
    			return false;
    		});
    	}
    };

    $.fn.os3ajaxform = function( options ) {
        return this.each(function() {
            var data = $(this).data('os3ajaxform');
            var _options = typeof options === 'object' && options;

            if (!data) {
            	var opts = $.extend( {}, $.fn.os3ajaxform.defaults, _options );
            	data = new Os3AjaxForm(this, opts);
            	data.initialize();
                $(this).data('os3ajaxform', data);
            }

            // Call multiselect method.
            if (typeof options === 'string') {
                data[options]();
                if (options === 'destroy') {
                    $(this).data('os3ajaxform', false);
                }
            }
        });
    };

    $.fn.os3ajaxform.defaults = {
		loading:function(){},
		success:function(response){},
		fail :function(xhr, textStatus, errorThrown){alert(xhr.responseText);}
    };
}( jQuery ));