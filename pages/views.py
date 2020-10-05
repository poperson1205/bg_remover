from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from .models import ImageFileModel
from .forms import ImageFileModelForm
from PIL import Image
from pathlib import Path
from django.conf import settings
import io

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ImageFileModelForm(request.POST, request.FILES)

        if form.is_valid():
            img = form['image'].value()
            with img.open('rb') as f_in:
                img_pil = Image.open(f_in)
                img_pil_resized = img_pil.resize((64,64))
                
                with io.BytesIO() as f_out:
                    img_pil_resized.save(f_out, format='PNG')
                    model_output = ImageFileModel.objects.create(image=ImageFile(name=img.name, file=f_out))
            
            return HttpResponseRedirect(model_output.image.url, content_type='')
    
    else:
        form = ImageFileModelForm()
        
    return render(request, 'pages/index.html', {'form': form})

def succeed(request):
    model = ImageFileModel.objects.all()[0]
    output_name = 'output.jpg'
    
    # Process image and save to 'output_path'
    with io.BytesIO() as f_out:
        with model.image.open() as f:
            img = Image.open(f)
            img_resized = img.resize((224,224))
            img_resized.save(f_out, format='JPEG')

        # Create output model
        model_output = ImageFileModel(image=ImageFile(name=output_name, file=f_out))
        model_output.save()

    return render(request, 'pages/succeed.html', {'path': model_output.image.url})
