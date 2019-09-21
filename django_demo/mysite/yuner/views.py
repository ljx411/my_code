from django.shortcuts import render
from yuner.models import Img


# Create your views here.

def upload_img(request):
    if request.method == 'post':
        file_list = request.FILES.getlist()
        for file in file_list:
            img = Img(img_url=file)
            img.save()
    return render(request, 'yuner/upload_img.html')
