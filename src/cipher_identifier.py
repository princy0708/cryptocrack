import re

class CipherIdentifier:
    def __init__(self, string):
        self.string = string.strip()

    def identify(self):
        results = []
        
        # Regex patterns for common hashes and ciphers
        patterns = {
            'MD5 / MD4 / NTLM': r'^[a-fA-F0-9]{32}$',
            'SHA-1': r'^[a-fA-F0-9]{40}$',
            'SHA-224': r'^[a-fA-F0-9]{56}$',
            'SHA-256': r'^[a-fA-F0-9]{64}$',
            'SHA-384': r'^[a-fA-F0-9]{96}$',
            'SHA-512': r'^[a-fA-F0-9]{128}$',
            'Bcrypt': r'^\$2[aby]?\$\d{2}\$[./A-Za-z0-9]{53}$',
            'CRC32': r'^[a-fA-F0-9]{8}$',
            'MySQL323': r'^[a-fA-F0-9]{16}$',
            'MySQL4.1/MySQL5': r'^\*[A-F0-9]{40}$',
            'RipeMD-160': r'^[a-fA-F0-9]{40}$',  # Same length as SHA1
            'Tiger-192': r'^[a-fA-F0-9]{48}$',
            'Whirlpool': r'^[a-fA-F0-9]{128}$', # Same length as SHA512
        }

        for cipher, pattern in patterns.items():
            if re.match(pattern, self.string):
                results.append(cipher)

        if not results:
            if self.string.isalpha():
                results.append("Possible Caesar/Vigenere/Substitution Cipher (Alphabetic only)")
            elif set(self.string) <= set('0123456789'):
                results.append("Numeric string (Possible plain text or simple encoding)")
        
        return results
