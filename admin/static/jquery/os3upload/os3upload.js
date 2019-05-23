String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};


(function ( $ ) {
    function Os3Upload(select,options) {
    	var $this = this;
    	this.$select = $(select);
    	this.opt = options;
    	this.initialize = function(){
    		//TODO - VERIFICAR SE JA EXISTE ANTES DE CRIAR
        	$this.dockmodal = $('<div class="dockmodal"><div class="dockmodalheader"><span class="dockmodalheader-title">Upload de arquivos</span><div class="dockmodalheader-controls"><span class="minimize"></span>'+
			   '<span class="dockmodal-close"></span></div></div><div id="dockmodalcontent"></div></div>');
        	if ( $( "#myDiv" ).length ) {
        		$this.dockmodal.appendTo('body');
        	}
         	$this.dockmodalcontent = $('#dockmodalcontent');
           	$('.dockmodalheader-controls .dockmodal-close').click(function(){
        		$this.dockmodal.hide();
        	});
        	$('.dockmodalheader-controls .minimize').click(function(){
        		var c = $('.dockmodalheader-controls .minimize');
        		if(c.attr('data-actiontype') == 'open'){
        			$this.dockmodalcontent.animate({height:300}, 200);
        			c.attr('data-actiontype','close');
        		}else{
        			$this.dockmodalcontent.animate({height:0}, 200);
        			c.attr('data-actiontype','open');
        		}
        	});
         	$this.fileupload = this.$select.get(0);
    		$this.fileupload.onchange = function(){
    			
    			$this.opt.beforeSend();
    			
            	files = $this.fileupload.files;
            	if(files.length == 0){
            		return;
            	}
            	$this.dockmodal.show();
            	$this.dockmodalcontent.animate({height:300}, 200);
            	$this.dockmodalcontent.empty();
            	//lista todos os arquivos
            	for(var i = 0; i < files.length; i++){
            		f = files[i];
            		$this.dockmodalcontent.append('<div class="fileitem"><div class="col1">' + f.name + '</div><div id="file-status-' + i + '" class="col2">Aguardando...</div></div>')
            	}
            	//faz upload arquivo por arquivo para nao sobrecarregar o servidor com dezenas de requests
            	var counter = 0;
            	var files_percent = 0;
            	var intervalid;
            	var canupload = true;
            	//verifica novo arquivo a cada 100 milesegundos
            	intervalid = setInterval(function(){
            		if(canupload){
                		$('.dockmodalheader-title').html('Fazendo upload {0} de {1}. {2}% conclu&iacute;do.'.format(counter + 1, files.length, Math.round((counter + 1) / files.length *100)));
                		canupload = false;
        	    		//comeca upload
        	    		var xhr = new XMLHttpRequest();
        				xhr.upload.addEventListener('progress',function(e){
        					$('#file-status-'+ (counter - 1)).html('Enviando...');
        				},false);
        				xhr.onreadystatechange = function(ev){
        					if(xhr.readyState == 4) {
        						console.log(xhr);
        						if(xhr.status == 200) {
        							$('#file-status-'+ (counter - 1)).html('Enviado');
        							$this.opt.success(xhr);
        						}
        						else {
        							$('#file-status-'+ (counter - 1)).html('Erro');
        							alert(xhr.responseText);
        						}
        						canupload = true;
        					}
        				};
        				xhr.open('POST',$this.opt.url, true);
        				var data = new FormData();
        				data.append('file', files[counter]);
        				xhr.send(data);
        	    		counter++;
            		}
            		if(counter == files.length){
            			clearTimeout(intervalid);
            			$('.dockmodalheader-title').html('Upload conclu&iacute;do.');
            			$this.$select.val('');
            			setTimeout(function(){$this.dockmodal.hide();},1000);
            		}
            	},100);
    		}

        }

    	this.send = function(){
    		if($this.fileupload.files.length > 0){
    			alert('Upload ainda em progresso. Aguarde!');
    			return;
    		}
    		$this.fileupload.click();
    	}
    };

    $.fn.os3upload = function( options ) {
        return this.each(function() {
            var data = $(this).data('os3upload');
            var _options = typeof options === 'object' && options;
            if (!data) {
            	var opts = $.extend( {}, $.fn.os3upload.defaults, _options );
            	data = new Os3Upload(this, opts);
            	data.initialize();
                $(this).data('os3upload', data);
            }

            if (typeof options === 'string') {
                data[options]();
                if (options === 'destroy') {
                    $(this).data('os3upload', false);
                }
            }
        });
    };

    $.fn.os3upload.defaults = {
    		success:function(xhr){}
        };
    
    $.fn.os3upload.defaults = {
    		beforeSend:function(){}
        };
}( jQuery ));