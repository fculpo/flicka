import paramiko
import sys


hosts = []
""" Target ip, port, user, passwd, remotepath, localpath """
target = [sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
connections = []

""" Loading slaves addresses into memory """
hostsFile = open('./slaves.txt', 'r')
data = hostsFile.readlines()
for line in data:
	hosts.append(line.split(','))

""" Setting up all ssh connections to slaves """
for host in hosts:
	print host
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host[0], int(host[1]), username=host[2], password=host[3])
	connections.append(client)

""" Getting the size of the target file to transfer """
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(target[0], target[1], target[2], target[3])

ftp = ssh.open_sftp()
stat = ftp.stat(target[4])
ftp.close()

size = stat.st_size

""" Computing the chunks sizes for future requests to slaves """
chunks = []
chunkSize = size//len(hosts)
reste = size%chunkSize
chunks.append(chunkSize + reste)
for i in range(1,len(hosts)+1):
	chunks.append(chunkSize)
	print chunks[i]

""" send orders to slaves for parallel transfers """
i = 0
offset = 0
for host, conn in zip(hosts, connections):
	end = "last" if (i == len(hosts)-1) else "osef" # if last chunk then echo it to the slave
	# command line to pass to destination slave
	command = "python ~/get.py " + target[0] + " " + str(target[1]) + " " + target[2] + " " + target[3] + " " + target[4] + " " + str(offset) + " " + str(chunks[i]) + " chunk" + str(i) + " " + end + " " + target[5]
	print command
	stdin, stdout, stderr = conn.exec_command(command)
	# stdout.readlines()
	# stdin.close()
	offset += chunks[i]
	i += 1