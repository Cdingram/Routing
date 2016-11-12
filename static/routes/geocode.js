// on geocode searchbar keyup event handler
// should query through ajax call to get addresses
function geocode_keyup(searchbar){
	// delay and call search
	var query = $("input#"+searchbar).val();
	
	// call geocode search with query
	$.ajax({
		url: GEOCODE_URL,
		dataType: 'json',
		data:{address: query},
	 	success: function( data ) {
	 		// need to add results to dropdown and save address on click
	    	console.log( data );
	    	show_results(searchbar, data);
		},
		error: function( data ) {
			// handle error
	    	console.log( "ERROR" );
		}
	});
}