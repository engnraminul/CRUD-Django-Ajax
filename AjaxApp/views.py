from django.shortcuts import render



from django.views.generic import ListView, View

from AjaxApp.models import Crud
from django.http import JsonResponse

class CrudHome(ListView):
    model = Crud
    template_name= 'home.html'


# class CrudCreate(View):
#     def get(self, request):
#         name = request.GET.get('name')
#         email = request.GET.get('email')
#         phone = request.GET.get('phone')
#         city = request.GET.get('city')

#         Crud.objects.create(name=name, email=email, phone=phone, city=city)


def Home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']

        obj=Crud(name=name, email=email, phone=phone, city=city)
        obj.save()

        user = {
            "id": obj.id, "name": obj.name, "email": obj.email, "phone":obj.phone, "city": obj.city
        }

        data = { 
            "users": user
        }

        #return JsonResponse(data)

    Cruddata = Crud.objects.all().order_by('id')
    
    context = {
        'data': Cruddata
    }


    return render(request, 'home.html', context)