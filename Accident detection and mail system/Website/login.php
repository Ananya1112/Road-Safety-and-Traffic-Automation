<html>
<head>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <style>
	  #table{
		  margin-top:130px;
		  text:white;
		  background:rgba(0,0,-1,.5);
		  box-shadow:0 15px 25px rgba(0,0,0,.5);
		  border-radius:10px;
		  padding-top:10px;
	  }
	  h2{
		  color:white;
	  }
	  #logo{
		  margin-top:100px;
	  }
	</style>
  </head>
<body style = "background-image:url(login1.jpg)">
<div class="container">
   <div id="table" class=" text-center mx-auto" style="width:300">
  <!-- <img src="logomnnit.jpg" width="100"height="100"/>-->
      <form method="POST" action="view.php">
          <h2 class="my-3">Login Portal</h2>
		 
             <input style="border-radius:10px" type="text" name="a" class="text-center mx-auto my-3"placeholder="USERNAME" size="30" required="" >
            <input style="border-radius:10px" type="password" class="text-center mx-auto" placeholder="PASSWORD" name="b" size="30" required=""></br></br>
            <input  style="border-radius:10px" type="submit" value="Submit" class="bg-primary" ></br>
             <input style="border-radius:10px"type="reset" class="bg-primary my-3" value="Reset" width="100px"><br>
			 <span style="color:white">For new registration <a class="text-warning" href="index.php">CLICK HERE</a></span>
	  
      </form>
     </div>
	 
	 </div>

    </body>
</html>