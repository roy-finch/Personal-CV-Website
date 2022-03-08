<?php
    $name = $_POST['name'];
    $email = $_POST['mail'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    $cmp_msg = wordwrap("Message sent from front-site.\nEmail Address:$email\nMessage:$message", 60);

    mail("royfinch99@hotmail.com", $subject, $cmp_msg);
    die();
?>