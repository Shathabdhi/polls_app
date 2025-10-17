from django.http import HttpResponse
from .models import Questions

# Create your views here.

def index(request):
    recent_questions = Questions.objects.order_by("-pub_date")[:5]
    question_texts = []
    for questions in recent_questions:
        question_texts.append(questions.questions_text)
        question_texts.append(", \n")
    output = ", ".join(question_texts)
    return HttpResponse(question_texts)

def details(request,question_id):
    return HttpResponse(f"You are looking at question {question_id}")

def result(request,question_id):
    response = "you are looking at the result of the question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse(f"You are voting on the question {question_id}")