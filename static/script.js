function voltage_read() {
	$.getJSON($SCRIPT_ROOT + '/result', function(data)
	{$('#voltage').text(data.value);});
}


function repeater (){
	setInterval(function(){ voltage_read() }, 30);
}



$(document).ready(function(){
	$('#start_monitor').click(function(){repeater()});$
});
