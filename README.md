# 🔍 Web Vulnerability Scanner

```markdown
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗██████╗  ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██║   ██║██║   ██║██║     ████╗  ██║██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██║   ██║██║   ██║██║     ██╔██╗ ██║██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝


╔════════════════════════════════════════════════════════════════════╗
║                    Elite Web Vulnerability Scanner v2.0                  ║
║                         Author: The Phantom                              ║
╚════════════════════════════════════════════════════════════════════╝

```

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security](https://img.shields.io/badge/security-educational-orange.svg)]()

A lightweight, educational web vulnerability scanner that detects common web application vulnerabilities including XSS, SQL Injection, Path Traversal, and Command Injection.

##  Ethical Disclaimer

**This tool is for EDUCATIONAL PURPOSES ONLY.** 
- Only use on systems you own or have explicit permission to test
- Unauthorized scanning may be illegal in your jurisdiction
- The author assumes no liability for misuse

##  Features

-  **XSS Detection** - Reflected cross-site scripting
-  **SQL Injection** - Error-based and time-based detection
-  **Path Traversal** - Directory traversal attempts
-  **Command Injection** - OS command injection testing
-  **Parameter Extraction** - Automatic URL parameter parsing
-  **Smart Detection** - Confidence scoring to reduce false positives
-  **Report Generation** - JSON/Text output for documentation

##  Quick Start

### Installation

```bash
git clone https://github.com/yourusername/web-vuln-scanner.git
cd vuln-phantom
pip install -r requirements.txt
# if only pip is not woking us the below command but first uncomment it
pip install --break-system-packages -r requirements.txt
python3 vulnphantom.py
```
