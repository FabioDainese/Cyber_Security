#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import string
import hashlib

def otp(key,timestamp,charset,size):
        otp = ''

        h = hashlib.sha256((key+timestamp).encode()).digest()

        for i in range(size):
                # picks a letter from charset at "random" based on the hash h bytes: works well if charset size is a power of two smaller than 256. In our case it is 64 so we are happy.
                assert len(charset) == 64
                index = h[0] % len(charset)
                otp += charset[index]

                # We could have used the next hash byte but we prefer to recompute the hash and make it dependent from the round i, so to strengthen security!!
                h = hashlib.sha256( bytes(h[0]) + (str(i)).encode() ).digest()

        return otp

def main():
        charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%$"

        wdir = os.path.dirname(os.path.realpath(__file__))
        # reads the secret key
        with open(os.path.join(wdir, 'key'), 'r') as f:
                key=f.read()
        with open(os.path.join(wdir, 'flag'),'r') as f:
                flag=f.read()

        # timestamp changes every 30 seconds to allow for syncronization
        timestamp = str(int(time.time()) // 30)

        user_otp = input("Insert your OTP: ")
        system_otp = otp(key,timestamp,charset,16)

        if (user_otp == system_otp):
                print('Authenticated! here is your flag: {}'.format(flag))
        else:
                print('Wrong OTP sorry ...')

if __name__ == '__main__':
        main()

