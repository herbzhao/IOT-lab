
//	Any Jquery event here
$(document).ready(function(){

	$('h1').click(function(){
		$('h1').fadeOut();}
		);
});


// Google chart here

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the  chart, passes in the data and draws it.

function drawChart() {
	
// Replace the data source URL on next line with your data source URL.	

var jsonData = $.ajax({
	url: $SCRIPT_ROOT + '/database',
	dataType: "json",
	async: false
	}).responseText;


// Create our data table out of JSON data loaded from server.
var data = new google.visualization.DataTable(jsonData);

// Instantiate and draw our chart, passing in some options.
var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
chart.draw(data, {width: 400, height: 240});

// Set chart options

}   // end of callback - drawChart
      
      

