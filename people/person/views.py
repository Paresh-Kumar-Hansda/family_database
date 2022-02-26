from django.shortcuts import render, redirect
from .models import Person
# Create your views here.
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
class PersonListView(generic.ListView):
    model = Person
from django.contrib.auth.mixins import LoginRequiredMixin
class PersonDetailView(LoginRequiredMixin,generic.DetailView):
    model = Person
    def get_queryset(self):
        return Person.objects.filter(django_username=self.request.user)
#from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
# Import User UpdateForm, ProfileUpdatForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,IdentyUpdateForm, JharsewaForm, EducationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! You are now able to log in') 
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'person/register.html', {'form': form})

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.person) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.person)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'person/profile.html', context)

@login_required
def identy(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        #p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.person)
        i_form = IdentyUpdateForm(request.POST)
        if i_form.is_valid():
            #u_form.save()
            #p_form.save()
            i_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('person-detail') # Redirect back to profile page

    else:
        #u_form = UserUpdateForm(instance=request.user)
        #p_form = ProfileUpdateForm(instance=request.user.person)
        i_form = IdentyUpdateForm()
    context = {
        'i_form': i_form,
    }

    return render(request, 'person/identy.html', context)

def jharsewa(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JharsewaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('person')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JharsewaForm()
    return render(request, 'person/jharsewa.html', {'form': form})



def edu(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EducationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('person')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EducationForm()
    return render(request, 'person/edu.html', {'form': form})
