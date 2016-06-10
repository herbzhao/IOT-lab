function voltage_read() {
	$.getJSON($SCRIPT_ROOT + '/voltage', function(data)
	{$('#voltage').text(data.value);});
}

function temp_read() {
	$.getJSON($SCRIPT_ROOT + '/temperature', function(data)
	{$('#temp').text(data.value);});
}

//voltage(serial) reading
var repeater_volt = null; 
function repeater_volt (){
	volt_display = setInterval(function(){ voltage_read() }, 90);
}

function stop_volt() {
    clearTimeout(volt_display);
};

//temperature reading
var repeater_temp = null;
function repeater_temp (){
	temp_display = setInterval(function(){ temp_read() }, 500);
}

function stop_temp() {
    clearTimeout(repeater_temp);
};


//~ $(document).ready(function(){
    //~ $("#set_serial").click(function(){
		 //~ repeater_volt()
    //~ });


    //~ $("#set_temp").click(function(){
		 //~ repeater_temp()
    //~ });
    
//~ });



$("#set_serial").click( repeater_volt);

$('#set_temp').click(reapeter_temp);
