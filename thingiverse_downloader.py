# todo use pyautogui or whatever to automate the download button as well

#process: download to M:/DL then run this program, which extracts the folder, and copies only the files dir

import os
from pathlib import Path
import zipfile
from shutil import copy, move
#  import ntpath

models_path = Path('M:\OneDrive - University of Waterloo\Documents\modelling\download')
downloads_path = Path('M:\Files\DL')

def newest(path):
    files = [file for file in os.listdir(path)
             if os.path.splitext(file)[1].lower()
                in ('.zip', '.ZIP', '.stl', '.STL')]
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

newest = newest(downloads_path)
path, ext = os.path.splitext(newest)
file = os.path.basename(path)

print(f'path: {path}')
print(f'file: {file}')

try:
    os.mkdir(models_path/file)
except:
    print(f'found existing dir {models_path/file}')

if ext.lower() == '.stl':
    filebase = os.path.basename(newest)
    print(f'models_path/file: {models_path/file}')
    print(f'models_path/file/filebase: {models_path/file/filebase}')
    copy(newest, models_path/file/filebase)
else:
    with zipfile.ZipFile(newest) as zf:
        for i in zf.namelist():
            if i.startswith('files/'):
                zf.extract(i, path=models_path/file)

    for i in os.listdir(models_path/file/'files'):
        move(models_path/file/'files'/i, models_path/file/i)

    os.rmdir(models_path/file/'files')

#  print(newest)

