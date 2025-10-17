from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Questions

# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list}
    # return HttpResponse(template.render(context,request))
    return render(request,"polls/index.html",context)

def details(request,question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Questions does not exists")
    return render(request,"polls/detail.html",{"question":question})

def result(request,question_id):
    response = "you are looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse(f"You are voting on the question {question_id}")