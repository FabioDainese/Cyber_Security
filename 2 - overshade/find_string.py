#!/usr/bin/env python3
import hashlib
import itertools
import sys

#Characters (charset) used to form the various passwords
generator_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()[]{\}|/,.;!-"

#Create passwords ranging from 4 to 10 characters long (I've chose to start from 4 since those with less characters, using this alphabet/charset, they will not generate the desired string)
for count in range(4,10):
    #Generating the Cartesian product among all the characters of our alphabet and iterating through the various elements (strings of length 'count')
    for item in itertools.product(generator_alphabet, repeat=count):
        tmp_str = "".join(item)
        #Generating the encrypted version of the string
        tmp_sha256_str = hashlib.sha256(tmp_str.encode('utf-8')).hexdigest()
        #If the last 3 hexadecimal characters correspond to the desired ones, it prints out both the string and its corresponding encrypted version with '\x' at the beginning and after every 2 characters
        if(tmp_sha256_str[-6:] == "00ae88"):
            print(tmp_str)
            print('{0}{1}'.format('\\x','\\x'.join(tmp_sha256_str[i:i+2] for i in range(0, len(tmp_sha256_str), 2))))
            sys.exit(0)