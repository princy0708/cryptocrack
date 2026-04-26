from cryptocrack import CryptoCrack
import unittest

class TestBase(unittest.TestCase):
    def test_base16(self):
        assert CryptoCrack().decode('436865636B537472696E67')[0] == 'CheckString', "Base16 test failed."

    def test_base32(self):
        assert CryptoCrack().decode('INUGKY3LKN2HE2LOM4======')[0] == 'CheckString', "Base32 test failed."

    def test_base36(self):
        assert CryptoCrack().decode('45640901731484716')[0] == 'checkstring', "Base36 test failed."

    def test_base58(self):
        assert CryptoCrack().decode('HiVkR1foHM1ZXjk')[0] == 'CheckString', "Base58 test failed."

    def test_base62(self):
        assert CryptoCrack().decode('6ZOc3cWz3dWiylL')[0] == 'CheckString', "Base62 test failed."

    def test_base64(self):
        assert CryptoCrack().decode('Q2hlY2tTdHJpbmc=')[0] == 'CheckString', "Base64 test failed."

    def test_base64url(self):
        assert CryptoCrack().decode('Q2hlY2tTdHJpbmc')[0] == 'CheckString', "Base64Url test failed."

    def test_ascii85(self):
        assert CryptoCrack().decode('6YL%@CK#=qBl7P')[0] == 'CheckString', "ASCII85 test failed."

    def test_base85(self):
        assert CryptoCrack().decode('Luh4VYg2S`X>Ml')[0] == 'CheckString', "Base85 test failed."

    def test_base91(self):                      
        assert CryptoCrack().decode('WXn<v;eYM%Z%xE')[0] == 'CheckString', "Base91 test failed."

    def test_base92(self):
        assert CryptoCrack().decode('9c&KSm]a;#m/X(')[0] == 'CheckString', "Base92 test failed."

    def test_base100(self):
        encode = '👫👟👜🐗👨👬👠👚👢🐗👙👩👦👮👥🐗👝👦👯🐗👡👬👤👧👜👛🐗👦👭👜👩🐗👫👟👜🐗👣👘👱👰🐗👛👦👞🐁'
        assert CryptoCrack().decode(encode)[0] == 'the quick brown fox jumped over the lazy dog', "Base100 test failed."

if __name__ == "__main__":
    unittest.main()
