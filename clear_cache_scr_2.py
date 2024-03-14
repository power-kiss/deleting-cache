
import os
import shutil
import glob

def remove_folders(path, folders):
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            print(f"Удаление папки {folder_path}")
            shutil.rmtree(folder_path)

userspath = 'c:\\users'

for username in os.listdir(userspath):
    userfolder = os.path.join(userspath, username)
    versionfolders = glob.glob(os.path.join(userfolder, 'appdata', '*', '1c', '*'))

    for versionfolder in versionfolders:
        for subfolder in os.listdir(versionfolder):
            subfolderpath = os.path.join(versionfolder, subfolder)
            cachefolders = glob.glob(os.path.join(subfolderpath, 'vrs-cache/*'))

            remove_folders(subfolderpath, cachefolders)
            remove_folders(subfolderpath, ['config', 'configsave', 'dbnamecache', 'sicache'])

            # print(f"Удаление папки версии {versionfolder}")
            # shutil.rmtree(versionfolder)

            
           
# # """
# # Функция remove_folders берет путь и список папок для удаления, и выполняет удаление этих папок, если они существуют. 
# # В основном цикле мы вызываем эту функцию дважды - первый раз для удаления vrs-cache* папок, а второй раз для удаления config, configsave, dbnamecache и sicache папок.
# # """
