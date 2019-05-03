<?php

$secret = '<SECRET>';
$flag = '<FLAG>';

$client = new MongoClient("mongo");
$dbusers = $client->database->users;

?>
