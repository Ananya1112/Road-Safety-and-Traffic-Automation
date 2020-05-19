<?php
$m=$_POST['a'];
$n=$_POST['b'];
$con=mysqli_connect("localhost","root");
mysqli_select_db($con,"project");
$q="select * from membership";
$result=mysqli_query($con,$q);
$nums=mysqli_num_rows($result);
$ra=mysqli_fetch_array($result);
?>

<html>
 <body>
    <table>
	 <tr>
	  <th>NAME</th>
	  <th>ADDRESS</th>
	  <th>PHONE-NUMBER</TH>
	  <th>ADHAR-NUMBER</th>
	  <TH>PARENTS-PHONE-NUMBER</TH>
	  <TH>PARENTS-NAME</TH>
	  
	 </tr>
	 
	 <?php
	 if($ra[0]==$m &&$ra[6]==$n){
	   for($i=1;$i<=nums;$i++)
	   {
		   $row=mysqli_fetch_array($result);
		 ?>
		 <tr>
		   <td><?php echo "$row[0]"; ?></td>
		   <td><?php echo"$row[1]";?></td>
		   <td><?php echo"$row[2]";?></td>
		   <td><?php echo"$row[3]";?></td>
		   <td><?php echo"$row[4]";?></td>
		   <td><?php echo"$row[5]";?></td>
		   <td><?php echo"$row[6]";?></td>
		 </tr>
		 <?php  
	   }
	 }
	 else
		 echo"first registration";
	 ?>
	 
	</table>
	 
 </body>
</html>