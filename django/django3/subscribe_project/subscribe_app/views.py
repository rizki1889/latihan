from django.shortcuts import render, redirect
from subscribe_app.models import Customer
from subscribe_app.form import NewSubscribe

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers': customer_list}
    return render(request, 'subscribe_app/customer.html', context=customer_dict)

def subscribe(request):
    if request.method == "POST":
        form = NewSubscribe(request.POST)
        
        if form.is_valid():
            form.save()  
            return redirect('customers')  
        else:
            print("error: Form invalid")  
    else:
        form = NewSubscribe()  

    return render(request, 'subscribe_app/subscribe.html', {'form': form})