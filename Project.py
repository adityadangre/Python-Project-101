import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFolder(self, source, destination):
        dbx = dropbox.Dropbox(self.access_token)
        print("[Success] dropbox account linked")
        c=0

        if os.path.exists(source):
            for root, dirs, files in os.walk(source):
                for name in files:
                    file_path=os.path.join(root,  name)
                    relative_path = os.path.relpath(file_path, root)
                    relative_path1= os.path.relpath(file_path, source)
                    if(relative_path==relative_path1):
                        dropbox_path = os.path.join(destination, relative_path)                        
                    else:
                        dropbox_path = destination + name                        
                    
                    with open(file_path, 'rb') as f:
                        dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))                        
                        
                    print(file_path,dropbox_path)
                    c=c+1
                                    
        else: 
            print("Path not exist") 

        print(f"{c} no. of files transfer into dropbox") 
              
     
def main():
    access_token = 'oafY2dCtfVsAAAAAAAAAAQNah8PZ-0Eb3vy7CETcT4QiEzbh3mJK13AaHaQy3NKq'
    transferData = TransferData(access_token)

    source = input('Enter the source file: ')
    destination = "/"

    transferData.uploadFolder(source, destination)
    print('Folder has successfully uploaded!!!')
    

if __name__ == '__main__':
    main()