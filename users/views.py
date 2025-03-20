from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import RegisterForm


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account has been created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
    )
@login_required
def profilepage(request):
    return  render(request, "users/profile.html")
