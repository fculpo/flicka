Flicka : Python multi machines magic
====================================

What is Flicka ?
----------------

Flicka allows users to coordinate multiples computers ("slaves") in order to grab chunks from a remote HTTP/FTP/FTPS/SFTP host


Howto ?
-------

The coordinator Python script flicka.py ssh to all slaves based on a slaves.txt file and then issue a custom command over each ssh session to each slave, containing protocol related options, such as offset, chunk size to fecth, output file...

The command issued in fact launches the get.py script located in each slave $HOME directory, which then open a connection to the target host and fetch the requested chunk, and writes it to a common directory shared by all slaves, waiting to be reassembled.


Developpement
-------------

Flicka is in early dev phase, and currently allow SFTP reception among unlimited number of slaves
