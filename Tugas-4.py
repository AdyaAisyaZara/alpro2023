

if __name__ == "__main__":
	nilai =int(input('masukkan nilai: '))
	
	if nilai <= 85 and nilai > 70:
		print('A')		
	elif nilai <= 70 and nilai > 60:
		print('B')
	elif nilai <= 55 and nilai > 50:
		print('C')
	elif nilai <= 30 and nilai > 25:
		print('D')
	else:
		print('E')
		
	print('selesai')	
