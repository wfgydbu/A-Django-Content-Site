import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings") 

import django
django.setup()

import hashlib

from sticker.models import Category, Sticker

dirname = '复仇者联盟'
c = Category(name=dirname)
c.save()

file_dir = r"D:\OneDrive\Documents\Python和数据挖掘\code\baidutieba\Download\asd2"

for file in os.listdir(file_dir): 
    with open(file_dir+'\\'+file, 'r', encoding='utf-8') as file:
        title  = file.readline().split(':')[1].strip()
        author = file.readline().split(':')[1].strip()

        content = file.read().strip()

        m = hashlib.md5()
        m.update(content.encode('utf-8'))
        md5 = m.hexdigest()

    Sticker.objects.create(title = title,
                       author = author,
                        content = content,
                        category = c,
                        md5 = md5
                        )    
