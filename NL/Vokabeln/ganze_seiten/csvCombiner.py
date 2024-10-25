import csv
import os
import glob
import re
import pandas as pd

def getIntFromString(s):
    return int(re.findall(r'\d+',s)[0])


def appendFilesToOne(file_names, combined_file_name):
    # Delete the combined file if it ( or an old one ) already exists
    for f in glob.glob("seite_*_bis_*.csv"):
        print("Deleting old file {}".format(f))
        os.remove(f)



    file_names = [file for file in file_names if file != combined_file_name]

    print("Trying to append {} files from {} to {} into {}".format(len(file_names),
                                                                   file_names[0],
                                                                   file_names[len(file_names)-1],
                                                                    combined_file_name))
    lines_written = 0

    

    with open(combined_file_name,'w+') as combined_file:
        # iterate over all files in cwd
        for file in file_names:

            # open each file
            with open(file, 'r') as src_file:
                
                # read lines in file
                amount_lines = sum(1 for line in src_file)
                lines_written += amount_lines
                print("Opening file {} with {} lines...".format(src_file.name,amount_lines ))
                
                # reset file pointer because lines have been counted
                src_file.seek(0)

                # read lines and save in combined file
                content = src_file.read()
                combined_file.write(content)
        print("Wrote {} lines!".format(lines_written))


#folder_path = 'C:\\Daten\\Dokumente\\Abitur\\Anki\\NL\\Vokabeln\\ganze_seiten'
folder_path = os.getcwd()
extension = 'csv'
os.chdir(folder_path)

all_files = glob.glob('*.{}'.format(extension))
amount_files = len(all_files)
if amount_files <= 0:
    print(all_files)
    print("No {} files provided in current working dir {}! ".format(extension,folder_path))
    print("Be sure that you are in the correct directory!!!")
    print("Exiting...")
    exit(-1)

combined_fname = "seite_{}_bis_{}.{}".format(getIntFromString(all_files[0]), 
                                         getIntFromString(all_files[amount_files-1]), extension
                                         )


print("Combining all .{} files in dir {}".format(extension,folder_path))

appendFilesToOne(all_files, combined_fname)
print("Summarized file will be saved under {}".format(combined_fname))





