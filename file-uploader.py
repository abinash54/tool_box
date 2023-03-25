import os
import requests

    
    
if __name__ == '__main__':
    src = './'
    fileTypes = ['zip']
    url = 'http://127.0.0.1:3056/get_files'
    
    try:
        for filetype in fileTypes:
            for file in os.listdir(src):
                if os.path.isfile(file) and file.endswith(filetype):
                    r = requests.post(url, files={'zipfile': file});
                    if r.status_code == 200:
                        print(file)
                        print('Success')
                    else:
                        print(file)
                        print('failed')
        
    except Exception as e:
        print(e)
        
    finally:
        exit(1)
