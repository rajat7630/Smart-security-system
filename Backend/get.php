<?php

$servername = "localhost" ;
$username = "id7535697_krishnahome" ;
$password = "12345678" ;
$database = "id7535697_home" ;


// create connection

$con =new mysqli($servername,$username,$password,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "select * from datalock";
	
$result = $con->query($query);

if($result->num_rows>0)
{
	$response["status"] = array();
	
	 while($row = $result->fetch_assoc()) {
        
	 $temp = array("id"=>$row["id"],"status"=>$row["status"]);
			 
			 array_push($response["status"],$temp);
    }
	
	die(json_encode($response["status"]));
}
else
{
	die("failed");
}


?>