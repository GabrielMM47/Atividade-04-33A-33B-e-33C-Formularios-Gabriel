from django.shortcuts import render, redirect
from .models import Carro, Hobbie, FichaTecnica

# Create your views here.
def home(request):
  carro = Carro.objects.all()
  hobbie = Hobbie.objects.all()
  ficha = FichaTecnica.objects.all()
  return render(request, "home.html", context={ "carro": carro, "hobbie": hobbie, "ficha": ficha })


def create_hobbie(request):
  if request.method=="POST":
    #criar um novo filme usando os valores do formulário
    Hobbie.objects.create(
      title = request.POST["title"],
      frequencia = request.POST["frequencia"],
      prioridade = request.POST["prioridade"],
      categoria = request.POST["categoria"]
    )
    return redirect("home")

  options_freq = Hobbie._meta.get_field("frequencia").choices
  options_cat = Hobbie._meta.get_field("categoria").choices

  return render(request, "forms_hobbies.html", context={"action": "Adicionar", "options_freq": options_freq, "options_cat": options_cat})

def update_hobbie(request, id):
  hobbie = Hobbie.objects.get(id = id)
  if request.method=="POST":
    #criar um novo filme usando os valores do formulário
    hobbie.title = request.POST["title"]
    hobbie.frequencia = request.POST["frequencia"]
    hobbie.prioridade = request.POST["prioridade"]
    hobbie.categoria = request.POST["categoria"]
    hobbie.save()
    return redirect("home")
  
  options_freq = Hobbie._meta.get_field("frequencia").choices
  options_cat = Hobbie._meta.get_field("categoria").choices
  
  return render(request, "forms_hobbies.html", context={"action": "Atualizar", "hobbie": hobbie, "options_freq": options_freq, "options_cat": options_cat})

def delete_hobbie(request, id):
  hobbie = Hobbie.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      hobbie.delete()
    
    return redirect("home")
  return render(request, "are_you_sure_hobbie.html", context={"hobbie": hobbie})


def create_carro(request):
  if request.method=="POST":
    #criar um novo filme usando os valores do formulário
    Carro.objects.create(
      title = request.POST["title"],
      modelo = request.POST["modelo"],
      montadora = request.POST["montadora"],
      carroceria = request.POST["carroceria"],
      tipo_motor = request.POST["tipo_motor"]
    )
    return redirect("home")
    
  options_carroceria = Carro._meta.get_field("carroceria").choices
  options_tipo = Carro._meta.get_field("tipo_motor").choices
    
  return render(request, "forms_carros.html", context={"action": "Adicionar", "options_carroceria": options_carroceria, "options_tipo": options_tipo})

def update_carro(request, id):
  carro = Carro.objects.get(id = id)
  if request.method=="POST":
    #criar um novo carro usando os valores do formulário
    carro.title = request.POST["title"]
    carro.modelo = request.POST["modelo"]
    carro.montadora = request.POST["montadora"]
    carro.carroceria = request.POST["carroceria"]
    carro.tipo_motor = request.POST["tipo_motor"]
    carro.save()
    return redirect("home")

  options_carroceria = Carro._meta.get_field("carroceria").choices
  options_tipo = Carro._meta.get_field("tipo_motor").choices
  
  return render(request, "forms_carros.html", context={"action": "Atualizar", "carro": carro,  "options_carroceria": options_carroceria, "options_tipo": options_tipo})

def delete_carro(request, id):
  carro = Carro.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      carro.delete()
    
    return redirect("home")
  return render(request, "are_you_sure_carro.html", context={"carro": carro})