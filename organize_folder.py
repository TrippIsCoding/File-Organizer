import os
import shutil
import time
import sys

if getattr(sys, 'frozen', False):
    folder_path = os.path.dirname(sys.executable)
else:
    folder_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder_path)

settings_path = os.path.join(folder_path, "settings.txt")

exclude = ('organize_folder.exe', 'organize_folder.py', 'settings.txt', 'history.log')
files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file)) and file not in exclude]

revert_files = False
use_misc = False

file_type = {}

with open(settings_path, 'r') as settings:
    match settings.readline().rstrip():
        case "Use_Revert: True":
            revert_files = True
        case _:
            revert_files = False
    
    match settings.readline().rstrip():
        case "Use_Misc: True":
            use_misc = True
        case _:
            use_misc = False

if revert_files == False:
    print("organizing files...")
    
    with open(settings_path, 'r') as settings:
        settings.readline()
        settings.readline()
        
        try:
            for setting in settings:
                category, extensions = setting.strip().split(':')
                extensions = tuple(ext.strip() for ext in extensions.split(','))
                info = {
                    category: extensions
                }
                file_type.update(info)
        except:
            settings.readline()

    for file in files:
        name, ext = os.path.splitext(file)
        is_misc = True

        for category, exentsion in file_type.items():
            if ext in exentsion:
                if not os.path.exists(f'{folder_path}/{category}'):
                    os.mkdir(f'{folder_path}/{category}')
            
                with open('history.log', 'a') as log:
                    log.write(f'{folder_path}/{file} -> {folder_path}/{category}/{file}\n')

                shutil.move(f'{folder_path}/{file}', f'{folder_path}/{category}')
                is_misc = False
    
        if is_misc is True and use_misc is True:
            if not os.path.exists(f'{folder_path}/Misc'):
                os.mkdir(f'{folder_path}/Misc')
        
            with open('history.log', 'a') as log:
                log.write(f'{folder_path}/{file} -> {folder_path}/Misc/{file}\n')

            shutil.move(f'{folder_path}/{file}', f'{folder_path}/Misc')
    print("Files organized!")
    time.sleep(3)

if revert_files == True and os.path.exists(f'{folder_path}/history.log'):
    print("Files reverting...")
    
    with open('history.log', 'r') as log:
        for paths in log.readlines():
            original_path, current_path = paths.strip().split('->')
            
            original_path = original_path.strip()
            current_path = current_path.strip()
            try:
                shutil.move(current_path, original_path)
            except:
                None
    os.remove(f'{folder_path}/history.log')
    print("Files reverted!")
    time.sleep(3)