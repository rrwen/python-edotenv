import os

from cryptography.fernet import Fernet

__PATH__ = os.path.dirname(os.path.abspath(__file__))

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

    Return
    ------
    str
        The decrypted string.

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

    Return
    ------
    bytes
        The encrypted string as bytes.

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

    Return
    ------
    bytes
        Key for encrypting and decrypting.

    Example
    -------
    .. jupyter-execute::

        from edotenv.encryption import gen_key

        key = gen_key()
        print(key)
    """
    out = Fernet.generate_key()
    return out

def read_key_file(key_path=None, create_if_not_exists=True):
    """
    Read a key file or create one if it does not exist.

    Parameters
    ----------
    key_path : str or None
        The path to the key used to encrypt and decrypt the .env file.
        
        * If the file does not exist, then a key file will be automatically generated
        * If ``None``, defaults to a file inside the package's directory
    
    create_if_not_exists : bool
        Whether to generate a new key and create the key file if it does not exist.

    Return
    ------
    bytes
        Key for encrypting and decrypting from the key file.

    Example
    -------
    .. jupyter-execute::

        import tempfile

        from edotenv.encryption import read_key_file
        
        with tempfile.TemporaryDirectory() as folder:
            key_path = f'{folder}/.env.key'
            key = read_key_file(key_path)
            print(key)
    """

    # Get the key path or use default at package dir if None
    key_path = key_path if key_path else os.path.join(__PATH__, '.env.key')

    # Read key from key file
    if os.path.isfile(key_path):
        with open(key_path, 'rb') as key_file:
            out = key_file.read()

    # Gen key and save key file
    elif create_if_not_exists:
        out = gen_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(out)
    
    # Key file does not exist
    else:
        raise ValueError(f'Key file at "{key_path}" does not exist')
    return out