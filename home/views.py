from unittest import result
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from home.models import Description, Gifcon, Imagecon, Task, translan
from pathlib import Path,os
from PIL import Image, ImageDraw, ImageFont #dynamic import
BASE_DIR = Path(__file__).resolve().parent.parent
import sys 
import requests,cv2,io
sys.path.append('/usr/local/lib/python3.9/site-packages')
import pytesseract	
from PIL import Image	
import pyttsx3		
from googletrans import Translator


# Create your views here.
def home(request):
    context={'success':False,"frombrow":True}
    
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        img1=request.FILES.get('img1')
        print(title,desc,img1)
        ins=Task(taskTitle=title,taskDesc=desc,taskImage=img1)
        ins.save()
        context={'success':True}
        
    return render(request,'index.html',context)

def feature(request):
    context={'success':False,"frombrow":False}
    
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        img1=request.FILES.get('img1')
        print(title,desc,img1)
        ins=Task(taskTitle=title,taskDesc=desc,taskImage=img1)
        ins.save()
        context={'success':True}

    return render(request,'index.html',context)


def imgtrans(request) :
    context={'success':False}
    if request.method=="POST":
        img1=request.FILES.get('img1')
        # desc=request.POST['desc']
        ins= Imagecon(taskImage=img1)
        ins.save()
        context={'success':True}
        allTasks=Imagecon.objects.all()
        # print(allTasks)
        for item in allTasks:
            print(item.taskImage)
        # desc=request.POST['desc']
        langto=request.POST['langto']
        img1=str(item.taskImage)
        str1="media/"
        img1=str1+img1
        img = cv2.imread(img1)
        _, compressedimg = cv2.imencode(".jpg", img)
        file_bytes = io.BytesIO(compressedimg)

        url_api = "https://api.ocr.space/parse/image"
        response = requests.post(url_api, 
            files = {img1 : file_bytes}, 
            data = {"apikey" : "K85285375488957"})
        result = response.json()
        output = result["ParsedResults"][0]["ParsedText"]
        context={'tasks':output}
        
        # print(desc)
        # ins=translan(taskDesc=desc,taskLan=langto)
        # ins.save()
        # context={'success':True}
        p = Translator() 
        print("trn")   
        allTasks=Imagecon.objects.all()  
        for item in allTasks:
            print(item.taskImage)                

        # k = p.translate(output,dest=item.taskLan)  
        k = p.translate(output,langto)      
        print(k)
        context={'tasks':k.text}

    return render(request,'imgTrans.html',context)

def imgtospeech(request) :
    context={'success':False}
    if request.method=="POST":
        img1=request.FILES.get('img1')
        # desc=request.POST['desc']
        ins= Imagecon(taskImage=img1)
        ins.save()
        context={'success':True}
        allTasks=Imagecon.objects.all()
        # print(allTasks)
        for item in allTasks:
            print(item.taskImage)
        # desc=request.POST['desc']
        # langto=request.POST['langto']
        img1=str(item.taskImage)
        str1="media/"
        img1=str1+img1
        img = cv2.imread(img1)
        _, compressedimg = cv2.imencode(".jpg", img)
        file_bytes = io.BytesIO(compressedimg)

        url_api = "https://api.ocr.space/parse/image"
        response = requests.post(url_api, 
            files = {img1 : file_bytes}, 
            data = {"apikey" : "K85285375488957"})
        result = response.json()
        output = result["ParsedResults"][0]["ParsedText"]
        context={'tasks':output}
        with open('abc.txt',mode ='w') as file: 
            file.write(output)
            # print(item.taskDesc)    
        engine = pyttsx3.init()
        engine.say(output)            
        engine.runAndWait()
        
        # print(desc)
        # ins=translan(taskDesc=desc,taskLan=langto)
        # ins.save()
        # context={'success':True}
        p = Translator() 
        print("trn")   
        allTasks=Imagecon.objects.all()  
        for item in allTasks:
            print(item.taskImage) 

    return render(request,'imgToSpeech.html',context)

