from django.shortcuts import render, redirect
from app.models import SCHOOL
# Create your views here.



# def school_form(request):
#     name = request.POST.get('name')
#     address = request.POST.get('address')
#     established_year = request.POST.get('established_year')
#     photo = request.FILES.get('photo')
#     if request.method == 'POST':
#         school = SCHOOL(
#             name=name,
#             address=address,
#             established_year=established_year,
#             photo=photo
#         )
#         school.save()
#         return redirect('school_data')
#     return render(request, 'school.html')  

# def School_data(request):
#     data = SCHOOL.objects.all()
#     return render(request, 'school.html',{'school':data})



from django.shortcuts import render, redirect
from app.models import SCHOOL

def school_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        established_year = request.POST.get('established_year')
        photo = request.FILES.get('photo')

        school = SCHOOL.objects.create(
            name=name,
            address=address,
            established_year=established_year,
            photo=photo
        )
        return redirect('schools')
    return render(request, 'school_form.html')


def School_data(request):
    data = SCHOOL.objects.all()
    return render(request, 'school.html', {'school': data})
