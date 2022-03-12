How it Works
============

This package uses `python-dotenv <https://pypi.org/project/python-dotenv/0.19.2/>`_ to read and load environmental variables from ``.env`` files, and `cryptography <https://pypi.org/project/cryptography/>`_ for encrypting and decrypting ``.env`` files.

The purpose of this package is to avoid plain text ``.env`` files by encrypting them, which can be useful in cases where the ``.env`` file is shared unintentionally (e.g. committed by accident, forgot to remove before sending in an email, malicious access when leaving computer unattended).

The scope of this package is limited to:

1. Encrypting/decrypting ``.env`` files with a randomly generated key
2. Loading environmental variables from encrypted ``.env`` files into Python
3. Saving environmental variables from Python into encrypted ``.env`` files

.. digraph:: methods

   rankdir = LR;
   
   file[label=".env" shape=oval];
   dotenv[label="dotenv (pkg)" shape=rect];
   cryptography[label="cryptography (pkg)" shape=rect];

   subgraph cluster0 {
      label=< <B>edotenv (pkg)</B> >;
      style=rounded;

      file -> dotenv [label=<<I>read/load</I>>];
      dotenv -> cryptography [label=<<I>encrypt</I>>];
      cryptography -> file [label=<<I>decrypt</I>>];
   }

For more details, see the `API Reference <./reference/index.html>`_ for source code and documentation.