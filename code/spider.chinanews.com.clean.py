# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:38:38 2020

@author: Zhenlin
"""

#清理乱码新闻

import os
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read('../config.ini', 'utf-8')

folder=config['DEFAULT']['doc_dir_path']

files=os.listdir(folder)

files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))

keyword='编辑'

i=1
for j,file in enumerate(files):
    print('%d/%d'%(j,len(files)))
    path='%s\%s'%(folder,file)

    tree =  ET.parse(path)
    root = tree.getroot()
    body = root.find('body').text
    docid = root.find('id')
    if keyword in body:
        docid.text = str(i)
        tree.write('%s\%d.xml'%(folder,i), encoding=config['DEFAULT']['doc_encoding'])
        i+=1
    else:
        os.remove(path)
        
print('# valid files = %d'%(i-1))