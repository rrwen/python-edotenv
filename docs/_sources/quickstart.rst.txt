Quick Start
===========

First, use the command ``edotenv`` in a command line terminal to encrypt a ``.env`` file:

.. code::

    edotenv encrypt

Once the ``.env`` file is encrypted, you can load environmental variables in Python:

.. code-block:: python

    from edotenv import load_edotenv

    load_edotenv()

.. note::

    The key file is used to encrypt and decrypt the ``.env`` file.
    
    By default and for convenience, this key file is stored in the package's folder to avoid accidental commits, but will be wiped in cases where a new virtual environment is used or the package is reinstalled/upgraded.

    In order to persist the key file, you will have to choose a safe location for it by setting the parameter ``--key_path`` in the command line terminal:

    .. code::

        edotenv encrypt --key_path path/to/.env.key

    For help with the ``edotenv`` command use:

    .. code::

        edotenv --help
        edotenv encrypt --help
        edotenv decrypt --help
