

if __name__ == "__main__":
	tinggi = int(input('masukkan tinggi: '))
	
	for x in range(tinggi, 0, -1):
		for y in range(1, x+1):
			
			print('*', end='')
		print()
		
	print('selesai')
