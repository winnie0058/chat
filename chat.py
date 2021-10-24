import os


def read_file(filename):
	chat = []
	if os.path.isfile(filename):
		with open(filename, "r", encoding='UTF-8-sig') as f:
			for line in f:
				# if 'Allen' in line || 'Tom' in line:
				# 	tmp = line + ':'
				chat.append(line.strip())
	else:
		print('找不到檔案')

	return chat

def convert(chat):
	new = []
	person = None #python 用法
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person :
			new.append(person + ':' + line)
	# print(new)
	return new

def write_file(chat, outputfile):
	with open (outputfile, 'w', encoding='UTF-8-sig') as f:
		for line in chat:
			f.write(line + '\n')


def main():
	chat = read_file('input.txt')
	# print(chat)
	chat = convert(chat)
	write_file(chat, 'output.txt')

main()