Flicka : Python multi machines magic
====================================

What is Flicka ?
----------------

Flicka allows users to coordinate multiples computers ("slaves") in order to grab chunks from a remote HTTP/FTP/FTPS/SFTP host

Why ?
-----

Some networks administration tools limit bandwith based on MAC/IP address of the user, identified by any sort of credentials on the active network equipment.
In order to circumvent this limitation, it is in fact possible to launch multiples Virtual Machines, bridged (or NATed) on the same network as the host, identified by the same credentials as the host, and thus allowed to require a totally independant amount of bandwith than the host.

With 3 VMs + Host, you can thus require 4*BW than usual, which is not negligeable, while staying legit.


Howto ?
-------

1. Setup one VM (prefer some light one without graphical UI, such as Debian to save some host ressources). 
2. Install all required packages and enable ssh server : see Dependencies.
3. Deploy flicka.py and get.py onto the VM
4. Configure network to be able to communicate with the limiting network equipment
5. Identify your VM to the switch via curl or lynx
6. Create linked clones of this VM, to quickly populate your slaves pool.

The coordinator Python script flicka.py ssh to all slaves based on a slaves.txt file and then issue a custom command over each ssh session to each slave, containing protocol related options, such as offset, chunk size to fecth, output file...

The command issued in fact launches the get.py script located in each slave $HOME directory, which then open a connection to the target host and fetch the requested chunk, and writes it to a common directory shared by all slaves, waiting to be reassembled.


Dependencies
------------

* Python 2.6
* python-paramiko
* openssh-server


Developpement
-------------

Flicka is in early dev phase, and currently allow SFTP reception among unlimited number of slaves is working

Any help is welcome !