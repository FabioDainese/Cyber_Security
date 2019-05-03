<?php
require_once 'includes/functions.inc.php';

if (is_logged_in()) {
    header('location: /');
}

if (isset($_POST['username']) && isset($_POST['password']) 
    && isset($_POST['password_confirm'])) {
    if ($_POST['password'] !== $_POST['password_confirm']) {
        $alert = 'Passwords do not match!';
    } else {
        if (register($_POST['username'], $_POST['password'])) {
            $info = 'User successfully registered! Please <a href="login.php">Log in</a>';
        }else{
            $alert = 'User already exists! try a different username.';
        }
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

  <?php
  if (isset($info)) {
  ?>
    <div class="m-3 alert alert-info" role="alert">
      <?php echo $info; ?>
    </div>
  <?php
  }
  ?>

  <div class='text-center mt-5'>
    <form class="form-signin" method="post" action="/register.php">
      <h1 class="h3 mb-3 font-weight-normal">Register a new user</h1>
      <label for="inputUser" class="sr-only">Username</label>
      <input name="username" type="text" id="inputUser" class="form-control" placeholder="Username" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <label for="inputPassword2" class="sr-only">Password (confirmation)</label>
      <input name="password_confirm" type="password" id="inputPassword2" class="form-control" placeholder="Password (confirmation)" required>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign up</button>
      <p>or <a href="login.php">Log in</a></p>
    </form>
  </div>
</div>

<?php
require_once 'templates/footer.inc.php';
?>
