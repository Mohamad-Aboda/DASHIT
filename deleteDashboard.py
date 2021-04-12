import os
import shutil

def remove(username, name):
    with open('templates/' + username + '/includes/_dashboards.html', "r") as f:
        lines = f.readlines()
    with open('templates/' + username + '/includes/_dashboards.html', "w") as f:
        for line in lines:
            if line.strip("\n").__contains__('value="' + name + '"') == False:
                f.write(line)
    with open('templates/' + username + '/includes/_upload.html', "r") as f:
        lines = f.readlines()
    with open('templates/' + username + '/includes/_upload.html', "w") as f:
        for line in lines:
            if line.strip("\n").__contains__('value="upload_' + name + '"') == False:
                f.write(line)
    os.remove('templates/' + username + '/' + name + '.html')
    try:
        os.remove('templates/' + username + '/' + name + '.json')
    except:
        print('file doesn\'t exists')
    shutil.rmtree('CSV/' + username + '/' + name)