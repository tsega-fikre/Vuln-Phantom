"""
Report Factory - Generates professional scan reports
"""

import json
from datetime import datetime
from typing import Dict

class ReportFactory:
    """Generate comprehensive scan reports"""
    
    def save_report(self, results: Dict, filename: str):
        """Save scan results to JSON file"""
        
        report = {
            'scan_summary': {
                'scan_id': results.get('scan_id', 'N/A'),
                'timestamp': results.get('timestamp', str(datetime.now())),
                'target': results.get('target', 'N/A'),
                'total_vulnerabilities': results.get('total_vulnerabilities', 0),
                'parameters_tested': results.get('parameters_tested', 0),
                'severity_breakdown': results.get('severity_breakdown', {})
            },
            'vulnerabilities': results.get('vulnerabilities', []),
            'metadata': {
                'scanner': 'VulnPhantom v2.0',
                'report_format': 'JSON',
                'generated_by': 'Phantom Security Framework'
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
