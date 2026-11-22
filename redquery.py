#!/usr/bin/env python3

from urllib.parse import urlparse
import argparse
import config
import banner
import sub_main
import sys

parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
parser.add_argument("-u", "--url", required=True, help="Specify the target URL")
parser.add_argument("-m", "--fail_message", help="Specify the error message returned for failed requests", required=True)

# Optional Arguments
parser.add_argument("-o", "--filename", nargs="?",const="Redquery.txt", help="Specify the output filename. Defaults to Redquery.txt", default=None)
parser.add_argument("--data", help="Specify the POST request data", default=None)
parser.add_argument("--param", help="Specify the vulnerable parameter in the POST data", default=None)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("-k", "--verify", action="store_true", help="Disable SSL certificate verification")
parser.add_argument("--cookie", help="Specify HTTP cookies", default=None)
parser.add_argument("--header", help="Specify custom HTTP headers", default=None)
parser.add_argument("--resume", action="store_true", help="Resume a supported enumeration stage")
parser.add_argument("--context", help="Specify the injection context: str/int. Defaults to str", default="str",choices=["str", "int"])
parser.add_argument("--condition", help="Specify the injection condition: AND/OR. Defaults to OR", default="OR",choices=["OR","AND"])
parser.add_argument("--proxy", help="Specify a proxy URL, such as Burp Suite, for debugging and request interception", default=None)
parser.add_argument("--valid", help="Specify the valid entry for AND-based injection", default=None)
parser.add_argument("--timeout", help="Specify the request timeout in seconds. Defaults to 4 seconds", default=4, type=int)
parser.add_argument("--method", help="Specify the HTTP request method. Defaults to POST", default="POST")
parser.add_argument("--enum", help="Specify the enumeration stage to resume. Defaults to table", default="table", choices=["table", "column", "row", "password"])
args = parser.parse_args()
parse_url = urlparse(args.url)

if parse_url.scheme not in ("http", "https") or not parse_url.netloc:
    print("Invalid URL provided")  
    sys.exit(1)     
if args.proxy is not None:
    parse_proxy = urlparse(args.proxy)
    if parse_proxy.scheme not in ("http", "https") or not parse_proxy.netloc:
        print("Invalid URL provided")
        sys.exit(1)
        
print("[!] Initializing Configurations...")
config.url = args.url
config.condition = args.condition
config.filename = args.filename
config.context = args.context
config.verbose = args.verbose
config.resume = args.resume
config.verify = args.verify
config.failure_message = args.fail_message
config.header = args.header
config.cookie = args.cookie
config.data = args.data
config.vulnerable = args.param
config.valid_entry = args.valid
config.proxy = args.proxy
config.method = args.method
config.enum = args.enum
config.timeout = args.timeout
print("[!] Configuration Initialized.\n")

#Calling the main check function
sub_main.sub_mainer()



