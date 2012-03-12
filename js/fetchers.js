function fetchGroups( callbackOK, callbackNoGroups )
{
	fetchData( "groups", callbackOK, callbackNoGroups )
}

/**
 * @param dataType The type of data to fetch: groups, modules, users
 */
function fetchData( dataType, callbackOK, callbackNoResults ) 
{
	showAI( );

				var json = {results: [ 
								{id: 1, title: "food_and_science_ck401_3rd_web_sys_eng", description: "Everyone in Web Systems Engineering", groupType: "students" }, 
								{id: 2, title: "food_and_science_ck401_3rd_cs", description: "Everyone in Computer Science Hons", groupType: "students" }, 
								{id: 3, title: "arts_music", description: "Everyone studying Music Hons.", groupType: "students" }, 
								{id: 4, title: "arts_music_trad_music_lecturers", description: "Lecturers teaching Trad Irish Music.", groupType: "lecturers" }, 
								{id: 5, title: "foot_and_science_microbiology_lab_assist", description: "Labs assistants for the microbiology lecture's labs.", groupType: "assistants" },
								{id: 6, title: "erasmus_2011_Juan_Carlos_Montero_109868111", description: "Erasmus 2011 student, Juan Carlos Montero.", groupType: "erasmus_students" }
							]};

				// move me begin
				if ( json && json.results ) 
				{
					if (  json.results.length == 0 )
					{
						if ( callbackNoResults )
						{
							callbackNoResults( );
						}
						else
						{
							alert( "There are no "+ dataType +" stored in the application's DB yet!" );
						}
					}
					else
					{
						callbackOK( json.results );
					}
				}
				else
				{
					if ( json && json.error )
					{
						alert( "Error: "+ json.error );
					}
					else
					{
						alert( "Something went wrong, could not fetch the list of "+ dataType +", please refresh the page and try again!" );
					}
				}
				// move me end
				return;

	$.getJSON({
	  type: "POST",
	  url: 	"createGroup.py",
	  data: params }).done( 
		  function( json ) 
			{
				hideAI( );

				if ( msg.toLowerCase( ) == "ok" ) 
				{
					alert( "The \""+ params.groupName +"\" group was successfully added!" );
					$( '#addGroupName' ).val( '' );
					$( '#addGroupDescription' ).val( '' );
				}
				else
				{
					alert( "Error: "+ msg );
				}
			});

}