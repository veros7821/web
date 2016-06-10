from django.shortcuts import render
from django.utils import timezone
from .models import Posteo
from .forms import PostForm

# Create your views here.

def inicio(request):
        return render(request,'inicio.html',{})

def post_list(request):
        posteos = Posteo.objects.filter(fecha_public__lte=timezone.now()).order_by('fecha_public')
        return render(request, 'sitio.post_list.html', {'posteos': posteos})

def post_detalle(request, pk):
        posteos= Posteo.objects.get(pk=id)
        return render(request, 'sitio.post_detalle.html', {'posteos': posteos})

def post_new(request):
        form = PostForm()
        return render(request, 'sitio.post_edit.html', {'form': form})

