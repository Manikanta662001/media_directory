from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
def image_form(request):
    form=ImageForm()
    d={'form':form}
    if request.method=='POST' and request.FILES:
        form_data=ImageForm(request.POST,request.FILES)
        if form_data.is_valid():
            img=form_data.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            img_url=fs.url(file)
            d1={'img_url':img_url}
            return render(request,'display_image.html',d1)
        
    return render(request,'image_form.html',d)
