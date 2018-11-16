'''
将pdf转化成txt
本工具所需包： padminer3k  
环境： Python3


使用方法：   
            python pdf2txt  文件名.pdf

            python pdf2txt  文件名.pdf  文件名.txt

'''

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import sys

def writeFile(PATH,str):
    f = open (PATH,'w',encoding='utf-8')
    f.write(str)
    f.close()

def PDFreader(pdfPATH,TXTname = ""):
    #获取文档对象
    fp = open(pdfPATH, "rb")
    #创建一个一个与文档关联的解释器
    parser = PDFParser(fp)
    #PDF文档的对象
    doc = PDFDocument()
    #连接解释器和文档对象
    parser.set_document(doc)
    doc.set_parser(parser)
    #初始化文档,当前文档没有密码，设为空字符串
    doc.initialize("")
    #创建PDF资源管理器
    resource = PDFResourceManager()
    #参数分析器
    laparam = LAParams()
    #创建一个聚合器
    device = PDFPageAggregator(resource, laparams=laparam)
    #创建PDF页面解释器
    interpreter = PDFPageInterpreter(resource, device)
    #使用文档对象得到页面的集合

    list=[]
    for page in doc.get_pages():
        # 使用页面解释器读取
        interpreter.process_page(page)
        # 使用聚合器来获得内容
        layout = device.get_result()
        for out in layout:
            if hasattr(out, "get_text"):
                str = out.get_text()
                list.append(str)
                print(str)
    TXTstr = "\n".join(list)
    if TXTname == "":
        TXTname = pdfPATH.replace(".pdf",".txt")
    writeFile(TXTname,TXTstr)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2 :
            PDFreader(sys.argv[1],"")
        elif len(sys.argv) == 3:
            PDFreader(sys.argv[1],sys.argv[2])
        else:
            print("参数错误")
    except:
        print("PDF解析出错")