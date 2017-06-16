/**
 * Created by aric on 15-12-28.
 */
// jQuery function to create a chart for each of the HighCharts Chart Options
// JSON object (_chartit_hco_array) passed to web page from the view.
$(document).ready(function() {
	$.each(_chartit_hco_array_spider, function(index, chartoptions) {
		chart = new Highcharts.Chart(chartoptions);
	});

    $.each(_chartit_hco_array_network, function(index, chartoptions) {
		chart = new Highcharts.Chart(chartoptions);
	});
    $.each(_chartit_hco_array_site, function(index, chartoptions) {
		chart = new Highcharts.Chart(chartoptions);
	});
});
