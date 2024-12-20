from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect

from django.shortcuts import get_object_or_404

from django.urls import reverse

# Create your views here.
from .models import Question, Choice

#Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

# Get specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exsist")
    return render(request, "polls/detail.html", {'question':question})

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

#vote for a question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message':"You didnt select a choice"
        })
    else:
        selected_choice.votes += 1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))