<?php

$servername = "localhost" ;
$username = "id7535697_krishnahome" ;
$password = "12345678" ;
$database = "id7535697_home" ;

$id = $_REQUEST["id"];
$status = $_REQUEST["status"];

if(isset($id)&&isset($status))
{

// create connection

$con =new mysqli($servername,$username,$password,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "UPDATE datalock set status='$status' where id = '$id'";

if($con->query($query)==TRUE)
{
	die("success");
}
else
{
	die("failed");
}
}
else
{
die("status or id is not set");	
}
?>