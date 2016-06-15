function voltage_read() {
	$.getJSON($SCRIPT_ROOT + '/voltage', function(data)
	{$('#voltage').text(data.value);});
}

function temp_read() {
	$.getJSON($SCRIPT_ROOT + '/temperature', function(data)
	{$('#temp').text(data.value);});
}



function repeater_temp (){
	//~ setInterval(function(){ voltage_read() }, 90);
	setInterval(function(){ temp_read(); }, 500);
}



function repeater_voltage (){
	setInterval(function(){ voltage_read(); }, 70);
}


//~ var volt_timer = null;

$(document).ready(function(){

	$('#volt_read').click(function(){
	repeater_voltage();
	});
	

});

