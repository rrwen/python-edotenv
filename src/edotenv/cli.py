import argparse
import os

from .core import *

__PATH__ = os.path.dirname(os.path.abspath(__file__))

def _get_parser():
    """
    Builds an ``argparse`` parser for the ``edotenv`` command line tool.

    Returns
    -------
    :class:`argparse.ArgumentParser`
        An ``argparse`` parser for ``edotenv``.

    Example
    -------
    .. jupyter-execute::
        :hide-output:

        from edotenv.cli import _get_parser
        parser = _get_parser()
        parser.print_help()
    """

    # Create parsers
    parser = argparse.ArgumentParser(description='Manages encrypted .env files')
    subparsers = parser.add_subparsers(title='commands', dest='command')

    # Add encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='encrypt a .env file')
    encrypt_parser.add_argument('dotenv_path', nargs='?', type=str, default='.env', help='path to .env file')
    encrypt_parser.add_argument('edotenv_path', nargs='?', type=str, default='.env', help='path to encrypted .env file')
    encrypt_parser.add_argument('--key_path',  type=str, default=None, help='path to key file')
    
    # Add decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='decrypt an encrypted .env file')
    decrypt_parser.add_argument('dotenv_path', nargs='?', type=str, default='.env', help='path to .env file')
    decrypt_parser.add_argument('edotenv_path', nargs='?', type=str, default='.env', help='path to encrypted .env file')
    decrypt_parser.add_argument('--key_path', type=str, default=None, help='path to key file')

    # Add clear command
    clear_parser = subparsers.add_parser('clear', help='clear encrypted .env or key file')
    clear_parser.add_argument('--edotenv_path', type=str, default=None, help='path to encrypted .env file - ignored if not set')
    clear_parser.add_argument('--key_path', type=str, default=None, help='path to key file')
    
    # Return cli parser
    out = parser
    return out

def run():
    """
    Runs the ``edotenv`` command.

    Example
    -------
    >>> edotenv --help

    .. jupyter-execute::
        :hide-code:

        from edotenv.cli import _get_parser
        parser = _get_parser()
        parser.print_help()

    Encrypt .env file:

    >>> edotenv encrypt .env .env.encrypted

    Decrypt .env file:

    >>> edotenv decrypt .env .env.encrypted

    Clear encrypted .env and key files:

    >>> edotenv clear --edotenv_path .env
    """

    # Get arguments and command
    parser = _get_parser()
    kwargs = vars(parser.parse_args())
    command = kwargs.pop('command')

    # Run commands
    if command == 'encrypt':
        dotenv_to_edotenv(**kwargs)
    elif command == 'decrypt':
        edotenv_to_dotenv(**kwargs)
    elif command == 'clear':
        key_path = kwargs['key_path']
        key_path = key_path if key_path else os.path.join(__PATH__, '.env.key')
        edotenv_path = kwargs['edotenv_path']
        if edotenv_path: # del encrypted .env file
            if os.path.isfile(edotenv_path):
                os.remove(edotenv_path)
        if os.path.isfile(key_path): # del key file
            os.remove(key_path)
    else:
        parser.print_help()