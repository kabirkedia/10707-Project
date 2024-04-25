import os
import glob

def concatenate_files(folder_path, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in glob.glob(os.path.join(folder_path, '*')):
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())

# Example usage
folder_path = 'ghazals_hi'
output_file = 'output_file.txt'
concatenate_files(folder_path, output_file)

