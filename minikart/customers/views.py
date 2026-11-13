from django.shortcuts import render

# Create your views here.
def user_accounts(request):
    return render(request,'account.html')
