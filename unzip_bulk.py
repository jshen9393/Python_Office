import zipfile
import glob

# Bulk unzip program.  Works from one file directory to export all zip files into one file directory

file_names = glob.glob("H:\unzip\*.zip") # name of source folder, isolate .zip files
for x in file_names: # loop to unzip file to destination one zip file at a time.
  zip = zipfile.ZipFile(x)
	zip.extractall(r'H:\unzip\xml_files') #destination folder

print "extract completed" #validate program is complete
