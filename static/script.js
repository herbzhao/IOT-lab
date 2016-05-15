function voltage_read() {
	$.getJSON($SCRIPT_ROOT + '/voltage', function(data)
	{$('#voltage').text(data.value);});
}

function temp_read() {
	$.getJSON($SCRIPT_ROOT + '/temperature', function(data)
	{$('#temp').text(data.value);});
}



function repeater (){
	setInterval(function(){ voltage_read() }, 90);
	setInterval(function(){ temp_read() }, 200);
}


$(document).ready(function(){
	repeater()

});



//$(document).ready(function(){
//	$('#start_monitor').click(function(){repeater()});$
//});
