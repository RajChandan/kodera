from django.shortcuts import render


# Create your views here.
def contact(request):
    print(request.method)
    year_range = range(2010, 2028)
    job_titles = ["A", "B"]
    if request.method == "POST":
        print(request.POST)
    return render(
        request,
        "Contact/contact.html",
        {"year_range": year_range, "job_titles": job_titles},
    )
