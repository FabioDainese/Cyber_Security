# Introduction
This challenge was designed to to put into practice the new learned things that involved *firewalls*, *access control* and *identification* (23<sup>th</sup> November 2018).

# Challenge Description
Giving the following network configuration:
<p align="center">
  <img src="Resources/Network Configuration.png" alt="Network Configuration">
</p>
Try to break into the system by firstly overcome the firewall and secondary gain unauthorized access in order to get the flag.

It is also provide the [`iptables configuration`](iptables-save) and a copy of [`OTPizza`](otp.py) source code.

## Original Description

>Rebels hide in a pizza delivery shop and use one firewall and a strange one-time credential called OTPizza to protect their servers.
>We found their network configuration and a copy of the OTPizza source code but we failed accessing the server.
>Please help us...

# Dependencies
The developed solution is based on *Python3*, so you'll need to have it installed in order to run it. To check if you have installed *Python3* in your computer, open a terminal window and type `python3 --version` or `which python3`. If the system has rised an error it means that you don't have installed it.

# Solution
To complete this challenge we initially look at the [*network configuration*](iptables-save), as we must need to connect to the `172.17.0.2` machine starting from being connected to the `10.0.0.0/16` network. 

Looking at that file we can find (in this specific rule `10.0.241.57 -i tap0 -p tcp -m tcp --sport 21337: 21437 --dport 54317 -j DNAT --to-destination 172.17.0.2:21337`) all the data necessary to carry out our desired connection. Basically we just need to connect to the firewall (`10.0.241.57`) using one of the `100` available ports (`21337:21437`) specifying also the destination port (`54317`). To achieve that we are going to use `netcat`, so we need to open a terminal window and type `nc -v 10.0.241.57 54317 -p 21400` (in this case we have chosen to connect to the port `21400`).
Once we are connected to the service the program will ask us to insert a key (**OTP**: *One Time Password*) which it will be compared with the one calculated by the `otp` function (used in the [`otp.py`](otp.py) file) and if there are equal the program will return the *FLAG*.

The *OTP* calculation is performed through a loop in which at each iteration a character is generated that it will be part of the final OTP. This calculation is based on a cascade chain of **SHA256** (*SHA256* is a one-way function that generates always the same output given the same input), which means that the output of each loop becomes the input of the next one, in which only the first symbol/Byte of the encryption function output is used to generate the OTP's new character. So to reconstruct the original OTP and get the *flag* we just need to find the first character used and then apply the same procedure available in the file [`'otp.py'`](otp.py). 

To find the initial character we use a brute-force approach in which at each iteration we generate a new *OTP* and test it if it's the right one by sending it as input to the service. If the output/response is `'Wrong OTP sorry'` we continue this brute-forcing process.

To run the provided solution (file [`attack.py`](attack.py) - well commented) you just need to open a terminal window, change directory to the which one where you have saved the file and type `python3 attack.py`.

# Possible Fixes
A possible solution is to modify the `'otp'` function such that it uses all the hashed string at every iteration instead of a single character and maybe use it in conjuction with a slowed hash function in order to prevent the brute-forcing (making it slow in such a way that you can try only a few combinations per second - *SHA-rounds*).
Another solution involves to adjust the firewall rules, if you do not want external access from the `10.0.0.0` network, by configure it such that it drops all the input connections from that particular network.
