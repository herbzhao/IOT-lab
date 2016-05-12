
//	Any Jquery event here
$(document).ready(function(){

	$('h1').click(function(){
		$('h1').fadeOut();}
		);
		
	repeater()
});


// Google chart here

// Load the Visualization API and the corechart package.
google.charts.load('current', {packages: ['gauge']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);


function repeater (){
	setInterval(function(){ voltage_read() }, 90);
}

function voltage_read() {
		$.getJSON($SCRIPT_ROOT + '/result', function(data)
	{$('#voltage').text(data.value);});
}


// Callback that creates and populates a data table,
// instantiates the  chart, passes in the data and draws it.


function drawChart() {
   
   
    var voltage = $.ajax({
	url: $SCRIPT_ROOT + '/result',
	dataType: "json",
	data = data.value,
	async: false
	}).responseText;


    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Voltage', voltage]
    ]);

    var options = {
        width: 400,
        height: 120,
        redFrom: 4,
        redTo: 5,
        yellowFrom: 3,
        yellowTo: 4,
        minorTicks: 0.01,
        max: 5
    };
    var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
    chart.draw(data, options);




    // dynamic update, randomly assign new values and redraw
/*    function getData () {
        $.ajax({
            url: $SCRIPT_ROOT + '/result',
            success: function (response) {
                data.setValue(0, 1, response);
                chart.draw(data, options);
                setTimeout(getData, 100);
            }
        });
    }
*/

getData();

}

