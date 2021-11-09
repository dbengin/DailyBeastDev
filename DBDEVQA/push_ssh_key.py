#!/usr/bin/python
import os
from getpass import getpass

import paramiko

def deploy_key(key, server, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password)
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')

key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
#username = os.getlogin()
username="dannyf"
password = getpass()
hosts = ["mysql-master01.dailybeast.com", 
"mysql-master02.dailybeast.com", 
"mysql-p-slave01.dailybeast.com", 
"mysql-p-slave02.dailybeast.com", 
"mysql-read01.dailybeast.com",
"mysql-lb-slave01.dailybeast.com",
"nagios.dailybeast.com",
"solr101.internal.east1c.aws.dailybeast.com",
"solr102.internal.east1c.aws.dailybeast.com",
"solr201.internal.east1d.aws.dailybeast.com",
"solr202.internal.east1d.aws.dailybeast.com",
"solr301.internal.east1d.aws.dailybeast.com",
"172.24.122.43",
"172.24.62.72",
"172.24.22.230"
]
for host in hosts:
    deploy_key(key, host, username, password)
    