#!/usr/bin/env python3
"""
VulnPhantom - Elite Web Vulnerability Scanner
"""

import sys
import argparse
import time
from urllib.parse import urlparse

# Add the current directory to path
sys.path.insert(0, '.')

from core.phantom_engine import VulnPhantomEngine
from utils.report_factory import ReportFactory
from utils.color_display import PhantomDisplay

def validate_url(url: str) -> bool:
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def main():
    display = PhantomDisplay()
    display.print_banner()
    
    parser = argparse.ArgumentParser(
        description='VulnPhantom - Elite Web Vulnerability Scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-t', '--threads', type=int, default=2, help='Number of threads')
    parser.add_argument('-o', '--output', help='Output report file')
    parser.add_argument('--stealth', action='store_true', help='Enable stealth mode')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Validate URL
    if not validate_url(args.url):
        display.print_error("Invalid URL format. Use http:// or https://")
        sys.exit(1)
    
    # Configuration
    config = {
        'threads': max(1, min(args.threads, 10)),  # Limit threads
        'timeout': args.timeout,
        'stealth_mode': args.stealth,
        'verbose': args.verbose
    }
    
    try:
        # Initialize and run scan
        engine = VulnPhantomEngine(args.url, config)
        results = engine.run_elite_scan()
        
        # Save report if requested
        if args.output:
            report_factory = ReportFactory()
            report_factory.save_report(results, args.output)
            display.print_success(f"Report saved to: {args.output}")
        
        # Exit with appropriate code
        if results.get('total_vulnerabilities', 0) > 0:
            sys.exit(1)
        else:
            sys.exit(0)
            
    except KeyboardInterrupt:
        display.print_warning("\nScan interrupted by user")
        sys.exit(130)
    except Exception as e:
        display.print_error(f"Scan failed: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
