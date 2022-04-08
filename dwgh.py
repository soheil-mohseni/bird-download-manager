#! usr/bin/python
import requests

enter = str(input('لینک دانلود خود را وارد کنید'))
page=requests.get(enter)
file= page.content
name = str(input('نام فایل همراه با فرمت آن را به انگلیسی وارد نمایید'))
with open(name,'wb')as f:
    f.write(file)
