============
|catimg| cat
============

.. |catimg| image:: src/cat.ico
    :width: 48

cat is console based application to print out contents of given files as arguments

=============
Documentation
=============

Installation
============

Method 1
--------

Cloning from git

.. code-block:: bash

    git clone https://github.com/TodoLodo/Passwords

Method 2
--------

Via Github repo zip download

.. image:: https://github.com/TodoLodo/TodoLodo/blob/main/imgs/buttons/GithubDownloadZip%5B276x48%5D.png
    :target: https://github.com/TodoLodo/cat/archive/refs/heads/main.zip


Method 2
--------

Via SourceForge

.. image:: https://a.fsdn.com/con/app/sf-download-button
    :target: https://sourceforge.net/projects/wincat/files/latest/download

Initiation
==========

Run ``catToPath.exe`` while selecting yes in the followed prompt window

If any error occurs related to path variable, the bin folder path in the root dir may have to be added to path manually

Usage
=====

On successful completion of previous steps ``cat`` will be available on the terminal, to confirm run cat with either of the flags ``-v`` or ``--version``

.. code-block:: bash

    cat -v

To print out contents of a file use the following command

.. code-block:: bash
        cat path\to\fileName.extension

Optionally flags can be mentioned separated by spaces for different functionalities which are list bellow

+-------+---------------------------------------+
| Flag  | Functionality                         |
+=======+=======================================+
| -n    | Numbers each line in increment order  |
+-------+---------------------------------------+
| -E    | Prints "$" at each end of a line      |
+-------+---------------------------------------+
