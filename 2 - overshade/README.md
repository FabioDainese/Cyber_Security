# Introduction
This challenge was designed to familiarize with the *GDB* debugger and to put into practice the *buffer/stack overflow* attacks (19<sup>th</sup> October 2018).

# Challenge Description
Write a *payload/script* such that interact with the [overshade](overshade) program (you can also view the relative source code in the [overshade.c](overshade.c) file) and gain unathorized access to get the *FLAG*. The developed/expected way to obtain access to the flag is to enter a password equals to the one saved and encrypted (SHA256) in an array. We will get the flag, without obviously knowing the correct password, using the '*stack overflow*' attack.

We are able to use this attack/technique since both the real password and the entered one (both are strings, so basically they are arrays of characters <- contiguously saved in the memory) are saved into the stack, so we can overwrite this data with other ad hoc information such that they respect all the conditions imposed by the program and so get the *flag*.

There is one more thing and that it is since the *scanf* function used in the program read maximum 49 characters as input, we are not able to overwrite entirely the arrays, that's because the `password` (20 characters) and `correcr_hash` (32 characters) arrays are in total 52 character-long, so we won't be able to change the last 3 characters of the hashed password (actually they will be only the last 2, since the *scanf* will add the end-of-line character `\x00` automatically).

To solve this problem we will use a brute forcing technique, which consists to execute a Python script that will generate strings until it finds one in which the last 3 hashed characters (sha256) will be equal to `'00ae88'` (*00*: end character string; *ae88*: non-overwritable characters - to remind that it is in *little endianness* order). Once this string is found we could execute the '*overshade*' program by first entering the plain text version of the string found + filling characters up to 20 + hased version of the string.

P.S. Obviously the `*flag*` file wasn't readable for our system user, so I couldn't dump the content.

# Dependencies
The developed solution is based on *Python3*, so you'll need to have it installed in order to run it. To check if you have installed *Python3* in your computer, open a terminal window and type `python3 --version` or `which python3`. If the system has rised an error it means that you don't have installed it.

# Solution
To find the right input string, as described in the previous sections, you just need to execute the [*find_string.py*](find_string.py) file (well commented). In order to do that you just simply need to open a terminal window, change directory to the which one where you have the file and type `python3 find_string.py`, this will finds and prints out a string and its corresponding hashed version that ends with `'00ae88'`.

An example of output is: `XzW/` (string found) and `\x0f\x9c\x7b\x7e\x86\xdb\xd2\xec\xa9\xf3\x29\x5a\x18\x29\xae\x45\x2b\x6c\x27\xaa\x71\x58\xc1\x5a\xde\x68\x50\x59\x2c\x00\xae\x88` (hashed version)

Now we have all the pieces to run our attack. So, we open a terminal window and type the following payload to get the *FLAG*:

```
python3 -c "import sys;sys.stdout.buffer.write(b'XzW/\0'+b'A'*15+b'\x0f\x9c\x7b\x7e\x86\xdb\xd2\xec\xa9\xf3\x29\x5a\x18\x29\xae\x45\x2b\x6c\x27\xaa\x71\x58\xc1\x5a\xde\x68\x50\x59\x2c')" | ./overshade
```

Basically, we have filled the `password` array (20 characters) with `XzW/\0` (`\0`: end-of-string, counted as a single character) and other 15 random characters, in this case `A`s, and overwriting the content of the `correcr_hash` array with the hashed version of the string found (to remark the fact that we haven't included `\x00\xae\x88` into the payload since it's useless).

# Possible Fixes
A possible solution, in this specific case, is to set the characters read by the *scanf* function up to 19 (19 + end-of-string character), so the user cannot perform the stack overflow, since it will only be able to fill the `password` array. Another one is to set the `PWDBUFFER` constant to `50`. 