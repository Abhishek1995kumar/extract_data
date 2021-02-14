from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage

# import sqlalchemy                     # iss ka use tab karenge jab ham MySQL Server ke sath kaam karenge

#   # iss ka use tab karenge jab ham MySQL Server ke sath kaam karenge
# engine = create_engine("mysql+pymysql://root:@localhost/ocr_image", echo=True)

from sqlalchemy import create_engine
import pytesseract
import cv2
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='ocr_image')
cursor = connection.cursor()

def index(request):

    if request.method == "POST":

        uploads = request.FILES['picture']

        print(uploads.name)
        print(uploads.size)

        fs = FileSystemStorage()
        fs.save(uploads.name, uploads, max_length=None)

        pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
        img = cv2.imread(r"D:\All_Projects\My_All_Projects\Django\extract_data\Meter.png", 0)

        Bill_Amount = img[685:705, 683:790]

        Due_Date = img[83:110, 660:800]

        CA_No = img[120:135, 775:900]

        due_date = pytesseract.image_to_string(Due_Date)
        ca_no = pytesseract.image_to_string(CA_No)
        bill_amount = pytesseract.image_to_string(Bill_Amount)

        print("@@@@@")
        print(str(due_date).strip(),str(ca_no).strip(),str(bill_amount).strip())

        sql_query = r"INSERT INTO myapp_extract_image(due_date,account_no,bill_amount) VALUES (%s,%s,%s)"
        data = (str(due_date).strip(),str(ca_no).strip(),str(bill_amount).strip())
        cursor.execute(sql_query, data)
        connection.commit()

        return redirect('success')

    return render(request, 'profile.html')

def success(request):

    if request.method == 'GET':
        # getting all the objects of hotel.
        extract_images = extract_image.objects.last()
        return render(request, 'success.html', {'extract_images' : extract_images})


