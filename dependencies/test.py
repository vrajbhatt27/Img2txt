import os
import time
import sys


imgPath = os.path.join(os.getcwd(), 'pics')
txtPath = os.path.join(os.getcwd(), 'txt_files')
totImg = len(os.listdir(imgPath))
totFiles = 0

time.sleep(5)

while True:
    l = len(os.listdir(txtPath))
    totFiles = l
    print('Files Converted: ', l)
    time.sleep(5)

    if totFiles == totImg:
        print('Done')
        sys.exit(0)
