from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404 , render
from django.urls import reverse
from django.template import loader
from django.db.models import F
from django.views import generic

from .models import Question , Choice

# Create your views here.
# /polls/
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

# /polls/5
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# /polls/5/results/
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# /polls/5/vote/
def vote(request, question_id):
    model = Question
    template_name = "polls/results.html"