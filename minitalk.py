import os
import re
import sys
import random
import string

pid = int(sys.argv[1]) if len(sys.argv) >= 2 else input('pid: ')
length = int(sys.argv[2]) if len(sys.argv) >= 3 else 500

makefile_cmd = 'make'
client_path = 'client'

os.popen(makefile_cmd).read()

if not os.path.exists(client_path):
	print(f'don\'t find {client_path}')
	exit()

args = ''.join(random.choices(string.ascii_letters + string.digits + "!#$%*+,-./:;=?@^_~", k=length))
print(f'ARGS = ...{args[-10:]}')
print(os.popen(f'./{client_path} {pid} "{args}"').read().removesuffix('\n'))
print('send !')
