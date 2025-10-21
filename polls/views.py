from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404 , render
from django.urls import reverse
from django.template import loader
from django.db.models import F

from .models import Question , Choice

# Create your views here.
# /polls/
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list}
    # return HttpResponse(template.render(context,request))
    return render(request,"polls/index.html",context)

# /polls/5
def details(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

# /polls/5/results/
def result(request,question_id):
    response = "you are looking at the result of the question %s."
    return HttpResponse(response % question_id)

# /polls/5/vote/
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"you didn't select a choice.",
            },    
        )
    except:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))