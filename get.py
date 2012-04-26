import paramiko
import sys
import os
import time
from glob import iglob
import shutil

target = {}
target["ip"] = sys.argv[1]
target["port"] = sys.argv[2]
target["user"] = sys.argv[3]
target["passwd"] = sys.argv[4]
target["remotepath"] = sys.argv[5]
target["offset"] = sys.argv[6]
target["size"] = sys.argv[7]
target["output"] = sys.argv[8]
target["end"] = sys.argv[9]
target["localpath"] = sys.argv[10]
temp = target["remotepath"].split('/')
target["filename"] = temp[len(temp)-1]

print target["localpath"]+target["filename"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(target["ip"], int(target["port"]), target["user"], target["passwd"])
ftp = ssh.open_sftp()
fr = ftp.file(target["remotepath"], 'rb') 
fr.seek(long(target["offset"]))
file_size = long(target["size"])
fr.prefetch() 
path = target["localpath"] + target["output"]

# main sftp routine
try: 
	fl = file(path, 'wb') 
	try: 
		size = 0 
		while True: 
			if (file_size - size > 32768):
				data = fr.read(32768) 
			else:
				data = fr.read(file_size - size)
			if len(data) == 0: 
				# print "stop"
				break 
			fl.write(data) 
			size += len(data) 
			# print str(size) + " - " + str(file_size)
	finally: 
		fl.close() 
finally: 
	fr.close() 
s = os.stat(path) 
if s.st_size != size: 
	raise IOError('size mismatch in get!  %d != %d' % (s.st_size, size)) 
   
ftp.close()

# if we are the last slave (last chunk) wait and concatenate all chunks to the end file
if (target["end"] == "last"):
	time.sleep(10)
	destination = open(target["localpath"] + target["filename"], 'wb')
	for filename in iglob(os.path.join(target["localpath"], 'chunk*')):
		f = open(filename, 'rb')
		shutil.copyfileobj(f, destination)
		f.close()
		os.remove(filename)
	destination.close()	
	