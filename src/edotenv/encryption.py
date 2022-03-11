from cryptography.fernet import Fernet

def decrypt(target, key, decode=True, encoding='utf8'):
    """
    Decrypt a string.

    Parameters
    ----------
    target : str or bytes
        The string to decrypt.
    key : str
        The key used to decrypt the string.
    decode : bool
        Whether to decode the ``target`` from bytes after decryption or not.
    encoding : str
        Encoding used to decode the ``target`` from bytes if ``decode`` is ``True``.

    Example
    -------
    .. jupyter-execute::

        from edotenv.encryption import *
        
        # Encrypt string
        key = gen_key()
        target = 'Encryption time!'
        encrypted = encrypt(target, key)
        print('encrypted: ' + str(encrypted))

        # Decrypt string
        decrypted = decrypt(encrypted, key)
        print('decrypted: ' + decrypted)
    """
    decrypter = Fernet(key)
    out = decrypter.decrypt(target)
    out = out.decode(encoding) if decode else out
    return out

def encrypt(target, key, to_bytes=True, encoding='utf8'):
    """
    Encrypt a string.

    Parameters
    ----------
    target : str or bytes
        The string to encrypt.
    key : str
        The key used to encrypt the string.
    to_bytes : bool
        Whether to convert the ``target`` to bytes before encryption or not.
    encoding : str
        Encoding used to convert the ``target`` to bytes if ``to_bytes`` is ``True``.

    Example
    -------
    .. jupyter-execute::

        from edotenv.encryption import encrypt
        
        key = gen_key()
        target = 'Encryption time!'
        encrypted = encrypt(target, key)
        print(encrypted)
    """
    encrypter = Fernet(key)
    target = bytes(target, encoding=encoding) if to_bytes else target
    out = encrypter.encrypt(target)
    return out

def gen_key():
    """
    Generate a key for encryption and decryption.

    Example
    -------
    .. jupyter-execute::

        from edotenv.encryption import gen_key

        key = gen_key()
        print(key)

    """
    out = Fernet.generate_key()
    return out