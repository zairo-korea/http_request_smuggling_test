<?php
session_start();
if(!isset($_GET['script'])){
?>
<form>
	<center>	
	<textarea name="script" cols="100" rows="20"><script>alert(1);</script></textarea><br>
	<input type="submit">
	</center>	
</form>
<?php
}else{
	echo $_GET['script'];
}
?>
