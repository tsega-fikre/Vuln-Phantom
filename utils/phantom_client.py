"""
Phantom HTTP Client - Advanced request handling with stealth capabilities
"""

import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Dict, Optional

class PhantomHTTPClient:
    """Advanced HTTP client with stealth and retry capabilities"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.timeout = config.get('timeout', 10)
        self.session = self._create_session()
        
    def _create_session(self) -> requests.Session:
        """Create session with retry strategy"""
        session = requests.Session()
        
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Default headers
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        })
        
        return session
    
    def get(self, url: str) -> Dict:
        """
        Perform GET request with error handling
        """
        try:
            start_time = time.time()
            response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            response_time = time.time() - start_time
            
            return {
                'status_code': response.status_code,
                'text': response.text,
                'headers': dict(response.headers),
                'time': response_time,
                'url': response.url
            }
            
        except requests.exceptions.Timeout:
            return {'status_code': 408, 'text': '', 'error': 'Timeout', 'time': self.timeout}
        except requests.exceptions.ConnectionError:
            return {'status_code': 0, 'text': '', 'error': 'Connection Error', 'time': 0}
        except Exception as e:
            return {'status_code': 0, 'text': '', 'error': str(e), 'time': 0}
