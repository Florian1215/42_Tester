import os
import re
import sys
import random

# python3.9 push_swap.py
#		'\d+' for specify length of args
#		'-a' for print test args
#		'evaluating' for check all


int_min = -10000
int_max = 10000

makefile_cmd = 'make'
checker_path = 'checker_Mac'
push_swap_path = 'push_swap'






length = int(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].isdigit() else 100
os.popen(makefile_cmd).read()

if not os.path.exists(push_swap_path) or not os.path.exists(checker_path):
	print(f'Error: don\'t find {push_swap_path} or {checker_path}')
	exit()


if 'evaluating' in sys.argv:

	def error(string_):
		print('Error: ' + string_)
		input('continue: ')


	def cmd(args):
		res = os.popen(f'./{push_swap_path} {args}').read()
		return (res)

	def cmd_check(args):
		return os.popen(f'./{push_swap_path} {args} | ./{checker_path} {args}').read().removesuffix('\n')

	def cmd_count(args):
		return len(cmd(args).split('\n')) - 1


	def cmd_error(args):
		res = cmd(args)
		if res != "Error\n":
			error(f"with {args} we must have an \"Error\" msg, we have '{res}'")
		else:
			print("\tOK")

	def cmd_nothing_return(args):
		if cmd(args):
			error(f"your program should return nothing - {args}")
		else:
			print("\tOK")

	def cmd_parsing(args):
		if cmd(args) == "Error\n":
			error(f"Parsing error - {args}")
		else:
			print("\tOK")


	def cmd_all_n(n):
		all = []

		def rec(tab, index=0):
			if index >= n:
				if len(set(tab)) == n:
					all.append(' '.join(str(k) for k in tab))
				return
			for i in range(n):
				tab[index] = i
				rec(tab, index + 1)
		
		res = [-1] * n
		rec(res)
		for args in all:
			check = cmd_check(args)
			if check == "KO":
				error(f"\tKO don't sort {args}")
				break
			ct = cmd_count(args)
			if (n == 5 and ct > 12):
				error(f"\tKO you sort in more than 12 instructions - {args}")
			elif (n == 3 and ct > 3):
				error(f"\tKO you sort in more than 3 instructions - {args}")
			elif all.index(args) % 20 == 0 or n == 3:
				print("\tOK")

	def cmd_100(max_pt):
		args = ' '.join([str(i) for i in random.sample(range(int_min, int_max), k=100)])
		check = cmd_check(args)
		if check == "KO":
			error(f"\tKO: don't sort {args}")
			return (100)
		else:
			ct = cmd_count(args)
			pts = {700: 5, 900: 4, 1100: 3, 1300: 2, 1500: 1}
			pt = 0
			for i in pts:
				if ct < i:
					pt = pts[i]
					break
			if pt < max_pt:
				print(f"\tOK sort in {ct} - {pt} pts")
			return pt

	def cmd_500(max_pt):
		args = ' '.join([str(i) for i in random.sample(range(int_min, int_max), k=500)])
		check = cmd_check(args)
		if check == "KO":
			error(f"\tKO don't sort {args}")
			return (100)
		else:
			ct = cmd_count(args)
			pts = {5500: 5, 7000: 4, 8500: 3, 10000: 2, 11500: 1}
			pt = 0
			for i in pts:
				if ct < i:
					pt = pts[i]
					break
			if pt < max_pt:
				print(f"\tOK sort in {ct} - {pt} pts")
			return pt


	print("Error management:")

	print("  Non numeric")
	cmd_error("559 3 sdf9")
	cmd_error("5hj 45 6 4")
	cmd_error("5 45 6hj 4")
	cmd_error("5 45 6 4 a")
	cmd_error("5 45 48 s")
	cmd_error("69 425 one 1")
	cmd_error("5 4-5 6 58")
	cmd_error("2 45 6 -")
	cmd_error("2 - 6 3")
	cmd_error("- 6 3")

	print("\n  Duplicate args")
	cmd_error("2 6 3 6")
	cmd_error("6 6 3")
	cmd_error("3 6 3")
	cmd_error("1 6 8 4 2 3 1")

	print("\n  Max INT")
	cmd_error("1 2147483648 8 4 2 3")
	cmd_error("1 6 8 2147483649 2 3")
	cmd_error("1 6 -2147483649 4 2 3")
	cmd_error("-2147483649 1 6 8 4 2 3")

	print("\n  Nothing to return")
	cmd_nothing_return("")
	cmd_nothing_return("42")
	cmd_nothing_return("30")
	cmd_nothing_return("-5")
	cmd_nothing_return("0 1 2 3")
	cmd_nothing_return("-185 26 48 8546")
	cmd_nothing_return("0 1 2 3 4 5 6 7 8 9 10 11")
	cmd_nothing_return("-554949 -2549 -695 15 45948 545498")
	cmd_nothing_return("548 9898")
	cmd_nothing_return("1 2")

	print("\n  Parsing")
	cmd_error('""')
	cmd_parsing('"0 5 8 9"')
	cmd_parsing('"0 5 1 9 2"')
	cmd_parsing('"5 6 8 9"')
	cmd_parsing('"9 5 8 -1288"')

	cmd_parsing('"0 5 9" 8')
	cmd_parsing('0 5 1 "9 2"')
	cmd_parsing('"5" 6 8 9')
	cmd_parsing('"9 5" 8 -1288')

	print("\n\nSimple version:")

	print("\n  3 args")
	cmd_all_n(3)
	print("\n  5 args")
	cmd_all_n(5)

	print("\n\nMiddle version:")
	print("\n  100 random")
	max_pt = 100
	for i in range(100):
		max_pt = cmd_100(max_pt)

	print("\n  500 random")
	max_pt = 100
	for i in range(50):
		max_pt = cmd_500(max_pt)
else:
	args = ' '.join([str(i) for i in random.sample(range(int_min, int_max), k=length)])

	check = os.popen(f'./{push_swap_path} {args}| ./{checker_path} {args}').read().removesuffix('\n')
	commands = int(re.findall('\d+', os.popen(f'./push_swap {args}| wc -l').read())[0])

	print(f'{check} - len {length} in {commands} commands')
	if '-a' in sys.argv:
		print(f'ARGS = {args}')
