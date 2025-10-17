from django.http import HttpResponse
from django.template import loader
from .models import Questions

# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list}
    return HttpResponse(template.render(context,request))

def details(request,question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def result(request,question_id):
    response = "you are looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse(f"You are voting on the question {question_id}")