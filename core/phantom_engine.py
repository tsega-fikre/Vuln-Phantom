"""
VulnPhantom Core Engine - Elite Web Vulnerability Scanner
Advanced multi-threaded scanning with intelligent detection
"""

import time
import random
import threading
from queue import Queue
from typing import Dict, List, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from core.payload_arsenal import PayloadArsenal
from core.detection_ai import DetectionEngine
from core.stealth_controller import StealthController
from utils.phantom_client import PhantomHTTPClient
from utils.color_display import PhantomDisplay

class VulnPhantomEngine:
    """Advanced scanning engine with multi-threading and intelligent detection"""
    
    def __init__(self, target_url: str, config: Dict):
        self.target_url = target_url
        self.config = config
        self.display = PhantomDisplay()
        self.http_client = PhantomHTTPClient(config)
        self.payload_arsenal = PayloadArsenal()
        self.detection_engine = DetectionEngine()
        self.stealth = StealthController(config) if config.get('stealth_mode') else None
        
        self.results = []
        self.vulnerabilities = []
        self.scan_id = str(int(time.time()))
        
        # Threading controls
        self.task_queue = Queue()
        self.max_workers = config.get('threads', 5)
        self.results_lock = threading.Lock()
        
    def extract_parameters(self) -> Dict[str, any]:
        """
        Advanced parameter extraction with context analysis
        """
        parsed = urlparse(self.target_url)
        params = parse_qs(parsed.query)
        
        # Analyze parameter context
        parameter_analysis = {}
        for param_name, param_values in params.items():
            value = param_values[0] if param_values else ''
            
            # Detect parameter type based on naming patterns
            param_type = self._analyze_parameter_type(param_name, value)
            
            parameter_analysis[param_name] = {
                'name': param_name,
                'value': value,
                'type': param_type,
                'original_value': value
            }
        
        return parameter_analysis
    
    def _analyze_parameter_type(self, name: str, value: str) -> str:
        """
        Intelligent parameter type detection
        """
        name_lower = name.lower()
        
        # ID-like parameters
        if any(keyword in name_lower for keyword in ['id', 'uid', 'userid', 'postid']):
            return 'numeric'
        
        # Search parameters
        if any(keyword in name_lower for keyword in ['search', 'q', 'query', 'find']):
            return 'search'
        
        # Username parameters
        if any(keyword in name_lower for keyword in ['user', 'username', 'login', 'email']):
            return 'string'
        
        # File parameters
        if any(keyword in name_lower for keyword in ['file', 'path', 'doc', 'page']):
            return 'file'
        
        return 'unknown'
    
    def _inject_payload_advanced(self, url: str, param_name: str, original_value: str, 
                                 payload: str, injection_type: str) -> str:
        """
        Advanced payload injection with multiple strategies
        """
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        # Different injection strategies based on type
        if injection_type == 'append':
            injected_value = original_value + payload
        elif injection_type == 'prepend':
            injected_value = payload + original_value
        elif injection_type == 'replace':
            injected_value = payload
        elif injection_type == 'json_inject':
            # Simulate JSON injection
            injected_value = f'{{"value":"{original_value}{payload}"}}'
        else:
            injected_value = payload
        
        params[param_name] = [injected_value]
        
        # Rebuild URL
        new_query = urlencode(params, doseq=True)
        new_url = urlunparse(parsed._replace(query=new_query))
        
        return new_url
    
    def scan_parameter_advanced(self, param_info: Dict) -> List[Dict]:
        """
        Comprehensive parameter scanning with multiple strategies
        """
        param_name = param_info['name']
        original_value = param_info['value']
        param_type = param_info['type']
        
        results = []
        
        # Get payloads based on parameter type
        payloads_to_test = self.payload_arsenal.get_payloads_by_context(param_type)
        
        # Baseline request for comparison
        baseline_response = self.http_client.get(self.target_url)
        baseline_length = len(baseline_response.get('text', ''))
        
        for payload_info in payloads_to_test:
            # Stealth mode delay
            if self.stealth:
                self.stealth.random_delay()
            
            # Multiple injection strategies
            for strategy in ['replace', 'append']:
                test_url = self._inject_payload_advanced(
                    self.target_url, param_name, original_value, 
                    payload_info['payload'], strategy
                )
                
                # Send request with timing
                start_time = time.time()
                response = self.http_client.get(test_url)
                response_time = time.time() - start_time
                
                # Intelligent detection
                vuln = self.detection_engine.analyze_response(
                    response=response,
                    payload=payload_info['payload'],
                    vuln_type=payload_info['type'],
                    baseline_length=baseline_length,
                    response_time=response_time,
                    original_value=original_value
                )
                
                if vuln and vuln.get('is_vulnerable'):
                    with self.results_lock:
                        self.vulnerabilities.append({
                            'parameter': param_name,
                            'vulnerability_type': vuln['type'],
                            'payload': payload_info['payload'],
                            'confidence': vuln['confidence'],
                            'severity': vuln['severity'],
                            'evidence': vuln['evidence'],
                            'timestamp': time.time()
                        })
                    
                    results.append(vuln)
                    
                    # Display finding immediately
                    self.display.print_vulnerability_found(
                        param_name, 
                        vuln['type'], 
                        vuln['confidence'], 
                        vuln['severity']
                    )
        
        return results
    
    def run_elite_scan(self) -> Dict:
        """
        Orchestrate elite-level scanning with multi-threading
        """
        self.display.print_banner()
        self.display.print_scan_start(self.target_url)
        
        # Extract and analyze parameters
        parameters = self.extract_parameters()
        
        if not parameters:
            self.display.print_error("No parameters found in URL")
            return {'error': 'No parameters found'}
        
        self.display.print_parameter_summary(len(parameters))
        
        # Multi-threaded scanning
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_param = {
                executor.submit(self.scan_parameter_advanced, param_info): param_name
                for param_name, param_info in parameters.items()
            }
            
            for future in as_completed(future_to_param):
                param_name = future_to_param[future]
                try:
                    results = future.result()
                except Exception as e:
                    self.display.print_error(f"Error scanning {param_name}: {str(e)}")
        
        # Generate final report
        report = self._generate_elite_report(parameters)
        
        self.display.print_scan_complete(len(self.vulnerabilities))
        
        return report
    
    def _generate_elite_report(self, parameters: Dict) -> Dict:
        """
        Generate comprehensive scan report
        """
        severity_counts = {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
        for vuln in self.vulnerabilities:
            severity_counts[vuln['severity']] += 1
        
        return {
            'scan_id': self.scan_id,
            'target': self.target_url,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'parameters_tested': len(parameters),
            'total_vulnerabilities': len(self.vulnerabilities),
            'severity_breakdown': severity_counts,
            'vulnerabilities': self.vulnerabilities,
            'scan_duration': time.time() - self.scan_start_time if hasattr(self, 'scan_start_time') else 0
        }
