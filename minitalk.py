import os
import sys
import random
import string

pid = sys.argv[1] if len(sys.argv) >= 2 else input('pid: ')
length = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2].isdigit() else 500
print_all_args = True if '-a' in sys.argv else False

makefile_cmd = 'make'
client_path = 'client'

os.popen(makefile_cmd).read()

if not os.path.exists(client_path):
	print(f'don\'t find {client_path}')
	exit()

if 'unicode' in sys.argv:
	args = ''.join(random.choices('ரறலளழவஶஷஸஹఠడఢణతథదధనචඡජඣඤඥඦටඨའཡརལཤཥསཧཨ', k=length))
else:
	args = ''.join(random.choices(string.ascii_letters + string.digits + "!#$%*+,-./:;=?@^_~", k=length))

if print_all_args:
	print(f'ARGS = \'{args}\'')
else:
	print(f'ARGS = ...{args[-10:]}')
print(os.popen(f'./{client_path} {pid} "{args}"').read().removesuffix('\n'))
print('send !')
