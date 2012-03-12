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
			
	var params = {entityID: entityID }

	$.getJSON({
	  type: "POST",
	  url: 	"deleteGroup.py",
	  data: params }).done( 
		  function( json ) 
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