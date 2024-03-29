#!/usr/bin/python3
# Take in a URL, send a request to URL, and dispaly body
"""
@author :justus njogu
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
