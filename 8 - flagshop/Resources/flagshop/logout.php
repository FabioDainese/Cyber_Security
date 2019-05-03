<?php
require_once 'includes/functions.inc.php';

logout();
header('location: /');

require_once 'templates/header.inc.php';
?>

<b>Logging out...</b>

<?php
require_once 'templates/footer.inc.php';
?>
