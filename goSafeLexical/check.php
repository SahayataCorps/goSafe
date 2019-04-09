
<!DOCTYPE html>
<html>
<head>
	<title>Checking...</title>
</head>
<body>
	<?php
	$a = $_POST['url'];
$myfile = fopen("url.txt","w");
fwrite($myfile, $a);
sleep(2); 
fclose($myfile);
$result = exec("C:\\Python27\\python.exe chor2.py ");
sleep(3);
$myfile2 = fopen("output.txt","r");
echo fread($myfile2, filesize("output.txt"));
unlink("output.txt");
fclose($myfile2);

$results_array = $result;
echo "<p>".$results_array."</p>";
?>
</body>
</html>