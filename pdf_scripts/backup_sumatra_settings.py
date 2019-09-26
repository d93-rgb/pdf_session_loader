from shutil import copyfile
import  os, time, ntpath
import datetime

source_path  = "C:\\\\Users\\Dood\\AppData\\Roaming\\SumatraPDF\\SumatraPDF-settings.txt"
dest_path    = "C:\\Users\\Dood\\Documents\\Backup\\Sumatra\\"
file_name = os.path.splitext(ntpath.basename(source_path))[0]

backup_time = time.time()
#print(backup_time)
#print(file_name)

timestamp = (datetime.datetime.fromtimestamp(backup_time).strftime("_%y-%m-%d-%H_%M_%S"))
timestamp_log = datetime.datetime.fromtimestamp(backup_time).strftime("%c")

backup_path = dest_path + file_name + timestamp + ".txt"

#print(timestamp)
#print(backup_file)

copyfile(source_path, backup_path)

print("Created backup of SumatraPDF settings on {} at '{}'".format(timestamp_log, backup_path))