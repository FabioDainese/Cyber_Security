<?php
require_once 'includes/functions.inc.php';
require_once 'templates/header.inc.php';
?>


    <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
      <h1 class="display-4">Pricing</h1>
      <p class="lead">
          With over 5 years of exeprience our consultats know exactly how to help
          you with any of your flag needs!
      </p>
    </div>

    <div class="container">
      <div class="card-deck mb-3 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal">VIP</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">FREE</h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>A free flag!</li>
              <li>Gives a <code>0.5</code> bonus on the exam score.</li>
              <li>Only obtainable by the <b>admin</b> VIP account.</li>
            </ul>
            <?php if (is_logged_in() && !is_admin()) {
            ?>
                <a class="btn btn-lg btn-block btn-outline-primary"><s>Redeem for free</s></a>
            <?php
            } else {
            ?>
                <a href="flag.php" class="btn btn-lg btn-block btn-outline-primary">Redeem for free</a>
            <?php
            }
            ?>
          </div>
        </div>
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal">Standard</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">100000 <small class="text-muted">gold coins</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>A quite expensive flag...</li>
              <li>Gives a <code>0.5</code> bonus on the exam score.</li>
              <li>Best price-benefit ratio!</li>
            </ul>
            <a href="flag.php" class="btn btn-lg btn-block btn-primary">Purchase</a>
          </div>
        </div>
      </div>
     </div>

<?php
require_once 'templates/footer.inc.php';
?>
