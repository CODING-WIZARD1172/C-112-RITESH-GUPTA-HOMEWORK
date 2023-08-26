import os
import shutil

# os.mkdir('C:/Users/Sec55/Desktop/fileOrganiser/IMAGES')
# os.mkdir('C:/Users/Sec55/Desktop/fileOrganiser/VIDEOS')
# os.mkdir('C:/Users/Sec55/Desktop/fileOrganiser/DOCUMENTS')
# os.mkdir('C:/Users/Sec55/Desktop/fileOrganiser/SETUP')
# os.mkdir('C:/Users/Sec55/Desktop/fileOrganiser/MISCELLANEOUS-2')


inidir = 'c:/Users/Sec55/Downloads'
fileList = os.listdir(inidir)


for files in fileList:
    # print(files)
    root, extension = os.path.splitext(files)
    path1 = inidir + '/' + files
    ext = extension.lower()

    try:
        if ext == '':
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/MISCELLNEOUS-2'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)
        if ext in ['.png', '.gif', '.jpg', '.jpeg', '.jfif']:
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/IMAGES'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)

        if ext in ['.mp3', '.vid']:
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/VIDEOS'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)

        if ext in ['.exe']:
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/SETUP'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)

        if ext in ['.pdf', '.docs']:
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/DOCUMENTS'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)
        else:
            fdir = 'c:/Users/Sec55/Desktop/fileOrganiser/MISCELLANEOUS-1'
            path2 = fdir + '/' + files
            shutil.move(path1, path2)

    except:
        continue