def tasks(request):
    allTasks=Imagecon.objects.all()
    # print(allTasks)
    for item in allTasks:
        print(item.taskImage)
    
    img = Image.open(item.taskImage)

    print(img)						
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    with open('abc.txt',mode ='w') as file:	
        file.write(result)
        print(result)
                    
    context={'tasks':result} 
    return render(request,'tasks.html',context)  





def imgApi(imgPath) :
    img = cv2.imread(imgPath)
    _, compressedimg = cv2.imencode(".jpg", img)
    file_bytes = io.BytesIO(compressedimg)

    url_api = "https://api.ocr.space/parse/image"
    response = requests.post(url_api, 
        files = {imgPath : file_bytes}, 
        data = {"apikey" : "K85285375488957"})
    result = response.json()
    output = result["ParsedResults"][0]["ParsedText"]

    return output



# imgpath = 'test1.jpg'

# result = imgApi(imgpath)
# print(result)


def imagec(request):
    context={'success':False}
    if request.method=="POST":
        img1=request.FILES.get('img1')
        
        ins= Imagecon(taskImage=img1)
        ins.save()
        context={'success':True}
        # img = Image.open(img1)
        




       
        # print(img)
        # print("img")
        print(img1)
        print("img1")
        # print(ins)
        # print("ins")
        allTasks=Imagecon.objects.all()
        # print(allTasks)
        for item in allTasks:
            print(item.taskImage)
        img1=str(item.taskImage)
        str1="media/"
        img1=str1+img1
        img = cv2.imread(img1)
        _, compressedimg = cv2.imencode(".jpg", img)
        file_bytes = io.BytesIO(compressedimg)

        url_api = "https://api.ocr.space/parse/image"
        response = requests.post(url_api, 
            files = {img1 : file_bytes}, 
            data = {"apikey" : "K85285375488957"})
        result = response.json()
        output = result["ParsedResults"][0]["ParsedText"]
        context={'tasks':output}
        return render(request,'tasks.html',context)
        # print(img)
        # print("imagec")						
        # pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
        # # converts the image to result and saves it into result variable
        # result = pytesseract.image_to_string(img)
        # with open('abc.txt',mode ='w') as file:	
        #     file.write(result)
        #     print(result)
                        
        # context={'tasks':result} 
        # return render(request,'tasks.html',context)

    return render(request,'imagec.html',context)  

def text_to_voice(request):
    context={'success':False}
    if request.method=="POST":
        desc=request.POST['desc']
        print(desc)
        ins=Description(taskDesc=desc)
        ins.save()
        context={'success':True}
        p = Translator() 
        print("trn")   
        allTasks=Description.objects.all()  

        for item in allTasks:
            print(item.taskDesc)

        with open('abc.txt',mode ='w') as file: 
            file.write(item.taskDesc)
            print(item.taskDesc)    
        engine = pyttsx3.init()
        engine.say(item.taskDesc)                             
        engine.runAndWait()
    return render(request,'text_to_voice.html',context)

