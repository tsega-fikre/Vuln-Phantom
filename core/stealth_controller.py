"""
Stealth mode controller - Avoid detection and rate limiting
"""

import time
import random
from typing import Dict

class StealthController:
    """Advanced stealth mechanisms for ethical scanning"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.request_count = 0
        self.start_time = time.time()
        
        # Stealth parameters
        self.min_delay = config.get('stealth_min_delay', 0.5)
        self.max_delay = config.get('stealth_max_delay', 2.0)
        self.jitter = config.get('stealth_jitter', 0.3)
        
        # IP rotation simulation (for educational purposes)
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'
        ]
        
    def random_delay(self):
        """
        Introduce random delay to avoid rate limiting
        """
        if self.config.get('stealth_mode', False):
            delay = random.uniform(self.min_delay, self.max_delay)
            time.sleep(delay)
    
    def get_next_user_agent(self) -> str:
        """
        Rotate user agents for stealth
        """
        if self.config.get('stealth_mode', False):
            return random.choice(self.user_agents)
        return self.user_agents[0]
    
    def should_rotate_ip(self) -> bool:
        """
        Determine if IP should be rotated (educational simulation)
        """
        self.request_count += 1
        
        # Rotate every 50 requests in stealth mode
        if self.config.get('stealth_mode', False) and self.request_count >= 50:
            self.request_count = 0
            return True
        
        return False
    
    def get_scan_stats(self) -> Dict:
        """
        Get stealth mode statistics
        """
        elapsed = time.time() - self.start_time
        return {
            'requests_made': self.request_count,
            'avg_delay': (self.min_delay + self.max_delay) / 2,
            'elapsed_time': elapsed,
            'requests_per_second': self.request_count / elapsed if elapsed > 0 else 0
        }
