import os

#清單的分割
# n = [2, 6, 6, 8, 4]
# 1. 前三個 n[:3] ( = 0:3) = [2, 6, 6]
# 2. 中間2-4個 [2:4] = [6, 8]
# 3. 結尾 n[-2:] = [8, 4]

def read_file(filename):
	chats = []
	if os.path.isfile(filename):
		with open(filename, "r", encoding='UTF-8-sig') as f:
			for line in f:
				chats.append(line.strip())
				# chats.append(line.strip().split(' '))
	else:
		print('找不到檔案')

	# print(chats)
	return chats

def convert(chats):
	new = []
	person = None #python 用法
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0

	for line in chats:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count +=1
			elif s[2] == '圖片':
				allen_image_count +=1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count +=1
			elif s[2] == '圖片':
				viki_image_count +=1
			else:
				for m in s[2]:
					viki_word_count += len(m)
			# print(s[2:])
		# print(s)
	print('Allen 說了', allen_word_count, '個字')
	print('Allen 傳了', allen_sticker_count,'個貼圖')
	print('Allen 傳了', allen_image_count,'個圖片')
	print('Viki 說了', viki_word_count, '個字')
	print('Viki 傳了', viki_sticker_count,'個貼圖')
	print('Viki 傳了', viki_image_count,'個圖片')
	return new

def write_file(chat, outputfile):
	with open (outputfile, 'w', encoding='UTF-8-sig') as f:
		for line in chat:
			f.write(line + '\n')


def main():
	chats = read_file('LINE-Viki.txt')
	chats = convert(chats)
	# write_file(chat, 'output.txt')

main()