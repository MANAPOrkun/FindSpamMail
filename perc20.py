import enum
import os, os.path
import shutil

# This file creates test data from 20% of the all data.


path_spam = 'Path of Spam Files'
path_nonspam = 'Path of Non Spam Files'

path_spam20 = 'Path of New Folder for 20% Spams'
path_nonspam20 = 'Path of New Folder for 20% Non Spams'

number_spam = len([name for name in os.listdir(path_spam) if os.path.isfile(os.path.join(path_spam, name))])
number_nonspam = len([name for name in os.listdir(path_nonspam) if os.path.isfile(os.path.join(path_nonspam, name))])

for i, j in enumerate(os.listdir(path_spam)):
    if number_spam / 5 > i:
        src = path_spam + '\\' + j
        dst =  path_spam20 + '\\' + j
        shutil.move(src, dst)

for i, j in enumerate(os.listdir(path_nonspam)):
    if number_nonspam / 5 > i:
        src = path_nonspam + '\\' + j
        dst =  path_nonspam20 + '\\' + j
        shutil.move(src, dst)