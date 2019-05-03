# Introduction
This challenge was designed to put into practice in a '*real*' world situation some server-side web attacks involving a couple of *PHP* vulnerabilities (18<sup>th</sup> March 2019).

# Challenge Description
This challenge consists of a simple platform where you can register to it. Once you have logged in, the sytem will load a "pricing" page, where only if you are the admin user you can see the *flag* (`"VIP"` tab). Obviously we don't know the admin password, but we are going to use some *PHP* vulnerabilities in order to gain unathorized access, as admin, and get the *FLAG*.

* Website: [https://flagshop.seclab.dais.unive.it](https://flagshop.seclab.dais.unive.it)
* Source files: [flagshop.tgz](Resources/flagshop.tgz) (ba2d00c18d289b4a52fd2772af1192ea56b6d689 sha1sum)

## Original Description
>With over 5 years of exeprience our consultats know exactly how to help you with any of your flag needs!
>
>Visit our [website](https://flagshop.seclab.dais.unive.it), you won't regret it!

# Solution
Every time you log into the platform a `$session` variable is created, which basically it consists of an associative array that contains the current user's name. After that the back-end will set a cookie `'session'` with the following content: `base64_encode( serialize($session) )`.

Every time the `'index.php'` page is called up, to understand whether to create an `'admin page'` (flag) or not, the `'is_admin()'` function is called, which in turn calls the `'get_username()'` function (file: [functions.inc.php](Resources/flagshop/includes/functions.inc.php)). This last function (`get_username`) calls the function `'init()'` (file: [session.inc.php](Resources/flagshop/includes/session.inc.php)), where we can see that there is a loose comparison used together with the `'strcmp'` function  (`strcmp($ session_hmac, $ hmac )`).

The `'strcmp'` function returns `0` if two strings are equal, but if we pass a string and a non-string as parameters, the function will return a *false* statement and the result of `strcmp()` will be `0` (`'false' == 0` implies `'true'`).
We use this technique, called *array injection*, to overcome the `IF` statement (`if ( strcmp($session_hmac, $hmac) == 0 )`) by changing the field `'hmac'`, which is a *cookie*, by setting it to an array for the previous explained reasons.

After that the function will return, if all goes well, an array `$session` (used in the `'index.php'` page to understand if the username is `"admin"` or not). To make it return the correct `$session`, containing `"admin"`, and then get the *flag*, we just need to set the `"session"` cookie to the following value (we repeat the operations that are performed by the `'save()'` function, to do that you need a *PHP* compiler):

```php
$session =  base64_encode(serialize(new Session));
```

Where an admin `'Session'` is defined as follow:
```php
class Session {
	private $content = array('username' => 'admin');

	# …other stuff…
}
```

Once this is done, we are able to obtain the *flag*. So, to sum up the attack procedure consists of:
1. Create an account;
2. Log into the platform;
3. Open the browser's `'Inspect element'` tab and go to the `'storage'` section (cookies);
4. Modify the `'hmac'` cookie such that it becomes an array (just set the name to `hmac[]`) for the reasons explained above;
5. Recreate the `'$session'` variable as described above (using any *PHP* compiler);
6. Set the found value to the `"session"` cookie;
7. Reload the `'Index.php'` page and press `'redeem for free'`.

# Possible Fixes
To solve this problem we just need to modify the `'init'` function, at the point in which it uses the `'strcmp (...)'`, so that there is no loose comparison (use `===`) and perform a string-type conversion (casting) for the two parameters passed to the `'strcmp'` function.
