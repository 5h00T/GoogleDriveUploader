import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def dfs(path,parent_id=None):
    print(path)
    if parent_id == None: #初回だけ
        folder_metadata = {'title' : os.path.split(path)[1],
                           'mimeType' : 'application/vnd.google-apps.folder'}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        parent_id = folder["id"]
    else:
        folder_metadata = {'title' : os.path.split(path)[1],
                           'mimeType' : 'application/vnd.google-apps.folder',
                           "parents": [{"kind": "drive#fileLink", "id": parent_id}]}
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
    
    for child in os.listdir(path):
        child_path = path + '/' + child
        if not os.path.isdir(child_path): 
            #ファイルの場合
            file = drive.CreateFile({'title' : os.path.split(child_path)[1],  
                                     "parents": [{"kind": "drive#fileLink", "id": folder["id"]}]})
            file.SetContentFile(filename=child_path)
            file.Upload()
            print(child_path)
        else:
            #フォルダの場合
            dfs(child_path,folder["id"])    # 再帰


if __name__=="__main__":
    if len(sys.argv) == 2:
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)
        dfs(sys.argv[1])
    else:
        print("引数は1個指定してください")
