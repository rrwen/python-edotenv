import os

from dotenv import load_dotenv, dotenv_values
from io import StringIO

from .encryption import *

def dotenv_to_edotenv(dotenv_path='.env', edotenv_path='.env', key_path=None, *args, **kwargs):
    """
    Encrypt a .env file.

    Parameters
    ----------
    dotenv_path : str
        The path of the .env file.
    edotenv_path : str
        The path of the encrypted .env file.
    key_path : str or None
        The path to the key used to encrypt and decrypt the .env file.
        
        * If the file does not exist, then a key file will be automatically generated
        * If ``None``, defaults to a file inside the package's directory

    *args, **kwargs
        Additional arguments passed to `dotenv.dotenv_values <https://saurabh-kumar.com/python-dotenv/reference/dotenv/main/#dotenv_values>`_.

    Example
    -------
    .. jupyter-execute::

        import tempfile
        import os

        from edotenv import dotenv_to_edotenv, load_edotenv

        with tempfile.TemporaryDirectory() as folder:

            # Remove vars for testing
            if 'TESTINGA' in os.environ:
                del os.environ['TESTINGA']
            if 'TESTINGB' in os.environ:
                del os.environ['TESTINGB']

            # Create a .env file with vars TESTINGA and TESTINGB
            dotenv_path = f'{folder}/.env'           
            with open(dotenv_path, 'w') as dotenv_file:
                dotenv_file.write('TESTINGA=testinga123\\nTESTINGB=testingb123')

            # Check if the vars exist
            print('TESTINGA in env (not loaded): ' + str('TESTINGA' in os.environ))
            print('TESTINGB in env (not loaded): ' + str('TESTINGA' in os.environ))

            # Encrypt the .env file
            edotenv_path = f'{folder}/.env.encrypted'
            key_path = f'{folder}/.env.key'
            dotenv_to_edotenv(dotenv_path, edotenv_path, key_path)

            # Load the encrypted .env file
            load_edotenv(edotenv_path, key_path)

            # Check if vars exist again
            print('TESTINGA value (loaded): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (loaded): ' + str(os.environ['TESTINGB']))
    """

    # Get .env file data
    values = dotenv_values(dotenv_path, *args, **kwargs)
    data = '\n'.join([v + '=' + values[v] for v in values])

    # Get the key from file or gen key file if not exists
    key = read_key_file(key_path)

    # Save encrypted .env file
    edata = encrypt(data, key)
    with open(edotenv_path, 'wb') as edotenv_file:
        edotenv_file.write(edata)

def edotenv_to_dotenv(dotenv_path='.env', edotenv_path='.env', key_path=None, *args, **kwargs):
    """
    Decrypt a .env file.

    Parameters
    ----------
    dotenv_path : str
        The path of the .env file.
    edotenv_path : str
        The path of the encrypted .env file.
    key_path : str or None
        The path to the key used to encrypt and decrypt the .env file.
        
        * If the file does not exist, then a key file will be automatically generated
        * If ``None``, defaults to a file inside the package's directory

    Example
    -------
    .. jupyter-execute::

        import tempfile
        import os

        from dotenv import load_dotenv
        from edotenv import dotenv_to_edotenv, load_edotenv, edotenv_to_dotenv

        with tempfile.TemporaryDirectory() as folder:

            # Remove vars for testing
            if 'TESTINGA' in os.environ:
                del os.environ['TESTINGA']
            if 'TESTINGB' in os.environ:
                del os.environ['TESTINGB']

            # Create a .env file with vars TESTINGA and TESTINGB
            dotenv_path = f'{folder}/.env'           
            with open(dotenv_path, 'w') as dotenv_file:
                dotenv_file.write('TESTINGA=testinga123\\nTESTINGB=testingb123')

            # Check if the vars exist
            print('TESTINGA in env (not loaded): ' + str('TESTINGA' in os.environ))
            print('TESTINGB in env (not loaded): ' + str('TESTINGA' in os.environ))

            # Encrypt the .env file
            edotenv_path = f'{folder}/.env.encrypted'
            key_path = f'{folder}/.env.key'
            dotenv_to_edotenv(dotenv_path, edotenv_path, key_path)

            # Load the encrypted .env file
            load_edotenv(edotenv_path, key_path)

            # Check if vars exist again
            print('TESTINGA value (loaded): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (loaded): ' + str(os.environ['TESTINGB']))

            # Decrypt the .env file
            dotenv_path = f'{folder}/.env.decrypted'
            edotenv_to_dotenv(dotenv_path, edotenv_path, key_path)

            # Remove vars for testing
            if 'TESTINGA' in os.environ:
                del os.environ['TESTINGA']
            if 'TESTINGB' in os.environ:
                del os.environ['TESTINGB']

            # Check if the vars exist after removal for testing decrypted file
            print('TESTINGA in env (before loading decrypt): ' + str('TESTINGA' in os.environ))
            print('TESTINGB in env (before loading decrypt): ' + str('TESTINGA' in os.environ))

            # Load the decrypted .env file
            load_dotenv(dotenv_path)

            # Check if vars exist again after loading decrypted file
            print('TESTINGA value (after loading decrypt): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (after loading decrypt): ' + str(os.environ['TESTINGB']))
    """

    # Read encrypted .env file
    with open(edotenv_path, 'rb') as edotenv_file:
        edata = edotenv_file.read()

    # Get the key from file or gen key file if not exists
    key = read_key_file(key_path)

    # Decrypt env vars and save to .env file
    data = decrypt(edata, key)
    with open(dotenv_path, 'w') as dotenv_file:
        dotenv_file.write(data)

