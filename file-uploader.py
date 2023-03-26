import os
import requests
import traceback

    
    
if __name__ == '__main__':
	src = '.'
	fileTypes = ['zip']
	url = 'http://127.0.0.1:6002/image_handler/api/save_multiple_patient_files/'
	print('initiating...\n')
	try:
		for filetype in fileTypes:
			for file in os.listdir(src):
				if os.path.isfile(file) and file.endswith(filetype):
					# generating file
					fileContent = open(src+'/'+file, 'rb')
					# sending file
					r = requests.post(url, files={'zipfile':fileContent})
								
					if r.status_code == 200:
						print(file)
						print('Success')
					else:
						print(file)
						print(r.status_code)
						print('failed')
					
					print('\n')
					fileContent.close()
		
		exit(1)
        
	except Exception as e:
		print(traceback.format_exc())
		
	finally:
		exit(1)
