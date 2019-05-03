<?php

require_once 'session.inc.php';

function get_username() {
    $session = Session::init();
    return $session->get("username");
}

function is_logged_in() {
    return get_username() !== NULL;
}

function is_admin() {
    return get_username() === "admin";
}

function logout() {
    Session::reset();
}

function login($user, $password) {
    global $dbusers;

    $session = Session::init();
    $document = array('username' => (string) $user, 'password' => (string) sha1($password));
    $cursor = $dbusers->find($document);
    if ($cursor->hasNext()){
        $user = $cursor->next();
        $session->set("username", $user["username"]);
        $session->save();
        return true;
    }
    return false;
}

function register($user, $password) {
    global $dbusers;

    $document = array('username' => (string) $user);
    if ($dbusers->count($document) > 0){
        return false;
    }
    $document['password'] = (string) sha1($password);
    $dbusers->insert($document);
    return true;
}

?>
