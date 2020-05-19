<?php
$m=$_POST['a'];
$n=$_POST['b'];
$o=$_POST['c'];
$p=$_POST['d'];
$q=$_POST['e'];
$r=$_POST['f'];
$s=$_POST['g'];


$con=mysqli_connect("localhost","root");
	mysqli_select_db($con,"project");
	
		$query1="INSERT INTO membership(NAME,ADDRESS,PHONE-NO,ADHAR-NO,PARENTS-PHONE-NO,PARENTS-NAME,PASSWORD) value('$m','$n',$o,$p,$q,'$r','$s')";
		$status=mysqli_query($con,$query1);
		mysqli_close($con);
?><html> 
 <body style="background-color:  #57daf0">
   <p>
     <?php
	 if($status==1)
		 echo "registration confirmed";
	 else 
		 echo "registration failed";
	 ?>
   </p>
</body>
</html>