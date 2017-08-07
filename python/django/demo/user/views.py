from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .forms import UserForm


def index(request):
    return render(request, "index.djhtml", {
        "users": User.objects.all().select_related("profile")
    })


def details(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST, instance=user)

    if request.method == 'POST' and form.is_valid():
        user.save()
        #messages.success(request, ('Your profile was successfully updated!'))

        return redirect('user:index')

    return render(request, "details.djhtml", {
        "form": form
    })
