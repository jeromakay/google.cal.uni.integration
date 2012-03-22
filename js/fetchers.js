function fetchGroups( callbackOK, callbackNoGroups )
{
	fetchData( "groups", callbackOK, callbackNoGroups )
}

function fetchModules( callbackOK, callbackNoGroups )
{
	fetchData( "modules", callbackOK, callbackNoGroups )
}

function fetchGroupUsers( groupID, callbackOK, callbackNoGroups ) 
{
	fetchData( "users", groupID, callbackOK, callbackNoGroups )
}

function fetchAllUsers( callbackOK, callbackNoGroups ) 
{
	fetchData( "users", callbackOK, callbackNoGroups )
}

/**
 * @param dataType The type of data to fetch: groups, modules, users
 * @param subDataID if we're fetching users from a group ID
 */
function fetchData( dataType, callbackOK, callbackNoResults, subDataID ) 
{
	showAI( );
	/*
	
	var json;
	
	if ( dataType == "groups" )
	{

				// groups
				json = {results: [ 
								{id: 1, group_type: 1, group_gid: "2dabd109cf892b94e72563da710669c4", title: "test", description: "Everyone in Web Systems Engineering" }, 
								//{id: 2, group_type: 1, group_gid: "ee8efdd53326e275390b866473aac247", title: "food_and_science_ck401_3rd_cs", description: "Everyone in Computer Science Hons" }, 
								//{id: 3, group_type: 1, group_gid: "9f1319fde74c8ca728ec7452d4e85521", title: "arts_music", description: "Everyone studying Music Hons." }, 
								//{id: 4, group_type: 2, group_gid: "9459e2b377f25454ee47133c03205076", title: "arts_music_trad_music_lecturers", description: "Lecturers teaching Trad Irish Music." }, 
								//{id: 5, group_type: 3, group_gid: "7e9cf516ec7fcc55476fe44696cfca66", title: "foot_and_science_microbiology_lab_assist", description: "Labs assistants for the microbiology lecture's labs." },
								//{id: 6, group_type: 1, group_gid: "f94d66f27497e84e10b2843ee718a078", title: "erasmus_2011_Juan_Carlos_Montero_1 09868111", description: "Erasmus 2011 student, Juan Carlos Montero." },
								//{id: 7, group_type: 1, group_gid: "wse@jeromakay.com", title: "real_deal", description: "This is the real deal." } 
								],
								
							groupTypes: [
								{ id: 1, name: "students" },
								{ id: 2, name: "lecturers" },
								{ id: 3, name: "assistants" }
							] };
	} 
	else if ( dataType == "modules" )
	{
	
				// modules 
				json = {results: [ 
							{module_id: 1, google_cal_id: "c4ca4238a0b923820dcc509a6f75849b", title: "CS1101", description: "Systems organization" }, 
							{module_id: 2, google_cal_id: "c81e728d9d4c2f636f067f89cc14862c", title: "CS2500 Lab", description: "JAVA Programming" }, 
							{module_id: 3, google_cal_id: "eccbc87e4b5ce2fe28308fd9f2a7baf3", title: "cs3313", description: "Middleware" } ] };
	} 
	else if ( dataType == "users" )
	{
		if ( typeof subDataID  != 'undefined' )
		{
			json = {results: [ ] };
		}
		else
		{
			json = {results: [ 
						{gID: "79f65a600ea5079115d4de4028a6805d", UID: "109811456", name: "Brian Walsh" }, 
						{gID: "14fd98f76815c4a4d9f9fecbb91c4dd0", UID: "109455821", name: "Vladimir Ghetau" }, 
						{gID: "79f65a600ea5079115d4de4028a6805d", UID: "109589951", name: "Tomas William Jackson" } ] };
		}
	}
	
				// move me begin
				if ( json && json.results ) 
				{
					if (  json.results.length == 0 )
					{
						if ( callbackNoResults )
						{
							callbackNoResults( );
						}
					}
					else if ( callbackOK )
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
				}
				// move me end
				return;
				
				*/
				
	var params = {
		"dataType": dataType,
		"subDataID": subDataID
	}

	$.ajax({
	  type: "POST",
	  url: 	"fetchers",
	  data: params }).done( 
		  function( msg ) 
			{
				json = jQuery.parseJSON( msg );


				if ( json && json.results ) 
				{
					if (  json.results.length == 0 )
					{
						if ( callbackNoResults )
						{
							callbackNoResults( );
						}
					}
					else if ( callbackOK )
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
						alert( 'The json you sent, is not valid.' );
					}
				}
			});
}