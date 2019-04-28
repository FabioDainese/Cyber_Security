# Introduction
This challenge was designed to put into practice in a '*real*' world situation some *server-side web* attacks (7<sup>th</sup> December 2018).

# Challenge Description
This challenge consists to find sensitive information saved in a database that is also used in a [website](https://rmb.seclab.dais.unive.it/) (it is also provided the [source code](Resources/rmb)) that shows a list of musics. The backend part uses extensively prepared statements, so you can’t perform SQL injection attacks, except in one specific point (function `'_get_releases'` defined in the [app.py](Resources/rmb/app.py) file), i.e. when a query is generated in which you can make Blind SQL injection and retrieve the wanted information a 'bit' at a time (in which you compare if the result of the query is ordered in one way or another).

## Original Description
>**RollMyBeats** is a web application developed by *Lavish* to manage his records. The project is still in an early stage of development, indeed the backend does not make use of the whole database schema yet... more features will be implemented in the next release! Even if *RMB* is pre-alpha software, *Lavish* focused heavily on the security of the platform. He used prepared statements wherever possible, so there should be no place for injections this time.
>
>Prove that lavish is wrong by reading his private notes ;P

# Dependencies
The developed solution is based on *Python3*, so you'll need to have it installed in order to run it. To check if you have installed *Python3* in your computer, open a terminal window and type `python3 --version` or `which python3`. If the system has rised an error it means that you don't have installed it.

# Solution
The provided solution ([*attack.py*](attack.py) file - well commented) initially retrieve the names of the tables available in the database, then it finds the names of the columns (fields) of each table and finally it dumps the personal contents (**flag**).

To run the *attack* script you just need to open a terminal window, change directory to the which one where you have saved the file and type `python3 attack.py`.

# Possible Fixes
A possible solution to solve this vulnerability is to sanitize the data retrieved from the web page, perhaps comparing them with a white-list of values that are admissible (in this case all the various sorting possibilities).
Another method is to create `N` prepared statements as many as the methods of sorting and to recall, from time to time, the one that reflects the sort chosen by the user.