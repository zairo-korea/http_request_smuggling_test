<?php
$db = new SQLite3('comments.db');
$db->exec("CREATE TABLE IF NOT EXISTS comment(id INTEGER PRIMARY KEY AUTOINCREMENT, nickname TEXT, value TEXT)");
$page = $_GET['page'];

switch($page){
	case "write":
		$page = "write";
		break;
	default:
		$page = "view";
}

if($page === "write"){
	if(isset($_POST['nickname']) && isset($_POST['comment'])){
		$nickname = $_POST['nickname'];
		$comment = $_POST['comment'];
		$db->exec('BEGIN');
		$stm = $db->prepare("INSERT INTO comment(nickname, value) VALUES (?, ?)");
		$stm->bindParam(1, $nickname);
		$stm->bindParam(2, $comment);
		$stm->execute();
		$db->exec('COMMIT');
		header("Location: /?page=view");
	}
}else if($page === "view"){
?>

<form method="post" action="/?page=write">
	<center>	
	Nickname: <input type="text" name="nickname" value=""><br>
	<textarea name="comment" cols="100" rows="20"></textarea><br>
	<input type="submit">
	</center>	
</form>
<br>

<center>
<?php
	$res = $db->query('SELECT nickname, value FROM comment ORDER BY id DESC');
	while ($row = $res->fetchArray()) {
		echo "<b>{$row['nickname']}</b>: <pre>{$row['value']}</pre><br>\n";
	}	
?>
<center>
	
<?php
}
?>