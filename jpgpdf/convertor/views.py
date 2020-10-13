from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from convertor.forms import *
from PIL import Image
from django.conf.urls.static import settings
from django.conf import settings
from django.conf.urls.static import static
from convertor.models import convention

from django.urls import reverse
import os
# Create your views here.
class index_page(FormView):
    template_name = 'index.html'
    form_class = images_pdf
    def form_valid(self, form):
        print('the form is valid')
        self.object = form.save(commit=False)
        self.object.name = self.request.FILES['image'].name
        self.object.image = self.request.FILES['image']
#        form.save()


        saving = self.object.save()

        return HttpResponseRedirect(reverse('convertor:output', kwargs={'pk':self.object.pk}))


class output_view(DetailView):
    model = taking_img
    context_object_name = 'img'
    template_name = 'output.html'
    #img = self.request.FILES['image']
    #img1 = Image.open(img)
    #image1 = img1.convert('RGB')
    # image1.save(settings.MEDIA_URL + 'images', 'pdf')
    # image1.save(settings.MEDIA_URL + 'images', format='pdf')
    #self.request.FILES['image'] = image1.save(format='PDF', fp='media/images/' + self.request.POST['name'] + '.pdf')
    #self.request.FILES['file'] = image1.save(format='PDF', fp='media/images/' + self.request.POST['name'] + '.pdf')


    def post(self, request, pk):
        number = self.kwargs['pk']
        mode = taking_img.objects.get(pk=number)
        Prename = mode.name
        name = str(Prename).replace(" ", "_")
        img = Image.open(settings.MEDIA_ROOT+ "/images/" + name)
        image = img.convert("RGB")
        images_list = self.request.FILES.getlist("images")
        img_array = []
        for i in images_list:
            imgFromList = Image.open(i)
            img_c = imgFromList.convert("RGB")
            img_array.append(img_c)
        print(name)
        savin_img = image.save(fp=settings.MEDIA_ROOT + "/converted/" + name +".pdf", format="PDF", save_all=True, append_images=img_array)
        self.object = convention(name=name, file=settings.MEDIA_ROOT + "/converted/" + name +".pdf")
        self.object.save()

        return HttpResponseRedirect(reverse('convertor:processed', kwargs={'pk':self.object.pk}))


class processed(DetailView):
    model = convention
    context_object_name = 'pdf'
    template_name = "download.html"
    def get_context_data(self, **kwargs):
        data = super(processed, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        mode = convention.objects.get(pk=pk)
        file_location = mode.file.path
        data['link'] = "media/converted/" + mode.name + ".pdf"
        print(file_location)
        return data