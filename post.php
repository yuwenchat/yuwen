<?php
session_start();
if(isset($_SESSION['name'])){

    $text = $_POST['text'];
     
    $text_message = "<div class='msgln'><span class='chat-time'>".date("g:i A")."</span> <b class='user-name'>".$_SESSION['name']."</b> ".stripslashes(htmlspecialchars($text))."<br></div>";
    $newStr = preg_replace('/[^\x{4e00}-\x{9fa5}]/u', '', $_GET['content']);
        $countstr = mb_strlen($newStr,"utf-8");
    file_put_contents("log.html", $text_message, FILE_APPEND | LOCK_EX);
}
?>