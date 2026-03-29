"""
Advanced detection engine with AI-like pattern recognition
"""

import re
import hashlib
from typing import Dict, List, Tuple

class DetectionEngine:
    """Intelligent vulnerability detection with confidence scoring"""
    
    def __init__(self):
        self.signature_database = self._load_signatures()
        
    def _load_signatures(self) -> Dict:
        """Load comprehensive vulnerability signatures"""
        return {
            'xss': {
                'patterns': [
                    r'<script[^>]*>.*?</script>',
                    r'on\w+\s*=',
                    r'javascript:',
                    r'alert\s*\(',
                    r'prompt\s*\(',
                    r'confirm\s*\(',
                    r'document\.\w+',
                    r'window\.\w+',
                    r'eval\s*\(',
                    r'innerHTML',
                    r'outerHTML'
                ],
                'severity': 'HIGH',
                'weight': 1.0
            },
            'sqli': {
                'patterns': [
                    r'SQL syntax.*MySQL',
                    r'Warning.*mysql_.*',
                    r'ORA-[0-9]{5}',
                    r'PostgreSQL.*ERROR',
                    r'Unclosed quotation mark',
                    r'Microsoft.*ODBC.*SQL Server',
                    r'SQLite.*Exception',
                    r'You have an error in your SQL syntax',
                    r'Division by zero in SQL',
                    r'Unknown column'
                ],
                'severity': 'CRITICAL',
                'weight': 1.5
            },
            'lfi': {
                'patterns': [
                    r'root:.*:0:0:',
                    r'\[boot loader\]',
                    r'\[extensions\]',
                    r'etc/passwd',
                    r'Windows Registry Editor',
                    r'<?php',
                    r'#include',
                    r'Microsoft Windows'
                ],
                'severity': 'HIGH',
                'weight': 1.0
            },
            'cmd_injection': {
                'patterns': [
                    r'uid=\d+\([^)]+\)',
                    r'gid=\d+\([^)]+\)',
                    r'Directory of',
                    r'Volume in drive',
                    r'[0-9]+ files?',
                    r'root:x:\d+:\d+',
                    r'\[\.\.\]'
                ],
                'severity': 'CRITICAL',
                'weight': 1.5
            }
        }
    
    def analyze_response(self, response: Dict, payload: str, vuln_type: str,
                        baseline_length: int, response_time: float, 
                        original_value: str) -> Dict:
        """
        Comprehensive response analysis with multiple detection methods
        """
        if response.get('status_code') != 200:
            return {'is_vulnerable': False}
        
        response_text = response.get('text', '')
        confidence = 0
        evidence = []
        
        # Method 1: Direct reflection detection
        if payload in response_text:
            confidence += 40
            evidence.append(f"Direct payload reflection: {payload[:50]}")
        
        # Method 2: Signature pattern matching
        signatures = self.signature_database.get(vuln_type, {}).get('patterns', [])
        for pattern in signatures:
            if re.search(pattern, response_text, re.IGNORECASE | re.MULTILINE):
                confidence += 20
                evidence.append(f"Signature matched: {pattern[:50]}")
        
        # Method 3: Content length analysis (for boolean-based detection)
        current_length = len(response_text)
        length_diff = abs(current_length - baseline_length)
        if length_diff > 100:  # Significant content change
            confidence += 15
            evidence.append(f"Content length changed by {length_diff} bytes")
        
        # Method 4: Time-based detection
        if response_time > 2.0:  # Unusual delay
            confidence += 10
            evidence.append(f"Time anomaly: {response_time:.2f}s")
        
        # Method 5: Error message detection
        error_keywords = ['error', 'exception', 'warning', 'fatal', 'syntax']
        for keyword in error_keywords:
            if keyword in response_text.lower():
                confidence += 5
                evidence.append(f"Error keyword: {keyword}")
                break
        
        # Determine vulnerability
        is_vulnerable = confidence >= 50
        
        if is_vulnerable:
            severity = self._calculate_severity(confidence, vuln_type)
            return {
                'is_vulnerable': True,
                'type': vuln_type.upper(),
                'confidence': min(confidence, 100),
                'severity': severity,
                'evidence': evidence[:5],  # Top 5 evidence items
                'response_length': current_length,
                'response_time': response_time
            }
        
        return {'is_vulnerable': False}
    
    def _calculate_severity(self, confidence: int, vuln_type: str) -> str:
        """
        Calculate severity based on confidence and vulnerability type
        """
        base_severity = self.signature_database.get(vuln_type, {}).get('severity', 'MEDIUM')
        
        if confidence >= 80:
            return base_severity
        elif confidence >= 60:
            return 'HIGH' if base_severity == 'CRITICAL' else 'MEDIUM'
        else:
            return 'MEDIUM'
    
    def detect_boolean_sqli(self, true_response: Dict, false_response: Dict) -> Dict:
        """
        Advanced boolean-based SQL injection detection
        """
        if not true_response or not false_response:
            return {'is_vulnerable': False}
        
        true_length = len(true_response.get('text', ''))
        false_length = len(false_response.get('text', ''))
        
        # Significant difference indicates boolean-based injection
        length_ratio = abs(true_length - false_length) / max(true_length, false_length)
        
        if length_ratio > 0.3:  # More than 30% difference
            return {
                'is_vulnerable': True,
                'type': 'SQLI_BOOLEAN',
                'confidence': 85,
                'severity': 'HIGH',
                'evidence': [
                    f"Content difference: {length_ratio*100:.1f}% variation",
                    "Boolean logic manipulation successful"
                ]
            }
        
        return {'is_vulnerable': False}
