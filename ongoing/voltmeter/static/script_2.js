
//	Any Jquery event here
$(document).ready(function(){

	$('h1').click(function(){
		$('h1').fadeOut();}
		);
});


// Google chart here

// Load the Visualization API and the corechart package.
google.charts.load('current', {packages: ['gauge']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the  chart, passes in the data and draws it.


function drawChart() {
	
// Replace the data source URL on next line with your data source URL.	

/*
var serial_ipnut = $.ajax({
	url: $SCRIPT_ROOT + '/result',
	dataType: "json",
	data = data.value,
	async: false
	}).responseText;
*/

/*
var serial_input = $.ajax({
  dataType: "json",
  url: $SCRIPT_ROOT + '/result',
  data: data.value,
  success: success
}).responseText;
*/

//https://groups.google.com/forum/#!topic/google-visualization-api/ShBsXw93_4w



var data = google.visualization.arrayToDataTable([
  ['Label', 'Value'],
  ['Voltage', 0]
]);

var options = {
  width: 400, height: 120,
  redFrom: 4, redTo: 5,
  yellowFrom:2, yellowTo: 4,
  minorTicks: 0.1, max: 5
};



// Create our data table out of JSON data loaded from server.
//var data = new google.visualization.DataTable(jsonData);

// Instantiate and draw our chart, passing in some options.
var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
chart.draw(data, options);




function getData () {
    $.ajax({
        url: $SCRIPT_ROOT + '/result',
        success: function (response) {
            data.setValue(0, 1, response);
            chart.draw(data, options);
            setTimeout(getData, 5000);
        }
    });
}

*/

getData();

// Set chart options

}   // end of callback - drawChart
      
      

