from django.shortcuts import render, reverse, redirect
from AppPerfiles.forms import UserRegisterForm

def registro(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
        
    else: 
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='AppPerfiles/registro.html',
        context={'form': formulario},
    )
