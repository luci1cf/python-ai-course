# Import
#---------------------------------------------------------------------------
import os
import shutil
from pathlib import Path

# Global Variables
#---------------------------------------------------------------------------
# PATH_DOWNLOADS = r'C:\Users\fluci\Downloads' # Dev/Local
PATH_DOWNLOADS = Path.home() / 'Downloads'     # Universal

# Define Sorting Rules
#---------------------------------------------------------------------------
CATEGORIES = {
    '_Invoices'     : ['invoice', 'receipt', 'rechnung'],
    '_Images'       : ['.jpg', '.jpeg', '.png'],
    '_GIF'          : ['.gif'],
    '_Videos'       : ['.mp4', '.mkv', '.avi', '.mov'],
    '_Docs'         : ['.pdf', '.docx', '.txt'],
    '_ZIPs'         : ['.zip', '.rar', '.7z'],
    '_Installers'   : ['.exe', '.msi'],
    '_Code'         : ['.py', '.js', '.html', '.css', '.md'],
    '_Data'         : ['.csv', '.xlsx'],
    '_Design'       : ['.fig', '.psd', '.svg'],
    '_Subtitles'    : ['.vtt']
}

# Functions
#-----------------------------------
def get_file_cat(filename):
    """ Find sorting folder by name
     :param filename: filename inside of Downloads Folder
     :return:         name of sorting folder
    """
    # Ignore Sorting Folders
    if filename.startswith('_'):
        return None

    # Folder
    filepath = os.path.join(PATH_DOWNLOADS, filename)
    if os.path.isdir(filepath):
        return '_Folder'

    # File
    else:
        # Option A - For File Extensions
        # # Looking for Category
        # for cat, list_keywords in CATEGORIES.items():
        #     if file_extension.lower() in list_keywords:
        #         return cat

        file_extension = '.' + filename.split('.')[-1]
        for cat, list_keywords in CATEGORIES.items():
            for keyword in list_keywords:
                if keyword.lower() in filename.lower():
                    return cat

        print(f'{file_extension} not supported. File ({filename})')
        return '_Others'

# Read All Files
#---------------------------------------------------------------------------
def sort_downloads():
    # Placeholders
    count, fails    = 0,0
    failed_msgs     = []

    all_files   = os.listdir(PATH_DOWNLOADS)
    folders     = [f for f in all_files if os.path.isdir(os.path.join(PATH_DOWNLOADS, f)) and not f.startswith('_')]
    files       = [f for f in all_files if not os.path.isdir(os.path.join(PATH_DOWNLOADS, f))]

    # Report to Console
    print('-'*40)
    print('Scanning Downloads Folder...')
    print(f'Folders found: {len(folders)}')

    if files:
        print(f'Files found: {len(files)}')
        print('-'*40)
        print('Sorting:')

    else:
        print('No Files Found')
        print('\nNothing to sort.')


    for file in os.listdir(PATH_DOWNLOADS):
        # Get File Category (based on rules)
        dir_name = get_file_cat(file)
        # print(cat, file)

        if dir_name:
            # Create Sorting Folders
            dir_filepath = os.path.join(PATH_DOWNLOADS, dir_name)
            if not os.path.exists(dir_filepath):
                os.makedirs(dir_filepath)

            # Define Old/New Paths
            old_path = PATH_DOWNLOADS / file
            new_path = os.path.join(PATH_DOWNLOADS, dir_name, file)

            # Move Files
            try:
                shutil.move(old_path, new_path)
                print(f'{dir_name} / {file}')
                count += 1

            except Exception as e:
                failed_msgs.append(f'{dir_name} / {file} - {e}')
                fails += 1

    if count:
        print(f'\nSuccessfully sorted {count} files.')

    if fails:
        print('-'*40)
        print(f'Failed to sort {fails} files.')
        for msg in failed_msgs:
            print(msg)

sort_downloads()