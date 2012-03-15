function hideAI( )
{
	$( '#AI' ).hide( );
}

function showAI( )
{
	$( '#AI' ).show( );
}

function initDropDowns( dropDownID, onSelectCallBack )
{
	$("#"+ dropDownID +".dropdown dt a").click(function() {
		$("#"+ dropDownID +".dropdown dd ul").toggle();
	});
	
	$("#"+ dropDownID +".dropdown dd ul li a").click(function() {
		var text = $(this).html();
		$("#"+ dropDownID +".dropdown dt a span").html(text);
		$("#"+ dropDownID +".dropdown dd ul").hide();
		
		if ( onSelectCallBack  )
		{
			onSelectCallBack( );
		}
	}); 
	
	$(document).bind('click', function(e) {
		var $clicked = $(e.target);
		if (! $clicked.parents().hasClass("dropdown") )
			$("#"+ dropDownID +".dropdown dd ul").hide();
	});
}