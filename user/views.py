

from .forms import SignUpForm

from django.shortcuts import render, redirect

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            
            
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})