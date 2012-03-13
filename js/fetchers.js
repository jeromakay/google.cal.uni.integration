function fetchGroups( callbackOK, callbackNoGroups )
{
	fetchData( "groups", callbackOK, callbackNoGroups )
}

function fetchModules( callbackOK, callbackNoGroups )
{
	fetchData( "modules", callbackOK, callbackNoGroups )
}

/**
 * @param dataType The type of data to fetch: groups, modules, users
 */
function fetchData( dataType, callbackOK, callbackNoResults ) 
{
	showAI( );

				// groups
				var json = {results: [ 
								{id: 1, group_type: 1, group_gid: "2dabd109cf892b94e72563da710669c4", title: "food_and_science_ck401_3rd_web_sys_eng", description: "Everyone in Web Systems Engineering" }, 
								{id: 2, group_type: 1, group_gid: "ee8efdd53326e275390b866473aac247", title: "food_and_science_ck401_3rd_cs", description: "Everyone in Computer Science Hons" }, 
								{id: 3, group_type: 1, group_gid: "9f1319fde74c8ca728ec7452d4e85521", title: "arts_music", description: "Everyone studying Music Hons." }, 
								{id: 4, group_type: 2, group_gid: "9459e2b377f25454ee47133c03205076", title: "arts_music_trad_music_lecturers", description: "Lecturers teaching Trad Irish Music." }, 
								{id: 5, group_type: 3, group_gid: "7e9cf516ec7fcc55476fe44696cfca66", title: "foot_and_science_microbiology_lab_assist", description: "Labs assistants for the microbiology lecture's labs." },
								{id: 6, group_type: 1, group_gid: "f94d66f27497e84e10b2843ee718a078", title: "erasmus_2011_Juan_Carlos_Montero_1 09868111", description: "Erasmus 2011 student, Juan Carlos Montero." },
								{id: "wse@jeromakay.com", group_type: 1, group_gid: "wse", title: "real_deal", description: "This is the real deal." } ],
								
							groupTypes: [
								{ id: 1, name: "students" },
								{ id: 2, name: "lecturers" },
								{ id: 3, name: "assistants" }
							] };

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
						callbackOK( json );
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