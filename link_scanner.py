import requests
import re
from urllib.parse import urlparse
import ssl
import socket
import whois
from datetime import datetime

phishing_domains = ['examplephish.com', 'malicioussite.xyz', 'fakebank.com']

def check_https(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme == 'https'

def check_phishing_domain(url):
    domain = urlparse(url).hostname
    return domain in phishing_domains

def check_ssl_certificate(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.connect((hostname, 443))
        conn.getpeercert()
        conn.close()
        return True
    except:
        return False

def check_whois_info(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
        w = whois.whois(domain)
        creation_date = w.creation_date if isinstance(w.creation_date, datetime) else None
        if creation_date and (datetime.now() - creation_date).days < 30:
            return True
        return False
    except:
        return False

def detect_suspicious_patterns(url):
    patterns = [
        r'\.xyz$', r'\.top$', r'\.tk$',
        r'login', r'password', r'account',
        r'bank', r'verify', r'security'
    ]
    return any(re.search(pattern, url) for pattern in patterns)

def scan_url(url):
    print(f"Scanning URL: {url}")
    if not check_https(url):
        print(f"Warning: Insecure URL: {url}")
        return
    if check_phishing_domain(url):
        print(f"Warning: Phishing domain detected: {url}")
        return
    if not check_ssl_certificate(url):
        print(f"Warning: Invalid SSL certificate: {url}")
        return
    if check_whois_info(url):
        print(f"Warning: Domain recently registered: {url}")
        return
    if detect_suspicious_patterns(url):
        print(f"Warning: Suspicious URL patterns detected: {url}")
        return
    print(f"URL seems safe: {url}")

urls = [
    "https://www.examplephish.com",
    "https://www.google.com",
    "http://malicioussite.xyz",
    "https://secure-bank-login.com",
    "https://newphishing.xyz/login"
]

for url in urls:
    scan_url(url)
