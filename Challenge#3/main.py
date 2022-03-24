#!/usr/bin/env python

import argparse
import urllib.request

# define and parse command-line options
parser = argparse.ArgumentParser(description='Get AWS Instnace Metadata')
parser.add_argument('--key', required=False, help='Keyname to get the Value')
args = vars(parser.parse_args())

url = 'http://169.254.169.254/latest/meta-data'
keyname = args['key']
metadata_keys = urllib.request.urlopen(url).read().decode()
json_hash = {}


if keyname:
    url = "{}/{}".format(url, keyname)
    response = urllib.request.urlopen(url).read().decode()
    json_hash[keyname] = response
    print(json_hash)
else:
    for keyname in metadata_keys.split("\n"):
        response = urllib.request.urlopen(url).read().decode()
        json_hash[keyname] = response
        print(json_hash)
