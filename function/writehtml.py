import base64
import re
def readimg(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    image_base64 = str(base64.b64encode(data), encoding='utf-8')
    return image_base64


def readtxt(txt_path):
    file = open(txt_path)
    keyStart = '"data:image/png;base64,'
    keyEnd = '" width'
    buff = file.read()
    pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
    result = str(pat.findall(buff)).strip('[]').strip('\'')
    file.close()
    return result

def writehtml(txt_path,imgpath):
    base64date = readimg(imgpath)
    old_text =readtxt(txt_path)
    with open(txt_path, 'r') as f:
        text = base64date
        file_data = ""
        for line in f:
            line = line.replace(old_text, text)
            file_data += line
    with open(txt_path, "w") as f:
        f.write(file_data)
        f.close()



if __name__ == "__main__":
     writehtml('E:/img.txt','E:/screenshot.png')