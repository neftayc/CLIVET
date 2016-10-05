from django.shortcuts import render, redirect
from .forms import MascotaForm, EspecieForm


# Create your views here.

def especieView(request):
    if request.method == "POST":
        form = EspecieForm(request.POST)
        if form.is_valid():
            # validares aqui
            print "Es Valido"
            return redirect("/")
    else:
        form = EspecieForm()

    return render(request, "clivet.html", {"form": form})


def mascotaView(request):
    if request.method == "POST":
        modelform = MascotaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/")
    else:
        modelform = MascotaForm()

    return render(request, "clivet.html", {"form": modelform})
