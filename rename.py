import os
import random


""" !!! This is for test purposes !!! """
def create_test_files(n, directory='.'):
    file_names = [f"file_{i}.txt" for i in range(0, n)]
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for name in file_names:
        with open(os.path.join(directory, name), 'w') as file:
            pass
    print(rf"Test files created at {str(os.getcwd())}\{path}")

def add_prefix(directory='.'):
    # Scan directory for files
    files = [ entry.name for entry in os.scandir(directory) if entry.is_file() ]

    # Shuffle files
    random.shuffle(files)

    # Count digit count based on number of files
    num_digits = len(str(len(files)))

    # Add prefix
    for i, filename in enumerate(files):
        prefix = f"{i:0{num_digits}d}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, f"{prefix}_{filename}"))
    print("Prefix added!")

def remove_prefix(directory='.'):
    files = [ entry.name for entry in os.scandir(directory) if entry.is_file() ]

    num_digits = len(str(len(files))) + 1 # Plus one for '_'

    for i,filename in enumerate(files):
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename[num_digits:]))
    print("Prefix removed!")

ascii_art=r"""
+=============================================================+
|  _____ _ _            ____                                  |
| |  ___(_) | ___      |  _ \ ___ _ __   __ _ _ __ ___   ___  |
| | |_  | | |/ _ \_____| |_) / _ \ '_ \ / _` | '_ ` _ \ / _ \ |
| |  _| | | |  __/_____|  _ <  __/ | | | (_| | | | | | |  __/ |
| |_|   |_|_|\___|     |_| \_\___|_| |_|\__,_|_| |_| |_|\___| |
|                                                             |
+=============================================================+

Note:
    Please put the script one directory above the targeted directory!
"""
print(ascii_art)
print()
print(r"[!!!] WATCH YOUR CASES AND INPUT CORRECTLY [!!!]")
while True:
    path = input("Enter directory name: ")
    if os.path.isdir(path):
        break

options=rf"""
Directory: {str(os.getcwd())}\{path}
Choose one options:
0. Create test files (directory='test')
1. Add Random Prefix
2. Remove Prefix
"""
print(options)
while True:
    choose = input("ID: ")
    if choose.isdigit() and (int(choose) >= 0 and int(choose) <=2):
        choose = int(choose)
        break

match choose:
    case 0:
        create_test_files(1001, 'test')
    case 1:
        add_prefix(path)
    case 2:
        remove_prefix(path)
