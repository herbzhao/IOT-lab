
//	Any Jquery event here
$(document).ready(function(){

	$('h1').click(function(){
		$('h1').fadeOut();}
		);
});


// Google chart here

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['gauge']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the  chart, passes in the data and draws it.

function drawChart() {
	
// Replace the data source URL on next line with your data source URL.	


	


var options = {
//  animation.easing:out,
  width: 400, height: 200,
  redFrom: 4.5, redTo: 5,
  yellowFrom:4, yellowTo: 4.5,
  minorTicks: 0.01, max:5
};
   

var jsonData = $.ajax({
	url: $SCRIPT_ROOT + '/voltage',
	dataType: "json",
	async: false
	}).responseText;
	
var data = new google.visualization.DataTable(jsonData);





function updateChart () {
	$.ajax({
		url: $SCRIPT_ROOT + '/voltage',
		dataType: "json",
		success: function (response) {
			
			var jsonData = $.ajax({
			url: $SCRIPT_ROOT + '/voltage',
			dataType: "json",
			async: false
			}).responseText;
			
			var data = new google.visualization.DataTable(jsonData);
			// use response to create/update DataTable
			chart.draw(data, options);
			// update the chart again in 30 ms
			setTimeout(updateChart, 30);
		},
		error: function (response) {}
});
}



var data = new google.visualization.DataTable(jsonData);

// Create our data table out of JSON data loaded from server.
//var data = new google.visualization.DataTable(jsonData);

// Instantiate and draw our chart, passing in some options.

var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

updateChart();

// Set chart options

//updateChart();

}   // end of callback - drawChart
      
      

