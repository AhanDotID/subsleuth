#!/usr/bin/env python3
# ================================================
#  SubSleuth - Simple Subdomain Finder
#  by Ahan Pahlevi | CianjurSec
# ================================================

import socket
import sys
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ── Colors ──
class C:
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    DIM    = '\033[2m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

BANNER = f"""
{C.GREEN}
  ██████ ██    ██ ██████  ███████ ██      ███████ ██    ██ ████████ ██   ██
 ██      ██    ██ ██   ██ ██      ██      ██      ██    ██    ██    ██   ██
  █████  ██    ██ ██████  ███████ ██      █████   ██    ██    ██    ███████
      ██ ██    ██ ██   ██      ██ ██      ██      ██    ██    ██    ██   ██
 ██████   ██████  ██████  ███████ ███████ ███████  ██████     ██    ██   ██
{C.RESET}
{C.DIM}         Simple Subdomain Finder | by Ahan Pahlevi | CianjurSec{C.RESET}
"""

# ── Default wordlist ──
DEFAULT_WORDLIST = [
    "www", "mail", "ftp", "smtp", "pop", "imap", "webmail",
    "admin", "administrator", "cpanel", "whm", "plesk",
    "api", "api2", "v1", "v2", "v3", "dev", "development",
    "staging", "stage", "test", "testing", "uat", "qa",
    "beta", "alpha", "demo", "sandbox",
    "blog", "forum", "shop", "store", "portal",
    "cdn", "static", "assets", "media", "img", "images",
    "vpn", "remote", "ssh", "rdp", "sftp",
    "db", "database", "mysql", "redis", "mongo",
    "git", "gitlab", "github", "bitbucket", "jenkins", "ci", "cd",
    "app", "apps", "mobile", "m",
    "secure", "ssl", "login", "auth", "sso", "oauth",
    "support", "help", "helpdesk", "ticket", "status",
    "docs", "documentation", "wiki", "kb",
    "ns1", "ns2", "ns3", "dns", "dns1", "dns2",
    "mx", "mx1", "mx2", "relay", "smtp2",
    "backup", "bak", "old", "new",
    "internal", "intranet", "corp", "office",
    "monitor", "monitoring", "nagios", "grafana", "kibana",
    "panel", "dashboard", "manage", "management", "control",
    "cloud", "aws", "azure", "gcp",
    "proxy", "gateway", "lb", "load", "waf",
    "id", "my", "account", "user", "users", "profile",
    "payment", "pay", "billing", "invoice",
    "crm", "erp", "hr", "jira", "confluence",
]

found_subdomains = []

def resolve(subdomain, domain, timeout=2):
    target = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        return (target, ip)
    except socket.gaierror:
        return None

def scan(domain, wordlist, threads, output_file=None, verbose=False):
    print(f"\n{C.CYAN}[*] Target  : {C.BOLD}{domain}{C.RESET}")
    print(f"{C.CYAN}[*] Words   : {C.BOLD}{len(wordlist)}{C.RESET}")
    print(f"{C.CYAN}[*] Threads : {C.BOLD}{threads}{C.RESET}")
    print(f"{C.CYAN}[*] Started : {C.BOLD}{datetime.now().strftime('%H:%M:%S')}{C.RESET}\n")
    print(f"{C.DIM}{'─' * 55}{C.RESET}")

    start = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(resolve, word, domain): word for word in wordlist}
        for future in as_completed(futures):
            result = future.result()
            if result:
                subdomain, ip = result
                found_subdomains.append((subdomain, ip))
                print(f"  {C.GREEN}[+]{C.RESET} {C.BOLD}{subdomain:<40}{C.RESET} {C.DIM}→{C.RESET} {C.CYAN}{ip}{C.RESET}")
            elif verbose:
                word = futures[future]
                print(f"  {C.DIM}[-] {word}.{domain}{C.RESET}")

    elapsed = time.time() - start
    print(f"\n{C.DIM}{'─' * 55}{C.RESET}")
    print(f"\n{C.GREEN}[✔] Found   : {C.BOLD}{len(found_subdomains)} subdomain(s){C.RESET}")
    print(f"{C.CYAN}[*] Time    : {C.BOLD}{elapsed:.2f}s{C.RESET}\n")

    if found_subdomains:
        print(f"{C.YELLOW}{'─' * 55}")
        print(f"  RESULTS")
        print(f"{'─' * 55}{C.RESET}")
        for sub, ip in sorted(found_subdomains):
            print(f"  {sub} → {ip}")
        print()

    if output_file:
        save(output_file)

def save(path):
    with open(path, 'w') as f:
        f.write(f"# SubSleuth Results\n")
        f.write(f"# Generated: {datetime.now()}\n\n")
        for sub, ip in sorted(found_subdomains):
            f.write(f"{sub} → {ip}\n")
    print(f"{C.GREEN}[✔] Saved to: {path}{C.RESET}\n")

def load_wordlist(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"{C.RED}[!] Wordlist not found: {path}{C.RESET}")
        sys.exit(1)

def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description='SubSleuth - Simple Subdomain Finder by Ahan Pahlevi',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('domain',
        help='Target domain (e.g. example.com)')
    parser.add_argument('-w', '--wordlist',
        help='Custom wordlist file (default: built-in list)',
        default=None)
    parser.add_argument('-t', '--threads',
        help='Number of threads (default: 50)',
        type=int, default=50)
    parser.add_argument('-o', '--output',
        help='Save results to file (e.g. results.txt)',
        default=None)
    parser.add_argument('-v', '--verbose',
        help='Show all attempts including failed ones',
        action='store_true')

    args = parser.parse_args()

    # Clean domain input
    domain = args.domain.replace('http://', '').replace('https://', '').rstrip('/')

    # Load wordlist
    if args.wordlist:
        wordlist = load_wordlist(args.wordlist)
        print(f"{C.CYAN}[*] Using custom wordlist: {args.wordlist}{C.RESET}")
    else:
        wordlist = DEFAULT_WORDLIST
        print(f"{C.CYAN}[*] Using built-in wordlist ({len(DEFAULT_WORDLIST)} words){C.RESET}")

    try:
        scan(domain, wordlist, args.threads, args.output, args.verbose)
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}[!] Interrupted by user{C.RESET}")
        if found_subdomains:
            print(f"{C.GREEN}[✔] Found so far: {len(found_subdomains)} subdomain(s){C.RESET}")
            if args.output:
                save(args.output)
        sys.exit(0)

if __name__ == '__main__':
    main()
