import os
from zipfile import ZipFile
import argparse, sys

if __name__=='__main__':
        
    srcLocation = './test_files'
    fileTypes = ['mp3', 'mp4']
    outputLocation ='./op'
    batchSize = 3
    # scanning the directory path
    count = 1
    try:
        for filetype in fileTypes:
            batchSizeCounter = 0
            zipper = ZipFile(outputLocation+'/zip_'+ str(count)+'.zip', 'w')
            for file in os.listdir(srcLocation):
                if batchSizeCounter == batchSize:
                    batchSizeCounter = 0
                    zipper.close()
                    count+=1
                    zipper = ZipFile(outputLocation+'/zip_'+ str(count)+'.zip', 'w')
                if os.path.isfile(os.path.join(srcLocation, file)) and file.endswith(filetype):
                    zipper.write(srcLocation+'/'+file, file)
                    batchSizeCounter += 1
                    
            zipper.close()
            count+=1
                            
    except FileNotFoundError as e:
        print(e)
        print('file error')
        exit(1)
        
    except Exception as e:
        print(e)
        exit(1)
        
    finally:
        exit(1)
                        
            
    