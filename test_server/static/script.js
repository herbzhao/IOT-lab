var val;
var timer = null;

function tick() {
    $('#input').val(++val);
};


$(document).ready(function(){
	
	
$('#start').click(function() {
    if (!timer) { // don't restart if already running
        val = +$('#input').val();
        timer = setInterval(tick, 1000);
    }
});

$('#stop').click(function() {
    clearInterval(timer);
    timer = null; // allow restarting
});

$('#test').click(function(){
	$(this).fadeOut(200);}
);


$('#html_button').click(function(){
	$(this).fadeOut(200);}
);

});



//~ $(document).ready(function(){
    //~ $('#set_serial').click(
		    //~ repeater_voltage();
		//~ );
    //~ repeater_voltage();

//~ $('#html_button').click(function(){
	//~ $(this).fadeOut(3000);}
//~ );


//~ $('#test').click(function(){
	//~ $(this).fadeOut(3000);}
//~ );


//~ $('#start').click(function(){
	//~ $(this).fadeOut(3000);}
//~ );


//~ $('#stop').click(function(){
	//~ $(this).fadeOut(3000);}
//~ );


//~ });

