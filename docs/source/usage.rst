Usage
=====

Encrypting a .env File
----------------------

To encrypt a ``.env`` file, use the :func:`edotenv.core.dotenv_to_edotenv` function:

.. code-block:: python

    from edotenv import dotenv_to_edotenv

    dotenv_to_edotenv('.env', '.env.encrypted')

.. note::

    By default, the key file is stored in the directory of the ``python-dotenv`` package, if you wish to store the key elsewhere, use:
    
    .. code-block:: python
    
        dotenv_to_edotenv('.env', '.env.encrypted', 'path/to/.env.key')

Saving Variables in an Encrypted .env File
------------------------------------------

To save environmental variables in Python to an encrypted ``.env`` file, use the :func:`edotenv.core.save_edotenv` function:

.. code-block:: python

    import os
    from edotenv import save_edotenv

    os.environ['TESTNGA'] = 'testinga123'

    save_edotenv('TESTINGA')

.. note::

    By default, the key file is stored in the directory of the ``python-dotenv`` package and uses ``.env`` as the encrypted file path, if you wish to store the key elsewhere or use a different file name, use:
    
    .. code-block:: python
    
        save_edotenv('TESTINGA', edotenv_path='.env.encrypted', key_path='.env.key')

Loading an Encrypted .env File
------------------------------

To load environmental variables from an encrypted ``.env`` file, use the :func:`edotenv.core.load_edotenv` function:

.. code-block:: python

    import os
    from edotenv import load_edotenv

    load_edotenv()

.. note::

    By default, the key file is stored in the directory of the ``python-dotenv`` package, if you wish to store the key elsewhere, use:
    
    .. code-block:: python
    
        load_edotenv(key_path='.env.key')

Decrypting a .env File
----------------------

To decrypt a ``.env`` file, use the :func:`edotenv.core.edotenv_to_dotenv` function:

.. code-block:: python

    from edotenv import edotenv_to_dotenv

    edotenv_to_dotenv('.env', '.env.encrypted')

.. note::

    By default, the key file is stored in the directory of the ``python-dotenv`` package, if you wish to store the key elsewhere, use:
    
    .. code-block:: python
    
        edotenv_to_dotenv('.env', '.env.encrypted', 'path/to/.env.key')