from django.shortcuts import render,redirect

# Create your views here.

# counsilor dashboard
def home(request):
    return render(request,'home.html')

def newlyassignleads(request):
    return render(request, 'newly_leads.html')

def currentleads(request):
    return render(request, 'current_leads.html')

def previousleads(request):
    return render(request, 'previous_leads.html')