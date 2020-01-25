#!/usr/bin/env python3
#
# base64 encode or decode a string 
#
# take input from command line
# print usage if syntax is invalid

import sys
import base64

def encode(s):
    """encodes a string"""
    encoded_bytes = base64.urlsafe_b64encode(s.encode('utf-8'))
    encoded_string = str(encoded_bytes, 'utf-8')
    print(f'\n{encoded_string}')

def decode(s):
    """decodes a binary string"""
    decoded_bytes = base64.urlsafe_b64decode(s)
    decoded_string = str(decoded_bytes, 'utf-8')
    print(f'\n{decoded_string}')

def main():
    usage = ("""
            Usage: b64.py -(e|d) <string>

            Example: b64.py -e 'This text' # encode
                     b64.py -d '0cmluZy4=' # decode
            """)

    if len(sys.argv) == 3 and sys.argv[1] in ('-e', '-d'):
        option = sys.argv[1]
        string = sys.argv[2]
        try:
            if option == '-e':
                encode(string)
            elif option == '-d':
                decode(string)
        except (base64.binascii.Error, UnicodeDecodeError):
            print('\nUse -e to encode the string.')
    else:
        print(usage)
# main
main()

