Usage
=====

This section provides details and examples on how to use the package in Python.

.. note::

    By default, the key file is stored in the directory of the ``python-dotenv`` package.
    
    Change the parameter ``key_path`` in each function if another location is desired.

    For example:

    .. code-block:: python

        dotenv_to_edotenv('.env', '.env.encrypted', key_path='path/to/.env.key')

Encrypting a .env File
----------------------

To encrypt a ``.env`` file, use the :func:`edotenv.core.dotenv_to_edotenv` function:

.. code-block:: python

    from edotenv import dotenv_to_edotenv

    dotenv_to_edotenv('.env', '.env.encrypted')

Saving Variables in an Encrypted .env File
------------------------------------------

To save environmental variables in Python to an encrypted ``.env`` file, use the :func:`edotenv.core.save_edotenv` function:

.. code-block:: python

    import os
    from edotenv import save_edotenv

    os.environ['TESTNGA'] = 'testinga123'

    save_edotenv('TESTINGA')

Loading an Encrypted .env File
------------------------------

To load environmental variables from an encrypted ``.env`` file, use the :func:`edotenv.core.load_edotenv` function:

.. code-block:: python

    import os
    from edotenv import load_edotenv

    load_edotenv()

Decrypting a .env File
----------------------

To decrypt a ``.env`` file, use the :func:`edotenv.core.edotenv_to_dotenv` function:

.. code-block:: python

    from edotenv import edotenv_to_dotenv

    edotenv_to_dotenv('.env', '.env.encrypted')
