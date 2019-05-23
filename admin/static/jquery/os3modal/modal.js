(function ( $ ) {
    var os3modal_array = [];
    function Os3Modal(select, options) {
    	var $this = this;
    	this.$select = $(select);
    	this.opt = options;

    	this.initialize = function(){
    		$this.$modal = $('<div  class="modalDialog"></div>');
    		$this.wrapper = $('<div class="modalwrapper"></div>');
    		$this.$close = $('<div title="Fechar" class="close"></div>');
    		$this.$close.click(function() {
    			$this.hide();
    			os3modal_array.pop();
    		});
    		$this.wrapper.append($this.$close);
    		$this.wrapper.append($this.$select);
    		$this.$modal.append($this.wrapper).appendTo('body');
    		$this.wrapper.css('width',$this.opt.width);
    		$this.wrapper.css('margin',$this.opt.margin);
    	}

    	this.checkHeight = function(){
    		$this.intervalID = setInterval(function () {
	        	area = $(window).height() - $this.wrapper.offset().top;
	        	if(area < $this.wrapper.height()){
	        		$this.wrapper.height(area - 50);
	        	}
    		}, 100);
    	}

    	this.show = function(){
    		$("body").css({ overflow: 'hidden' });
    		$this.$modal.removeClass('modalDialog-hide').addClass('modalDialog-show');
            os3modal_array.push($this);
            $this.checkHeight();
    	}

    	this.hide = function(){
    		if($this.$modal.hasClass('modalDialog-show')){
    			$this.opt.close();
    		}
    		$this.$modal.removeClass('modalDialog-show').addClass('modalDialog-hide');
		    $("body").css({ overflow: 'inherit' });
		    clearInterval($this.intervalID);
    		$this.wrapper.css('height','auto');
    	}

    	this.loading = function(keepHeight){
    		w = $this.$select.height();
    		$this.$select.html('');
    		if(keepHeight)
    			$this.$select.height(w);
    		$this.$select.addClass('modalLoading');
    	}

    	this.unloading = function(){
    		$this.$select.removeClass('modalLoading');
    	}
    };

    $.fn.os3modal = function( options,parameter) {
        return this.each(function() {
            var data = $(this).data('os3modal');
            var _options = typeof options === 'object' && options;

            if (!data) {
            	var opts = $.extend( {}, $.fn.os3modal.defaults, _options );
            	data = new Os3Modal(this, opts);
            	data.initialize();
                $(this).data('os3modal', data);
            }

            // Call multiselect method.
            if (typeof options === 'string') {
                data[options](parameter);
                if (options === 'destroy') {
                    $(this).data('os3modal', false);
                }
            }
        });
    };

    $.fn.os3modal.defaults = {
	    width: "400px",
	    margin: '10% auto',
	    close:function(){}
	};

    $(document).keyup(function(ev){
        if(ev.keyCode == 27){
        	if(os3modal_array.length > 0){
        		var modal = os3modal_array.pop();
        		modal.hide();
        	}
        }
    });
}( jQuery ));