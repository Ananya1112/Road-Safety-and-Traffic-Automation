<html>  
<head>
<!--<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<style style="type/css"> 

 
	</style>-->
</head>
<body style = "background:url(form1.jpg)">
 <div class="text-center p-3 mx-auto" style="color:#6110E7 " width="800px" height="40px" >
 
  
   <div class="container">
   
   <div id="table" class="text-center mx-auto">
    <h3  >REGISTRATION PORTAL</h3><br>
   <form method="POST" action="register.php">
    <table>
    <tr>
     <th> NAME :</th><td><input  type="text" name="a" required=""></td>
	  </tr>
        <tr>
     <th> ADDRESS:</th><td><input  type="text" name="b" required=""></td>
	  </tr>
	      <tr>
     <th> PHONE-NO :</th><td><input   type="number" name="c" required=""></td>
	  </tr>
	      <tr>
     <th> ADHAR :</th><td><input   type="number" name="d" required=""></td>
	  </tr>
	      <tr>
     <th> PARENTS-PHONE-NO.:</th><td><input   type="number" name="e" required=""></td>
	  </tr>
	      <tr>
     <th> PARENTS-NAME :</th><td><input   type="text" name="f" required=""></td>
	  </tr>
	      <tr>
     <th> PASSWORD :</th><td><input   type="password" name="g" required=""></td>
	  </tr>
	      <tr>
     <th> SUBMIT :</th><td><input   type="submit" value="SUBMIT" ></td>
	  </tr>
	      <tr>
     <th> RESET :</th><td><input   type="reset" value="RESET"></td>
	  </tr>
	</table>
   </form>
  
 
   <a href='login.php' style="color:black">Click Here </a>To Login</div>
   </div>
  <!-- <script type="text/javascript">
       document.getElementById('e').onclick=function(){
		   var name="document.getElementById('a').value";
		   var email="document.getElementById('a').value";
		   var password="document.getElementById('a').value";
		   var phone="document.getElementById('a').value";
		   var t=name.length;
		   var u=email.length;
		   var v=password.length;
		   var w=phone.length;
		   if(t>0&&u>0&&v>0&&w>0)
		   {
			   alert('your registration is confirmed');
		   }
		   
	   }
   </script>-->
   
   </body>
</html>