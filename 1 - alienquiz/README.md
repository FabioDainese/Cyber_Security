# Introduction
This challenge was designed to familiarize with *Python* (5<sup>th</sup> October 2018).

# Challenge Description
Write a python script which interacts with *alienquiz* and beats all the levels by answering correctly to the questions! Once you'll have successfully completed it you'll be rewarded with a *FLAG* to submit to the checker system.

* [alienquiz (linux32)](Resources/alienquiz-32) (e16880e8b68f5a5dd9cfe081cf128326eaf623f6a3cb905e7442c7b6b2636647 sha256sum)
* [alienquiz (linux64)](Resources/alienquiz-32) (2b9684c88c85f97eb4c4f684cbd07438efa0eae812bf93c1ce593d4df7c04ff6 sha256sum)

# Dependencies
The *alienquiz* program is runnable only on GNU/Linux OS.

The developed solution is based on *Python3*, so you'll need to have it installed in order to run it. To check if you have installed *Python3* in your computer, open a terminal window and type `python3 --version` or `which python3`. If the system has rised an error it means that you don't have installed it.

# Solution
To run the provided solution (file [*auto_alienquiz.py*](auto_alienquiz.py) - well commented) you just need to open a terminal window, change directory to the which one where you have saved the file and type `python3 auto_alienquiz.py`.

**N.B.** If you have changed the location of the *alienquiz* program you'll also need to update it as well into the *auto_alienquiz.py* file at the line: 
```python
...
process = subprocess.Popen("<new_location_>/./alienquiz-32",stdin=subprocess.PIPE,stdout=subprocess.PIPE)
...
```
