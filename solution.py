import glob
import os.path

def find_files(files, string):
	files_with_string = []
	for file in files:
		with open(file, 'r') as new_file:
			if new_file.read().find(string)>=0:
				files_with_string.append(file)
	return files_with_string

print('python3 find_procedure.py')

migrations = 'Migrations'
sql_files = glob.glob(os.path.join(migrations, "*.sql"))

while True:
	string = input('Введите строку: ')
	sql_files = find_files(sql_files, string)
	
	if len(sql_files) < 5:
		for sql_file in sql_files:
			print(sql_file)
	else:
		print('... большой список файлов ...')
		
	print('Всего:', len(sql_files))	
