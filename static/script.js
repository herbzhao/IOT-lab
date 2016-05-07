$(document).ready(function(){
	
	$('h2').on("click",function(){
		$(this).fadeOut();
		});
		
	$('input[name=set_serial]').on("click",function(){
		$(this).fadeOut();
		});

	$('label[for=port_command]').on("click",function(){
		$(this).fadeOut();
		});
	
	$.getJSON('/monitor', {
          a: $('input[name="a"]').val(),
          b: $('input[name="b"]').val()
        }, function(data) {
          $("#result").text(data.result);
        });
     


            
            
});
