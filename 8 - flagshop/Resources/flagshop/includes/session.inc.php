<?php

require_once 'config.inc.php';
  
class Session {
    private $content = array();
    
    function set($k, $v) {
        $this->content[$k] = $v;
    }
    function get($k) {
        return $this->content[$k];
    }

    function save() {
        global $secret;
        $session = base64_encode(serialize($this));
        $hmac = hash_hmac("sha256", $session, $secret);
        setcookie('session', $session, 0, '/');
        setcookie('hmac', $hmac, 0, '/');
    }

    static function reset() {
        setcookie('session', null, time() - 3600, '/');
        setcookie('hmac', null, time() - 3600, '/');
    }

    static function init() {
        global $secret;
        if (!isset($_COOKIE['session']) || !isset($_COOKIE['hmac'])){
            return new Session();
        }
        $session = $_COOKIE['session'];
        $hmac = $_COOKIE['hmac'];
        $session_hmac = hash_hmac("sha256", $session, $secret);
        
        // Compare HMACs: if they do not match do not unsafely unserialize!
        if (strcmp($session_hmac, $hmac) == 0) {
            $session = unserialize(base64_decode($session));
            if (!$session){
                echo '<b><font color=red>[Session] Warning: invalid/malformed session! you have been logged out.</font></b>';
                return new Session();
            }
            return $session;
        } else {
            echo '<b><font color=red>[Session] Warning: invalid session hmac! you have been logged out.</font></b>';
            return new Session();
        }
    }
}

?>
