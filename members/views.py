from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('all-members.html')
    context = {
        'members':members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member':member
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('template.html')
    context = { 'members' : mydata, }

    return HttpResponse(template.render(context, request))
