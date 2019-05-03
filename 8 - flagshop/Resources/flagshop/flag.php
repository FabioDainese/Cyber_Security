<?php
require_once 'includes/functions.inc.php';
require_once 'templates/header.inc.php';
?>

<div class="spacer mt-5"></div>

<?php
if (!is_logged_in()) {
?>

    <div class="container">
      <div class="card-deck mb-3 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal">Please log in</h4>
          </div>
          <div class="card-body">
            <ul class="list-unstyled mt-3 mb-4">
              <li class="alert alert-info">
                Please <a href="login.php">log in</a><br>
                or <a href="register.php">register</a> for free!
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

<?php
} else {
?>
  <?php
  if (is_admin()) {
  ?>
      <div class="container">
        <div class="card-deck mb-3 text-center">
          <div class="card mb-4 shadow-sm">
            <div class="card-header">
              <h4 class="my-0 font-weight-normal">Redeem flag</h4>
            </div>
            <div class="card-body">
              <h3 class="card-title pricing-card-title">
                <span class='fa fa-flag'></span>
                <span class='fa fa-flag'></span>
                <span class='fa fa-flag'></span>
              </h3>
              <ul class="list-unstyled mt-3 mb-4">
                <li>Hi <b>admin</b>!</li>
                <li>Here is your flag: <code>flg{<?php echo $flag; ?>}</code></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  <?php
  }else{
  ?>
      <div class="container">
        <div class="card-deck mb-3 text-center">
          <div class="card mb-4 shadow-sm">
            <div class="card-header">
              <h4 class="my-0 font-weight-normal">Purchase flag</h4>
            </div>
            <div class="card-body">
              <h3 class="card-title pricing-card-title">
                Standard offer: <span class="text-muted">100000 gold coins</span>
              </h3>
              <ul class="list-unstyled mt-3 mb-4">
                <li class="alert alert-danger">
                  Our payment system is out of order...
                  Try again later.
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  <?php
  }
  ?>
<?php
}
?>

<?php
require_once 'templates/footer.inc.php';
?>