def load_edotenv(edotenv_path='.env', key_path=None, *args, **kwargs):
    """
    Load environmental varables from an encrypted .env file.

    Parameters
    ----------
    edotenv_path : str
        The path of the encrypted .env file.
    key_path : str or None
        The path to the key used to encrypt and decrypt the .env file. If ``None``, defaults to a file inside the package's directory.
    *args, **kwargs
        Additional arguments passed to `dotenv.load_dotenv <https://saurabh-kumar.com/python-dotenv/reference/dotenv/main/#load_dotenv>`_.

    Example
    -------
    .. jupyter-execute::

        import tempfile
        import os

        from edotenv import dotenv_to_edotenv, load_edotenv

        with tempfile.TemporaryDirectory() as folder:

            # Remove vars for testing
            if 'TESTINGA' in os.environ:
                del os.environ['TESTINGA']
            if 'TESTINGB' in os.environ:
                del os.environ['TESTINGB']

            # Create a .env file with vars TESTINGA and TESTINGB
            dotenv_path = f'{folder}/.env'           
            with open(dotenv_path, 'w') as dotenv_file:
                dotenv_file.write('TESTINGA=testinga123\\nTESTINGB=testingb123')

            # Check if the vars exist
            print('TESTINGA in env (not loaded): ' + str('TESTINGA' in os.environ))
            print('TESTINGB in env (not loaded): ' + str('TESTINGA' in os.environ))

            # Encrypt the .env file
            edotenv_path = f'{folder}/.env.encrypted'
            key_path = f'{folder}/.env.key'
            dotenv_to_edotenv(dotenv_path, edotenv_path, key_path)

            # Load the encrypted .env file
            load_edotenv(edotenv_path, key_path)

            # Check if vars exist again
            print('TESTINGA value (loaded): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (loaded): ' + str(os.environ['TESTINGB']))
    """

    # Read encrypted .env file
    with open(edotenv_path, 'rb') as edotenv_file:
        edata = edotenv_file.read()

    # Get the key from file or gen key file if not exists
    key = read_key_file(key_path, create_if_not_exists=False)
    
    # Decrypt env vars and load them
    data = decrypt(edata, key)
    stream = StringIO(data)
    load_dotenv(stream=stream, *args, **kwargs)

def save_edotenv(vars, edotenv_path='.env', key_path=None):
    """
    Load environmental varables from an encrypted .env file.

    Parameters
    ----------
    edotenv_path : str
        The path of the encrypted .env file.
    key_path : str or None
        The path to the key used to encrypt and decrypt the .env file.
        
        * If the file does not exist, then a key file will be automatically generated
        * If ``None``, defaults to a file inside the package's directory

    vars : str OR list
        A list of the environmental variable names to save into the encrypted .env file.

    Example
    -------
    .. jupyter-execute::

        import tempfile
        import os

        from edotenv import save_edotenv, load_edotenv

        with tempfile.TemporaryDirectory() as folder:

            # Remove vars for testing
            if 'TESTINGA' in os.environ:
                del os.environ['TESTINGA']
            if 'TESTINGB' in os.environ:
                del os.environ['TESTINGB']

            # Set env vars TESTINGA and TESTINGB
            os.environ['TESTINGA'] = 'testinga123'
            os.environ['TESTINGB'] = 'testingb123'

            # Check the values of the vars
            print('TESTINGA value (before save): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (before save): ' + str(os.environ['TESTINGB']))

            # Save an encrypted .env file of the vars
            edotenv_path = f'{folder}/.env.encrypted'
            key_path = f'{folder}/.env.key'
            vars = ['TESTINGA', 'TESTINGB']       
            save_edotenv(vars, edotenv_path, key_path)

            # Load the encrypted .env file
            load_edotenv(edotenv_path, key_path)

            # Check if the vars loaded correctly from encrypted .env file
            print('TESTINGA value (after save): ' + str(os.environ['TESTINGA']))
            print('TESTINGB value (after save): ' + str(os.environ['TESTINGB']))
    """

    # Get the key from file or gen key file if not exists
    key = read_key_file(key_path)
    
    # Get and encrypt env vars
    vars = vars if isinstance(vars, list) else [vars]
    data = '\n'.join([v + '=' + str(os.environ[v]) for v in vars])
    edata = encrypt(data, key)
    
    # Save encrypted .env file
    with open(edotenv_path, 'wb') as edotenv_file:
        edotenv_file.write(edata)
        