from django.shortcuts import render


# Create your views here.
def contact(request):
    print(request.method)
    return render(request, "Contact/contact.html")
