import os
import sys
import time
import shutil
import argparse

# checks if you are running the .py or .exe of the script
if getattr(sys, 'frozen', False):
    folder_path = os.path.dirname(sys.executable)
else:
    folder_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder_path)

# file_type is so the organizer knows what categories the files with the corresponding extensions get moved to
file_type = {
    'Images': ('.jpg', '.png', '.gif'),
    'Documents': ('.pdf', '.docx', '.txt'),
    'Videos': ('.mp4', '.avi', '.mkv'),
    'Audio': ('.mp3', '.wav')
}

# exclude is a tuple with the names of files that shouldn't get moved
exclude = ('organize_files.exe', 'organize_files.py', 'history.log', 'README.md')

def get_files():
    '''get_files returns a list of files in the current folder path'''

    return [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file)) and file not in exclude]

def organize_files(files, use_misc, verbose):
    '''organize_files moves all files within the .py or .exe path to the corresponding category'''

    if not files:
        print("No file's detected, nothing to organize")
        return
    
    print("organizing files...")
    for file in files:
        name, ext = os.path.splitext(file)
        moved = False

        for category, extensions in file_type.items():
            if ext.lower() in extensions:
                dest_folder = category
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                
                try:
                    shutil.move(file, dest_folder)
                    if verbose:
                        print(f'{os.path.join(folder_path, file)} -> {os.path.join(folder_path, dest_folder, file)}')
                    with open('history.log', 'a') as log:
                        log.write(f'{os.path.join(folder_path, file)} -> {os.path.join(folder_path, dest_folder, file)}\n')
                    moved = True
                except Exception as e:
                    print(f'Error moving {file}: {e}')
                break
    
        if not moved and use_misc:
            if not os.path.exists('Misc'):
                os.mkdir('Misc')
        
            try:
                shutil.move(file, 'Misc')
                if verbose:
                    print(f'{os.path.join(folder_path, file)} -> {os.path.join(folder_path, "Misc", file)}')
                with open('history.log', 'a') as log:
                    log.write(f'{os.path.join(folder_path, file)} -> {os.path.join(folder_path, "Misc", file)}\n')
            except Exception as e:
                print(f'Error moving {file} to Misc: {e}')
    print('Files organized!')

def revert_files():
    '''revert_files moves all files inside history.log to their original location'''

    if not os.path.exists('history.log'):
        print('No history.log found-nothing to revert!')
        return
    
    print("Files reverting...")
    with open('history.log', 'r') as log:
        for line in log:
            original, current = line.strip().split(' -> ')
            try:
                shutil.move(current, original)
            except Exception as e:
                print(f'Error reverting {current}: {e}')
    os.remove('history.log')
    print("Files reverted!")

def main():
    parser = argparse.ArgumentParser(description='Organize files into category folders or revert them.')
    parser.add_argument('--revert', action='store_true', help='Revert files to their original location')
    parser.add_argument('--misc', action='store_true', help='Move uncategorized files into Misc folder')
    parser.add_argument('--verbose', action='store_true', help='Prints each file moved by the organizer')
    args = parser.parse_args()

    files = get_files()
    if args.revert:
        revert_files()
    else:
        organize_files(files, args.misc, args.verbose)
    time.sleep(2)

if __name__ == '__main__':
    main()
