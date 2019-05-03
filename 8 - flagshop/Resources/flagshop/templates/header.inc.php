
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Flag Shop</title>

    <!-- Bootstrap core CSS -->
    <link href="https://getbootstrap.com/docs/4.1/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Font Awesome icons -->
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <style>
    html {
          font-size: 14px;
    }
    @media (min-width: 768px) {
          html {
                  font-size: 16px;
                    }
    }

    .container {
          max-width: 960px;
    }

    .pricing-header {
          max-width: 700px;
    }

    .card-deck .card {
          min-width: 220px;
    }

    .form-signin {
          width: 100%;
            max-width: 330px;
              padding: 15px;
                margin: auto;
    }
    .form-signin .form-control {
          position: relative;
            box-sizing: border-box;
              height: auto;
                padding: 10px;
                  font-size: 16px;
    }
    .form-signin .form-control:focus {
          z-index: 2;
    }
    .form-signin input[type="email"] {
          margin-bottom: -1px;
            border-bottom-right-radius: 0;
              border-bottom-left-radius: 0;
    }
    .form-signin input[type="password"] {
          margin-bottom: 10px;
            border-top-left-radius: 0;
              border-top-right-radius: 0;
    }
    .titlelink, .titlelink:hover {
        text-decoration: none;
        color: inherit;
    }
    </style>
  </head>

  <body>

    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
      <h5 class="my-0 mr-md-auto font-weight-normal">
          <span class="fa fa-flag"></span>
          <a class="titlelink" href="/">FlagShop</a>
      </h5>
      <?php 
      if (is_logged_in()) {
      ?>
          <a class="btn btn-disabled">
          <span class="fa fa-user"></span>
          <span><?php echo htmlentities(get_username()); ?></span>
          </a>
          <a class="btn btn-outline-primary" href="logout.php">Log out</a>
      <?php
      } else {
      ?>
          <nav class="my-2 my-md-0 mr-md-3">
            <a class="p-2 text-dark" href="login.php">Log in</a>
          </nav>
          <a class="btn btn-outline-primary" href="register.php">Sign up</a>
      <?php
      }
      ?>
    </div>

