import hashlib
import sys


def main(typ, msg):
	if typ == 1:
		sha = hashlib.sha1(message)
		sha1 = sha.hexdigest()
		return sha1
	elif typ == 2:
		sha = hashlib.sha128(message)
		sha1 = sha.hexdigest()
		return sha1
	elif typ == 3:
		sha = hashlib.sha256(message)
		sha1 = sha.hexdigest()
		return sha1
	else:
		return 'Error!'

def start():
	print "Hello, welcome to string encryption script! :)\n"
	type = raw_input("Type: 1 --> SHA1, 2 --> SHA128, 3 --> SHA256: ")
	message = raw_input("Enter the string you want to hash: ")
	return int(type), message

if __name__ == '__main__':
	type, message = start()
	print main(type, message)
	
