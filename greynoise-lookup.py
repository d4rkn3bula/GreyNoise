#!/usr/bin/python3

import requests
import json
import argparse
import re
from pprint import pprint

def get_args():
    parser = argparse.ArgumentParser(prog="GreyNoise Community API Lookup")
    parser.add_argument("-i", "--ipaddress", help="Input IPv4 address you'd like to query")
    args = parser.parse_args()
    return args

def ip_check(ip):

    ip_re = re.compile(
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    if ip_re.match(ip):
        return ip
    else:
        print(f"\nprocess killed, {ip} is not an ip address")
        exit()

def api_request(ip_rep):
    url = "https://api.greynoise.io/v3/community/"
    response = requests.get(url + ip_rep)
    print(response)
    result = json.loads(response.text)
    pprint(result)

def main():
    args = get_args()
    ip_rep = args.ipaddress

    if args.ipaddress:
        ip_check(ip_rep)
        api_request(ip_rep)
    else:
        print("Not valid, please try another request")

if __name__ == "__main__":
    main()

