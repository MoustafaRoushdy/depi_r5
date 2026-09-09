<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$dbname = 'mysql';  // don't update this line 
$dbuser = 'admin';
$dbpass = '';
$dbhost = '';
 
$link = mysqli_connect($dbhost, $dbuser, $dbpass) or die("Unable to Connect to '$dbhost'");
mysqli_select_db($link, $dbname) or die("Could not open the db '$dbname'");
 
$test_query = "SHOW TABLES FROM $dbname";
$result = mysqli_query($link, $test_query);
 
$tblCnt = 0;
while($tbl = mysqli_fetch_array($result)) {
  $tblCnt++;
}
 echo "Connected successfully\n";
?>
