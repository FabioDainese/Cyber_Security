<?php
require_once 'includes/functions.inc.php';

if (is_logged_in()) {
    header('location: /');
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    if (login($_POST['username'], $_POST['password'])) {
        header('location: /');
    }else{
        $alert = "Wrong username or password!";
    }
}

?>

<?php
require_once 'templates/header.inc.php';
?>

<div class"container">

  <?php
  if (isset($alert)) {
  ?>
    <div class="m-3 alert alert-danger" role="alert">
      <?php echo $alert; ?>
    </div>
  <?php
  }
  ?>

  <div class='text-center mt-5'>
    <form class="form-signin" method="post" action="/login.php">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputUser" class="sr-only">Username</label>
      <input type="text" id="inputUser" name="username" class="form-control" placeholder="Username" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Log in</button>
      <p>or <a href="register.php">sign up</a></p>
    </form>
  </div>
</div>

<?php
require_once 'templates/footer.inc.php';
?>
