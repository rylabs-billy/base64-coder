#!/usr/bin/env python3
#
# base64 encode or decode a string 

import sys
import base64

usage = ("""
Usage: b64.py <string> -(e|d)

Example: b64.py 'This text' -e  # encode
         b64.py '0cmluZy4=' -d  # decode
        """)

# accepted arguments
arg_list = ['-e','-d']

# take input from command line
# print usage if user f'd up 
if len(sys.argv) == 3 and sys.argv[1] in arg_list:
    arg = sys.argv[1]
    string = sys.argv[2]
    try:
        # encode string
        if arg == arg_list[0]:
            encoded_bytes = base64.urlsafe_b64encode(string.encode('utf-8'))
            encoded_string = str(encoded_bytes, 'utf-8')
            print(f'\n{encoded_string}')
        # decode string
        elif arg == arg_list[1]:
            decoded_bytes = base64.urlsafe_b64decode(string)
            decoded_string = str(decoded_bytes, 'utf-8')
            print(f'\n{decoded_string}')
    except (base64.binascii.Error, UnicodeDecodeError):
        print('\nNothing to decode here dummy.')
else:
    print(usage)
