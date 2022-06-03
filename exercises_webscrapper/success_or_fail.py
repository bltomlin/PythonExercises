"""
Define a function check_success(url) that, given a URL, sends out a GET request and returns "Success" if it succeeds and "Fail" otherwise.
"""

import requests

def check_success(url):
    r = requests.get(url)
    if r:
        return 'Success'
    else:
        return 'Fail'