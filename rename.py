import os
import random

def create_test_files(n, directory='.'):
    file_names = [f"file_{i}.txt" for i in range(0, n)]
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for name in file_names:
        with open(os.path.join(directory, name), 'w') as file:
            pass

def add_prefix(directory='.'):
    # Scan directory for files
    files = [ entry.name for entry in os.scandir(directory) if entry.is_file() ]

    # Shuffle files
    random.shuffle(files)

    # Add prefix 
    num_digits = len(str(len(files)))
    for i, filename in enumerate(files):
        prefix = f"{i:0{num_digits}d}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, f"{prefix}_{filename}"))
    print("Prefix added!")

def remove_prefix(directory='.'):
    pass


create_test_files(1001, 'test')
add_prefix('test')

