import config
import requests
from urllib.parse import parse_qsl
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import sys

def dispatch_request(payload):
    #==================================Initializing.....=======================
    
    #====================Cookie configuration====================
    if config.cookie:
        cookie = dict(parse_qsl(config.cookie))
    else:
        cookie = None
        
    #====================Header configuration====================
    if config.header:
        key, value = config.header.split(":", 1)
        head = {key.strip(): value.strip()}
    else:
        head = None
        
    #====================Proxy configuration====================
    if config.proxy:
        proxy = {
        "http": config.proxy,
        "https": config.proxy
        }
    else:
        proxy = None
        
    #==================================Initializied==============================
    final_payload = payload
    if config.method == "POST":
        value = post_request(payload=final_payload,cookie=cookie,header=head,proxy=proxy)
        return value
    if config.method == "GET":
        value = get_request(payload=final_payload,cookie=cookie,header=head,proxy=proxy)
        return value
    
#Post Request
def post_request(payload,cookie,header,proxy):
    info = dict(parse_qsl(config.data))
    info[config.vulnerable] = payload
    try:
        response = requests.post(
            url=config.url,
            data=info,
            verify=config.verify,
            proxies=proxy,
            timeout=config.timeout,
            cookies=cookie,
            headers=header
        )
        if config.failure_message not in response.text:
            return True
    except requests.RequestException:
        print(f"[!] Request Error. Check your internet connection and try again")
        sys.exit(1)
    except requests.exceptions.InvalidURL:
        print(f"[!] Invalid URL {config.url}. Provide a valid URL")
        sys.exit(1)
    except requests.exceptions.InvalidHeader:
        print(f"[!] Invalid Header {config.header}. Provide a valid Header")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"[!] Request Timeout. Consider increasing --timeout and try again")
        sys.exit(1)
    except requests.exceptions.InvalidProxyURL:
        print(f"[!] Proxy Error {proxy}. Consider providing a valid --proxy and try again")
        sys.exit(1)
    except requests.exceptions.SSLError:
        print(f"[!] SSL certificate Error. Consider using -k and try again")
        sys.exit(1)
    
#Get Request
def get_request(payload,cookie,header,proxy):
    parsed = urlparse(config.url)
    changed_url = dict(parse_qsl(parsed.query, keep_blank_values=True))
    changed_url[config.vulnerable] = payload
    original_url = urlunparse(parsed._replace(query=urlencode(changed_url)))
    try:
        response = requests.get(
            url=original_url,
            verify=config.verify,
            proxies=proxy,
            timeout=config.timeout,
            cookies=cookie,
            headers=header
        )
        if config.failure_message not in response.text:
            return True
    except requests.RequestException:
        print(f"[!] Request Error. Check your internet connection and try again")
        sys.exit(1)
    except requests.exceptions.InvalidURL:
        print(f"[!] Invalid URL {config.url}. Provide a valid URL")
        sys.exit(1)
    except requests.exceptions.InvalidHeader:
        print(f"[!] Invalid Header {config.header}. Provide a valid Header")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"[!] Request Timeout. Consider increasing --timeout and try again")
        sys.exit(1)
    except requests.exceptions.InvalidProxyURL:
        print(f"[!] Proxy Error {proxy}. Consider providing a valid --proxy and try again")
        sys.exit(1)
    except requests.exceptions.SSLError:
        print(f"[!] SSL certificate Error. Consider using -k and try again")
        sys.exit(1)
        
        