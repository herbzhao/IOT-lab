function voltage_read() {
	$.getJSON($SCRIPT_ROOT + '/voltage', function(data)
	{$('#voltage').text(data.value);});
}

function temp_read() {
	$.getJSON($SCRIPT_ROOT + '/temperature', function(data)
	{$('#temp').text(data.value);});
}



//~ function incubator_status() {
	//~ $.getJSON($SCRIPT_ROOT + '/temperature', function(data)
	//~ {$('#temp').text(data.value);});
//~ }



//~ $('#set_sensor').click(function(){
//~ setInterval(function(){ temp_read() }, 500);
//~ });

function repeater_temp (){
	
	//~ setInterval(function(){ voltage_read() }, 90);


	setInterval(function(){ temp_read() }, 500);

}


function repeater_voltage (){
	setInterval(function(){ voltage_read() }, 90);
}


//~ $('#set_serial').click(repeater);

$(document).ready(function(){

    //~ $("#set_serial").click(function(){
        //~ repeater()
    //~ });
    repeater_voltage();
    repeater_temp();
});



