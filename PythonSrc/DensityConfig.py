import sys
import os
import glob
import time

FolderName = sys.argv[1]
CfgFile = 'Cfg.tmp'

os.chdir(FolderName)

CurrentFiles = glob.glob('*.csv')
print "\n//////////////////////////\nSelect File to work on:\n\n"
for kat in range(len(CurrentFiles)):
    print  str(kat) + " : " + CurrentFiles[kat]

WorkFolderNum = raw_input("Enter File to process (i.e. 4):  ")

FileName = CurrentFiles[int(WorkFolderNum)]

while os.path.exists(CfgFile):
    print 'Configuration file already present \n waiting for clean up ....\n'
    time.sleep(5)


f = open(CfgFile, 'w')
f.write(FileName)
f.close()


