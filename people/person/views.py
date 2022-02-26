from django.shortcuts import render, redirect
from .models import Person
# Create your views here.
from django.views import generic

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
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,IdentyUpdateForm

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
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.person)
        i_form = IdentyUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.person.identy)
        if u_form.is_valid() and p_form.is_valid() and i_form.is_valid():
            u_form.save()
            p_form.save()
            i_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('identy') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.person)
        i_form = IdentyUpdateForm(instance=request.user.person.identy)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'i_form': i_form,
    }

    return render(request, 'person/identy.html', context)
