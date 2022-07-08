#%%

import urllib.request
import os


dir_name = "./img"                
if not os.path.exists(dir_name):   # img 폴더가 없으면 새로 만들기  
    os.mkdir(dir_name)

for i in range(99, 1000):
    
    if i < 9:
        page = f"000{i+1}"
    elif i < 99:
        page = f"00{i+1}"
    else:
        page = f"0{i+1}"

    img_path = f"https://ia802308.us.archive.org/BookReader/BookReaderImages.php?zip=/33/items/dragon-quest-xi-echoes-of-the-elusive-age-definitive-edition-gamer-guide/Dragon%20Quest%20XI%20Echoes%20of%20The%20Elusive%20Age%20Definitive%20Edition%20Gamer%20Guide_jp2.zip&file=Dragon%20Quest%20XI%20Echoes%20of%20The%20Elusive%20Age%20Definitive%20Edition%20Gamer%20Guide_jp2/Dragon%20Quest%20XI%20Echoes%20of%20The%20Elusive%20Age%20Definitive%20Edition%20Gamer%20Guide_{page}.jp2&id=dragon-quest-xi-echoes-of-the-elusive-age-definitive-edition-gamer-guide&scale=2&rotate=0"
    

    file_name = f'{i+1}.jpg'
    print(file_name)

    urllib.request.urlretrieve(img_path, dir_name + "/" + file_name)

# %%
import glob
import natsort
files = glob.glob("./img/*.jpg")

files = natsort.natsorted(files)

#%%# 화면캡처 파일 -> 각각의 pdf 파일로 저장
import img2pdf
from PyPDF2 import PdfFileWriter, PdfFileReader

dir_name = "./pdf"                
if not os.path.exists(dir_name):   # img 폴더가 없으면 새로 만들기  
    os.mkdir(dir_name)

for i in range(len(files)):
    #file_name2 = f'{i+1}.png'
    #file_name = capture_dir +"\\"+ file_name2
    #print(file_name)
    
    ImgFile = open(files[i], "rb")
    PdfFile = open(dir_name +"\\"+ f"output_{i+1}.pdf", "wb")
    
    PdfFile.write(img2pdf.convert(ImgFile))
    ImgFile.close()
    PdfFile.close()
#%%

#  각각의 pdf 파일  -> 하나의 pdf 파일로 저장
pdf_writer = PdfFileWriter()
for i in range(len(files)):
    file_name2 = f'output_{i+1}.pdf'
    file_name = dir_name +"\\"+ file_name2
    print(file_name)

    pdf_reader = PdfFileReader(file_name)

    for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
#%%
with open(f"result.pdf", 'wb') as fh:
    pdf_writer.write(fh)

# %%