def gif_to_text(request):
    context={'success':False}
    if request.method=="POST":
        img1=request.FILES.get('img1')
        print(img1)
        print("img")
        
        ins= Imagecon(taskImage=img1)
        ins.save()
        context={'success':True}
        # img = Image.open(img1)
        




       
        # print(img)
        # print("img")
        # print(img1)
        # print("img1")
        # print(ins)
        # print("ins")
        # allTasks=Imagecon.objects.all()
        # print(allTasks)
        # for item in allTasks:
        #     print(item.taskImage)
        # img1=str(item.taskImage)
        # str1="media/"
        # img1=str1+img1
        # img = cv2.imread(img1)
        # _, compressedimg = cv2.imencode(".jpg", img)
        # file_bytes = io.BytesIO(compressedimg)

        # url_api = "https://api.ocr.space/parse/image"
        # response = requests.post(url_api, 
        #     files = {img1 : file_bytes}, 
        #     data = {"apikey" : "K85285375488957"})
        # result = response.json()
        # output = result["ParsedResults"][0]["ParsedText"]
        # context={'tasks':output}
        # return render(request,'tasks.html',context)
        





        allTasks=Imagecon.objects.all()
        # print(allTasks)
        for item in allTasks:
            print(item.taskImage)
        # opening an image from the source path
        # img = Image.open(item.taskImage)	
        img1 = Image.open(item.taskImage)
        # result1 = ["Here are your results"]
        
        for frame in range(0,1):
            

            img1.seek(frame)
            print(img1)
            img1.convert('RGB').save('image.jpg')
            
            # print("img1")
            # print(img1)
            # ins= Imagecon(taskImage=img1)
            # ins.save()
            # context={'success':True}
            for item in allTasks:
                print(item.taskImage)
        #     pytesseract.pytesseract.tesseract_cmd ='C:/Python310/Lib/site-packages/Tesseract-OCR/tesseract.exe'
        # # converts the image to result and saves it into result variable
        #     result1 = pytesseract.image_to_string(img1)
        #     print(result1)


           
            img1=str(item.taskImage)
            str1="media/"
            img1=str1+img1
            img = cv2.imread("image.jpg")
            _, compressedimg = cv2.imencode(".jpg", img)
            file_bytes = io.BytesIO(compressedimg)

            url_api = "https://api.ocr.space/parse/image"
            response = requests.post(url_api, 
                files = {"image.jpg" : file_bytes}, 
                data = {"apikey" : "K85285375488957"})
            result = response.json()
            output = result["ParsedResults"][0]["ParsedText"]
            print(output)
            print("out")
            # result1.append(output)
    
        # gif='a'
        # img1.save(gif+".png",'png', optimize=True, quality=70)
        # img1.convert('RGBA')
        # global im1
        # import_filename = item.taskImage
        # im1=Image.open(import_filename).convert('RGB')
        # export_filename=fd.asksaveasfilename(defaultextension=".jpg")
        # im1.save(export_filename)
        # messagebox.showinfo("Success","File converted to .jpg")
        # describes image format in the output				
        # path where the tesseract module is installed  
        # write text in a text file and save it to source path
        print(output)                
        context={'tasks':output} 
        return render(request,'tasks.html',context)





















        global im1
        img1=request.FILES.get('img1')
        # print(type(img1))
        # im12 = Image.open(img1)
        # gif='a'
        # im12.save(gif+".png",'png', optimize=True, quality=70)
        # print(type(im12))
        # print("tttttt")     
        ins1= Imagecon(taskImage=img1)
        ins1.save()
        context={'success':True}
    return render(request,'gif_to_text.html',context)

def gif_text(request):
    allTasks=Gifcon.objects.all()
    # print(allTasks)
    for item in allTasks:
        print(item.taskImage)
    # opening an image from the source path
    # img = Image.open(item.taskImage)
    # ins= Imagecon(taskImage=img1)
        	
    img1 = Image.open(item.taskImage)
    result = ["Here are your results"]
    
    for frame in range(0,5):

        img1.seek(frame)
        print(type(img1))
        img1.convert('RGBA')
        print(img1)
        pytesseract.pytesseract.tesseract_cmd ='C:/Python310/Lib/site-packages/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable
        result1 = pytesseract.image_to_string(img1)
        print(result1)
        result.append(result1)
 
    # gif='a'
    # img1.save(gif+".png",'png', optimize=True, quality=70)
    img1.convert('RGBA')
    # global im1
    # import_filename = item.taskImage
    # im1=Image.open(import_filename).convert('RGB')
    # export_filename=fd.asksaveasfilename(defaultextension=".jpg")
    # im1.save(export_filename)
    # messagebox.showinfo("Success","File converted to .jpg")
    # describes image format in the output				
    # path where the tesseract module is installed  
    # write text in a text file and save it to source path
    print(result)                
    context={'tasks':result} 
    return render(request,'gif_text.html',context) 

def translate_to_text(request):
    context={'success':False}
    if request.method=="POST":
        
        desc=request.POST['desc']
        langto=request.POST['langto']
        
        print(desc)
        ins=translan(taskDesc=desc,taskLan=langto)
        ins.save()
        context={'success':True}
        p = Translator() 
        print("trn")   
        allTasks=translan.objects.all()  
        for item in allTasks:
            print(item.taskDesc)                

        k = p.translate(item.taskDesc,dest=item.taskLan)      
        print(k)
        context={'tasks':k.text}
        
    return render(request,'translate_to_text.html',context)