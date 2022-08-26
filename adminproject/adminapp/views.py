from django.shortcuts import render, redirect
from .forms import UsrForm, loginForm
from .models import Person
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def user_list(request):
        if 'user' in request.session:      # to stop accessing directly from url without login
            ul = {'user_list' : Person.objects.all()}
            return render(request, "list.html",ul)
        else:
            return redirect('login')


def user_form(request,id=0):
    if 'user' in request.session:   
        if request.method == 'GET':
            if id == 0:             
                form = UsrForm()  # to get empty list to add user GET
                
            else:
                user = Person.objects.get(pk=id)
                form = UsrForm(instance=user)   # to get list to update user GET
                    
            return render(request, "form.html", {'form':form})

        else:
            if id == 0:
                form = UsrForm(request.POST)   # to send list to add user POST
                  
            else:
                user = Person.objects.get(pk=id)    # to send list to update user POST
                form = UsrForm(request.POST,instance = user)
            if form.is_valid():
                form.save()
            return redirect('/list')
    else:
            return redirect('login')     


def user_delete(request,id):
    user = Person.objects.get(pk=id)
    user.delete()
    return redirect('/list')


def user_login(request):
    
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')         # cleaned_data automatically converts data to the appropriate type 
            password=form.cleaned_data.get('password')
            i = Person.objects.filter(username=username,password=password).exists()
            user = {'user_list' : Person.objects.filter(username=username,password=password)}
            
            if i == True:
                j = Person.objects.filter(username=username, role_id = 1).exists()
                if j == True:
                    request.session['user'] = username
                    return redirect('list')                     #to authenticate admin or user
                request.session['user'] = username
                return render(request,"userpage.html", user )
            else:
                messages.error(request, 'Invalid username or password!')
                
    context = {'form':form}
    return render(request,'login.html',context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)    #logout - back to login
def user_logout(request):
    request.session.clear()
    logout(request)
    return redirect('/')