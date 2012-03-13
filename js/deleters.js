function deleteGroup( groupID, callbackOK )
{
	deleteEntity( "group", groupID, callbackOK )
}

/**
 * @param dataType The type of data to delete: groups, modules, users
 */
function deleteEntity( dataType, entityID, callbackOK ) 
{
	showAI( );
	
	var params = { dataType: dataType, entityID: entityID }
	
	$.ajax({
	  type: "POST",
	  url: 	"DeleterAjax",
	  data: params }).done( 
		  function( msg ) 
			{
				hideAI( );
				
				if ( msg.toLowerCase( ) == "ok" ) 
				{
					if ( callbackOK )
					{
						callbackOK( );
					}
				}
				else
				{
					alert( "Error: "+ msg );
				}
			});

}