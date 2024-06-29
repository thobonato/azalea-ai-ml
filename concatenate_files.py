import os

def concatenate_files(source_dir, output_file, extensions):
    files_found = 0
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(source_dir):
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
    if files_found == 0:
        print(f'No files with extensions {extensions} found in {source_dir}')
    else:
        print(f'All code files have been concatenated into {output_file}')

# Define the directory containing your code files and the output file name
source_directory = 'Azalea'  # Adjust the path as necessary
output_filename = 'combined_code.txt'
file_extensions = ('.py', '.js', '.txt')  # Extensions based on the provided structure

# Call the function to concatenate files
concatenate_files(source_directory, output_filename, file_extensions)
