def decode(enc):
	print(bytes.fromhex(enc).decode('utf-8'))

if __name__=='__main__':
	with open('./ch8.txt') as f:
		enc_str = f.readline().rstrip()
	decode(enc_str)