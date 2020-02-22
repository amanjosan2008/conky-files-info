#!/usr/bin/python3
#Initial File Count / Current File Count
#Sub directory size wise
#Top Dirs in count wise
#Bottom Dirs in count wise

import os
from datetime import datetime

path="/data/.folder/"

file_list =[]
data_list =[]
drive_list=[]
other_list=[]

for root,dirc,fname in os.walk(path):
    for f in fname:
        file_name = os.path.join(root, f)
        file_list.append(file_name)
        if "/data/.folder/DATA" in file_name:
            data_list.append(os.path.join(root, f))
        elif "/data/.folder/Drive" in file_name:
            drive_list.append(file_name)
        else:
            other_list.append(file_name)

def type(list_name,ext):
    l = [f for f in list_name if ext in f]
    return len(l)

def top(path):
        p = 1
        x = {}
        for filen in path:
            p += 1
            filesize = (os.path.getsize(filen))
            #relfile = os.path.relpath(filen, '/data/.folder/')
            x.update({filen.split('/')[-1]: filesize})
        # Limit iterations to 10 or less in case lesser no of files
        if (len(x) < 5):
            a = len(x)
        else:
            a = 5
        for i in range(a):
            key, value = max(x.items(), key = lambda p: p[1])
            sizeinmb = (value/1000000)
            sizeflt = "{:.0f}".format(sizeinmb)
            print(sizeflt+" MB  " + key[:40].ljust(44))
            x.pop((max(x, key=x.get)))

size_total = os.popen('du -sh /data/.folder/').read().split()[0]
size_data = os.popen('du -sh /data/.folder/DATA').read().split()[0]
size_drive = os.popen('du -sh /data/.folder/Drive').read().split()[0]
size_others = str(int(size_total.strip('G')) - (int(size_data.strip('G')) + int(size_drive.strip('G'))))


print("Total Files:     ", len(file_list),'('+size_total+')')
print("Files in Data:   ", len(data_list),'('+size_data+')')
print("Files in Others: ", len(other_list),'('+size_others+'G)')
print("Files in Drive:  ", len(drive_list),' ('+size_drive+')\n')

file_type = [".jpg",".png",".jpeg",".gif",".mp4",".flv",".avi",".mpg",".3gp",".dat"]

print('Type:\t\t All:\t Data:\t Other:\tDrive:')
for i in file_type:
    print((i.strip('.')).upper(), '\t\t', type(file_list, i), '\t', type(data_list, i), '\t', type(other_list, i), '\t', type(drive_list, i))

#print('\nBiggest files:')
#top(file_list)

print('\nBiggest files in DATA:')
top(data_list)

#print('\nBiggest files in Drive:')
#top(drive_list)

print('\nBiggest files in Others:')
top(other_list)


print('\nBiggest Dir:')
print(os.popen('find /data/.folder/DATA -type f -exec dirname {} \; | sort | uniq -c | sort -nr | head -n 5').read())
print('Smallest Dir:')
print(os.popen('find /data/.folder/DATA -type f -exec dirname {} \; | sort | uniq -c | sort -nr | tail -n 5').read())

now = datetime.now()
time = now.strftime("%H:%M")

print("Last Fetch:", time)
