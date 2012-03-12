print """

	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html>

<head>
	<title>UCC Timetable Manager</title>
	<link rel="stylesheet" type="text/css" href="css/style.css" />
	
	<!-- Vlad 08/03/2012 BEGIN -->
	<script type="text/javascript" src="js/jquery-1.7.1.min.js"></script>
	<script type="text/javascript" src="js/utils.js"></script>
	<!-- Vlad 08/03/2012 END -->
	
	
</head>
<body>
<div id="page">
	<!-- vimeo like havigation from here 
	http://www.jankoatwarpspeed.com/post/2009/01/19/Create-Vimeo-like-top-navigation.aspx
	-->
	<ul id="menu"> 
		<li class="logo"> 
			<img style="float:left;" alt="" src="images/menu/menu_left.png"/> 
		</li> 
		<li><a href="#">Home</a> 
		</li> 
		<li><a href="#">Groups</a> 
			<ul id="groups"> 
				<li>
					<img class="corner_inset_left" alt="" src="images/menu/corner_inset_left.png"/> 
					<a href="#">Add group</a>
					<img class="corner_inset_right" alt="" src="images/menu/corner_inset_right.png"/>
				</li> 
				<li><a href="#">Delete groups</a></li> 
				<li><a href="#">Edit groups</a></li>
				<li><a href="#">Group users management</a></li>				
				<li class="last"> 
					<img class="corner_left" alt="" src="images/menu/corner_left.png"/> 
					<img class="middle" alt="" src="images/menu/dot.gif"/> 
					<img class="corner_right" alt="" src="images/menu/corner_right.png"/> 
				</li> 
			</ul> 
		</li>

		<!-- modules menu start -->
		<li><a href="#">Modules</a> 
			<ul id="modules"> 
				<li>
					<img class="corner_inset_left" alt="" src="images/menu/corner_inset_left.png"/> 
					<a href="#">Add module</a>
					<img class="corner_inset_right" alt="" src="images/menu/corner_inset_right.png"/>
				</li> 
				<li><a href="#">Delete modules</a></li> 
				<li><a href="#">Edit modules</a></li> 
				<li><a href="#">Split module into groups</a></li>
				<li><a href="#">Check attendance availability</a></li>				
				<li><a href="#">Modules groups management</a></li> 
				<li class="last"> 
					<img class="corner_left" alt="" src="images/menu/corner_left.png"/> 
					<img class="middle" alt="" src="images/menu/dot.gif"/> 
					<img class="corner_right" alt="" src="images/menu/corner_right.png"/> 
				</li> 
			</ul> 
		</li>
		<!-- modules menu end -->


		<!-- Students menu start -->
		<li><a href="#">Students</a> 
			<ul id="students"> 
				<li>
					<img class="corner_inset_left" alt="" src="images/menu/corner_inset_left.png"/> 
					<a href="#">Browse students</a>
					<img class="corner_inset_right" alt="" src="images/menu/corner_inset_right.png"/>
				</li> 
				<li><a href="#">Add student to group</a></li> 
				<li><a href="#">Add Erasmus students</a></li> 
				<li><a href="#">Remove students from group</a></li> 
				<li class="last"> 
					<img class="corner_left" alt="" src="images/menu/corner_left.png"/> 
					<img class="middle" alt="" src="images/menu/dot.gif"/> 
					<img class="corner_right" alt="" src="images/menu/corner_right.png"/> 
				</li> 
			</ul> 
		</li>
		<!-- students menu end -->
		
		<li id="vimeo-menu-filler">&nbsp;</li>
		<li class="searchContainer">  
			<div> 
			<form action="#" method="post">
				<input type="text" id="login-email" name="Email" value="Email" />
				<input type="text" id="login-pw" name="Password" value="Password" />
				<input type="submit" value="Login" />
			</form>  
		</li> 
	</ul> 
	<img style="float:left;" alt="" src="images/menu/menu_right.png"/>
	<div style="clear:both;"></div>
	
	<h1>Groups management</h1>
	
	<!-- Vlad 08/03/2012 BEGIN -->
	
	<nav id="breadcrumbs">
		<a href="#">Groups</a> &raquo; <a href="#">Add group</a>
	</nav>
	
	<h2>Add new group</h2>
	
	<form>
		<p>
			<label for="addGroupName">Group name:</label><br />
			<input type="text" name="addGroupName" id="addGroupName" style="width:50%" />
		</p>

		<p>
			<label for="addGroupDescription">Group description:</label><br />
			<textarea name="addGroupDescription" id="addGroupDescription" style="width:50%;height:500px;"></textarea>
		</p>

		<p>
			<input type="submit" id="addGroupSubmit" value="Create group &raquo;" />
		</p>
	</form>
	<!-- Vlad 08/03/2012 END -->
		
	
	<div id="footer">
		Copyright &copy; 2012, University College Cork
	</div>
	
</div> <!-- div id="page" -->
<!-- Vlad 08/03/2012 BEGIN -->
<div id="AI"><div>Please wait, loading...</div></div>
<script type="text/javascript">
$(window).load(function () 
{
	hideAI( );
	$( '#addGroupName' ).focus( );

	$("#addGroupSubmit").click( function( ) 
	{
		showAI( );
		var params = { groupName : $( '#addGroupName' ).val( ).trim( ), groupDescription: $( '#addGroupDescription' ).val( ).trim( ) };
		
		if ( !params.groupName )  
		{
			hideAI( );
			alert( "Group name is required." );
			$( '#addGroupName' ).focus( );
			return false;
		}
		
		if ( !params.groupDescription )  
		{
			hideAI( );
			alert( "Group description is required." );
			$( '#addGroupDescription' ).focus( );
			return false;
		}
		
		$.ajax({
		  type: "POST",
		  url: 	"addgroups.py",
		  data: params }).done( 
			  function( msg ) 
				{
					msg = msg.trim();
					hideAI( );

					if ( msg.toLowerCase( ) == "ok" ) 
					{
						alert( "The '"+ params.groupName +"' group was successfully added!" );
						$( '#addGroupName' ).val( '' );
						$( '#addGroupDescription' ).val( '' );
					}
					else
					{
						alert( "Error: "+ msg );
					}
				});

		return false;
	});
});
</script>
<!-- Vlad 08/03/2012 END -->
</body>
</html>

"""