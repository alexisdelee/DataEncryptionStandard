from core import DataEncryptionStandardCipher, DataEncryptionStandardDecipher

class Method():
    Cipher = DataEncryptionStandardCipher.run
    Decipher = DataEncryptionStandardDecipher.run

def compute(key, message, fn):
    assert type(key) is str
    assert type(message) is str
    assert fn is Method.Cipher or fn is Method.Decipher

    return fn(key, message)
