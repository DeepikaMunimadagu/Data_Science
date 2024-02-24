import os
import shutil

path = r"C:/Users/Dell/Desktop/DREAM/PYTHON/"
folder_name = ['csv files', 'image files', 'python files', 'pdf files']
file_name = os.listdir(path)

for i in range(4):
    if not os.path.exists(path + folder_name[i]):
        print(path + folder_name[i])
        os.makedirs(path + folder_name[i])

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".py" in file and not os.path.exists(path + "python files/" + file):
        shutil.move(path + file, path + "python files/" + file)
