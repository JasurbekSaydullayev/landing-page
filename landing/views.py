from django.shortcuts import render
from .models import Announcements
from django.core.paginator import Paginator
from .models import Customers


def landing(request):
    announcements_list = Announcements.objects.all()
    paginator = Paginator(announcements_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'announcements': page_obj})



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        customer = Customers(
            name=name,
            email=email,
            phone=phone,
        )
        customer.save()

        return render(request, 'backhomepage.html')

    return render(request, 'contact.html')
