from django.shortcuts import get_object_or_404, render
from .models import Question
from django.http import HttpResponseRedirect
from django.urls import reverse


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'detail.html', {'question': question, 'error_message': 'You did not select any choices'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))