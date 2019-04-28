#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import string
import hashlib
import subprocess
import re
import sys

#Charset used to compose the original OTP (present on the 'opt.py' file)
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%$"
#Regex used to interrupt the searching loop as soon as the flag is found
re = re.compile('Authenticated!')

#Brute-forcing loop udes to find the correct initial Byte/character (h[0] = range from 0 to 255)
for h_index in range(256):
    #Support string used to save the calculated 'otp'
    otp = ''
    h = [h_index]

    #Performing the same procedure used in the source code (otp.py) to recreate the OTP key
    for i in range(16):
        assert len(charset) == 64

        index = h[0] % len(charset)
        otp += charset[index]

        h = hashlib.sha256( bytes(h[0]) + (str(i)).encode('utf-8') ).digest()

    #Through 'subprocess' the program write on the STDIN (shell) the calculated OTP and putting it in pipe with the command 'netcat', which allows it to connect to the service. The 'getoutput' method is used to capture the output (shell) and return it as a string. The 'sleep' prevents the echo utility to close the pipe to early and terminate the connection (error 'bind failed')
    output = subprocess.getoutput('(echo '+ otp +'; sleep 0.15) | nc -v 10.0.241.57 54317 -p 21390')

    #If the output contains the word 'Authenticated' it means that we have found the flag, so we print it and interrupt the searching loop
    if re.search(output):
        print("Correct OTP = ",otp)
        print("Output = ",output)
        sys.exit(0)