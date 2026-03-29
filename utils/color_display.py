"""
Professional colored output for VulnPhantom
"""

from colorama import init, Fore, Back, Style
import sys

# Initialize colorama
init(autoreset=True)

class PhantomDisplay:
    """Elite display handler with professional UI"""
    
    def __init__(self):
        self.banner_art = """
    ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗██████╗  ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
    ██║   ██║██║   ██║██║     ████╗  ██║██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
    ██║   ██║██║   ██║██║     ██╔██╗ ██║██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
    ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
     ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
      ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
    """
    
    def print_banner(self):
        """Display elite banner"""
        print(Fore.CYAN + self.banner_art)
        print(Fore.YELLOW + Style.BRIGHT + "╔════════════════════════════════════════════════════════════════════╗")
        print(Fore.YELLOW + Style.BRIGHT + "║                    Elite Web Vulnerability Scanner v2.0              ║")
        print(Fore.YELLOW + Style.BRIGHT + "║                         Author: The Phantom                         ║")
        print(Fore.YELLOW + Style.BRIGHT + "╚════════════════════════════════════════════════════════════════════╝")
        print()
    
    def print_scan_start(self, target_url: str):
        """Display scan start information"""
        print(Fore.WHITE + Style.BRIGHT + "\n[+] Initializing Phantom Scan Engine")
        print(Fore.WHITE + f"[+] Target: {target_url}")
        print(Fore.WHITE + "[+] Loading payload arsenal...")
        print(Fore.WHITE + "[+] Activating detection algorithms...")
        print(Fore.CYAN + "═" * 60 + "\n")
    
    def print_parameter_summary(self, param_count: int):
        """Display parameter analysis summary"""
        print(Fore.GREEN + Style.BRIGHT + f"[✓] Parameters detected: {param_count}")
        print(Fore.GREEN + "[✓] Starting vulnerability assessment...\n")
    
    def print_vulnerability_found(self, param: str, vuln_type: str, confidence: int, severity: str):
        """Display vulnerability findings with colors"""
        severity_color = {
            'CRITICAL': Fore.RED + Style.BRIGHT,
            'HIGH': Fore.RED,
            'MEDIUM': Fore.YELLOW,
            'LOW': Fore.BLUE
        }.get(severity, Fore.WHITE)
        
        print(severity_color + f"\n[!] VULNERABILITY DETECTED!")
        print(severity_color + f"    Parameter: {param}")
        print(severity_color + f"    Type: {vuln_type}")
        print(severity_color + f"    Confidence: {confidence}%")
        print(severity_color + f"    Severity: {severity}")
        print(Fore.WHITE + "─" * 40)
    
    def print_scan_complete(self, vuln_count: int):
        """Display scan completion summary"""
        print(Fore.CYAN + "\n" + "═" * 60)
        
        if vuln_count > 0:
            print(Fore.RED + Style.BRIGHT + f"\n[!] Scan Complete - {vuln_count} potential vulnerabilities identified")
        else:
            print(Fore.GREEN + Style.BRIGHT + "\n[✓] Scan Complete - No vulnerabilities detected")
        
        print(Fore.WHITE + "[✓] Report generated successfully")
    
    def print_error(self, message: str):
        """Display error message"""
        print(Fore.RED + f"\n[✗] ERROR: {message}")
    
    def print_success(self, message: str):
        """Display success message"""
        print(Fore.GREEN + f"\n[✓] {message}")
    
    def print_warning(self, message: str):
        """Display warning message"""
        print(Fore.YELLOW + f"\n[!] WARNING: {message}")
