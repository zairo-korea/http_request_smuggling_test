<?php
if(!isset($_GET['url'])){
?>
	<a href="./?url=https://www.kitribob.kr/">KITRI BoB</a>
<?php	
}else{
	header("Location: {$_GET['url']}");
}
?>