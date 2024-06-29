import os

def concatenate_files(source_dirs, output_file, extensions, specific_files):
    files_found = 0
    with open(output_file, 'w') as outfile:
        for source_dir in source_dirs:
            for root, dirs, files in os.walk(source_dir):
                # Exclude the .venv directory
                dirs[:] = [d for d in dirs if d != '.venv']
                print(f'Checking directory: {root}')
                for file in files:
                    if file.endswith(extensions):
                        files_found += 1
                        file_path = os.path.join(root, file)
                        print(f'Reading file: {file_path}')
                        with open(file_path, 'r') as infile:
                            outfile.write(f'\n\n# Begin {file_path}\n')
                            outfile.write(infile.read())
                            outfile.write(f'\n# End {file_path}\n')
        for specific_file in specific_files:
            if os.path.isfile(specific_file):
                files_found += 1
                print(f'Reading file: {specific_file}')
                with open(specific_file, 'r') as infile:
                    outfile.write(f'\n\n# Begin {specific_file}\n')
                    outfile.write(infile.read())
                    outfile.write(f'\n# End {specific_file}\n')
    if files_found == 0:
        print(f'No files with extensions {extensions} found in specified directories and files.')
    else:
        print(f'All code files have been concatenated into {output_file}')

# Define the directories containing your code files and specific files to include
source_directories = [
    '/Users/thomazbonato/Desktop/Personal/Summer24/Coding/Azalea/backend',
    '/Users/thomazbonato/Desktop/Personal/Summer24/Coding/Azalea/frontend/src'
]
specific_files = [
]
output_filename = 'combined_code.txt'
file_extensions = ('.py', '.js', '.txt')  # Extensions based on the provided structure

# Call the function to concatenate files
concatenate_files(source_directories, output_filename, file_extensions, specific_files)
