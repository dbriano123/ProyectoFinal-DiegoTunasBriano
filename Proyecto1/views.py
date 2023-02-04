from contextvars import Context
import os
from django.http import HttpResponse
from jinja2 import Template
from django.shortcuts import redirect, render

from Proyecto1.models import Pagina,Usuario
import datetime

def obtenerUsuario(request):
    usuarioC = request.COOKIES.get('usuario')
    if usuarioC is not None:
        usuarios = Usuario.objects.filter(usuario=usuarioC)
        if len(usuarios) > 0:
            usuario = usuarios[0]
            print(usuario.tipo)
            print(usuario)
            return usuario
    return None

def inicio(request):
    usuario = obtenerUsuario(request)
    paginas = Pagina.objects.filter()
    return render(request, 'index.html', {"paginas": paginas,"usuario":usuario})

def perfil(request):
    usuario = obtenerUsuario(request)
    usuarioBase = Usuario.objects.filter(usuario=usuario.usuario)
    
    if request.method == 'POST':
        usuarioBase = usuarioBase[0]
        usuarioBase.nombre = request.POST['nombre']
        usuarioBase.email = request.POST['email']
        usuarioBase.save()
    usuario = obtenerUsuario(request)
    return render(request, 'perfil.html', {"usuario":usuario})




def eliminarPagina(request,id):
    
    paginas = Pagina.objects.filter(id=id)
    paginas.delete()
        
    return redirect('inicio')


def ingresoPagina(request):
    
    usuario = obtenerUsuario(request)
    print(usuario)
    if request.method == 'POST':
        
        pagina = Pagina(
                titulo=request.POST['titulo'],
                subtitulo=request.POST['subtitulo'],
                cuerpo=request.POST['cuerpo'],
                imagen=request.POST['imagen'],
                fecha=datetime.datetime.now(),
                autor=usuario.usuario
        )
        pagina.save()
        return redirect('inicio')


    return render(request, 'ingresoPagina.html',{"usuario":usuario})




def salir(request):
    

    redirectInicio = redirect('inicio')
    redirectInicio.delete_cookie('usuario')
    redirectInicio.delete_cookie('nombre')
    redirectInicio.delete_cookie('tipo')
    return redirectInicio


def entrar(request):
    
    usuarioReg = obtenerUsuario(request)
    if request.method == 'POST':
        usuario=request.POST['usuario']
        clave=request.POST['clave']
        usuarios = Usuario.objects.filter(usuario=usuario,clave=clave)
        print(usuarios)
        if len(usuarios) > 0:
            usuario = usuarios[0]
            print(usuario.tipo)
            redirectInicio = redirect('inicio')
            redirectInicio.set_cookie('usuario', usuario.usuario)
            redirectInicio.set_cookie('nombre', usuario.nombre)
            redirectInicio.set_cookie('tipo', usuario.tipo)
            return redirectInicio
        else:
            return render(request, 'entrar.html',{ 'error' :'Usuario o contraseña incorecto.',"usuario":usuarioReg})
        
        
    return render(request, 'entrar.html')
        
    



def registro(request):
    
    usuarioReg = obtenerUsuario(request)
    if request.method == 'POST':
        
        nuevousuario = Usuario(
                nombre=request.POST['nombre'],
                clave=request.POST['clave'],
                email=request.POST['email'],
                usuario=request.POST['usuario'],
                tipo='usuario'
        )
        nuevousuario.save()
        return redirect('entrar')


    return render(request, 'registro.html',{"usuario":usuarioReg})


def pagina(request,id):
    usuario = obtenerUsuario(request)

    paginas = Pagina.objects.filter(id=id)
    pagina = None
    if len(paginas) > 0:
        pagina = paginas[0]
        
    return render(request, 'pagina.html', {"pagina": pagina,"usuario":usuario})



def sobreNosotros(request):
   usuario = obtenerUsuario(request)
   return render(request, 'sobreNosotros.html',{"usuario":usuario})
