# Introduction
This challenge was designed to get used to the *GDB* debugger and to put into practice the *stack overflow* and *format string* attacks (9<sup>th</sup> November 2018).

# Challenge Description
Write a *script* such that interact with the [starcalc](starcalc) program and gain unauthorized access to get the *FLAG*. 

Analyzing the source code ([starcalc.c](starcalc.c) file) we can notice two precise points where there are vulnerabilities. The first one is in the function `'calc'` when the `printf(name)` is made. In this case there's no specified string format (format directives). Meanwhile, the second one is in the function `'unlock_db'` in the section where it reads the input from the *STDIN* without specifying a maximum length (stack overflow attack).

Exploiting these vulnerabilities, we can initially retrieve the *canary* and then reuse it when we are going to overwrite the buffer (without causing stack smashing) with the address of the `'dumpdb'` function (return address) in order to get the flag.

P.S. Obviously the `stars.cvs` file wasn't readable for our system user, so I couldn't simply dump the content.

## Original Description

>Ever wondered about the mass of the stars in the sky?
>
>Well, you should! Many spacecrafts have been sucked into the gravity of giant stars after a hyperspace jump! For your safety, step inside the **STARCALC** program and leak the database of the most massive known stars!
>
>Do you have what it takes to exploit **starcalc**?

# Dependencies
The developed solution is based on *Python3*, so you'll need to have it installed in order to run it. To check if you have installed *Python3* in your computer, open a terminal window and type `python3 --version` or `which python3`. If the system has rised an error it means that you don't have installed it.

# Solution
To run the provided solution (file [auto_starcalc.py](auto_starcalc.py) - well commented) you just need to open a terminal window, change directory to the which one where you have saved the file and type `python3 auto_starcalc.py`.

The developed solution first retrieves the *canary* (since the *starcal* program was compiled with stack protector enabled) and then replaces the return address with the one of the `dumpdb(...)` function in order to get the *flag*. An important thing to point out is that the program contained the canary at a fixed offset (process data area).

For more implementative details/explanations look at the [*auto_starcalc.py*](auto_starcalc.py) file comments.

**N.B.** If you have changed the location of the *starcalc* program you'll also need to update it as well into the *auto_starcalc.py* file at the line:

```python
...
p = subprocess.Popen('<new_location>/./starcalc', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
...
```

# Possible Fixes
A possible solution, in this specific case, is to specify a format directive in the `printf` used inside the `unlock_db` function (in order to prevent dumping the stack and therefore retrieve the canary) and to fix the reading part present in the `unlock_db` function specifying to reading maximum 31 characters (leaving also space for the `'\0'` byte).
