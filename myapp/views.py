# myapp/views.py

from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def image_list(request):
    images = Image.objects.all()
    return render(request, 'myapp/base.html', {'images': images})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'myapp/img_upload.html', {'form': form})
