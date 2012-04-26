Flicka : Python multi machines magic
====================================

What is Flicka ?
----------------

Flicka allows users to coordinate multiples computers ("slaves") in order to grab chunks from a remote HTTP/FTP/FTPS/SFTP host


Howto ?
-------

The coordinator Python script flicka.py ssh to all slaves based on a slaves.txt file and then issue a custom command to each slave containing protocol related options, such as offset, chunk size to fecth, output file...


Developpement
-------------

Flicka is in early dev phase, and currently allow SFTP reception among unlimited number of slaves
