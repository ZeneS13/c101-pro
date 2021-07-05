import dropbox
import os
from dropbox.files import WriteMode

class TransferData: 
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self, file_from,file_to):
        dbx = dropbox.Dropbox(self.acceess_token)
        

    for root, dirs, files in os.walk(file_from):

        for filename in files:

            local_path = os.path.join(root, filename)

        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = oss.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), fropbox_path, mode= WriteMode('overwrite')) 

def main():
    access_token = 'sl.AziYXj9IHB2CH4yRt88pDxV-Atlm_ceHdQMrapeUQDFkGJGQY8M5firhoEYyAEwpSt7O2_n7KRtSfFwyONd28_0KEBGC18SMu-6vErZ5sZq4GCD8ezRe1Af2DYDVo8pCZhVSqcg'
    transferData= TransferData(access_token)

    file_from= input("Enter the file path to transfer: ")
    file_to = input("enter the file path to upload: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")


main() 