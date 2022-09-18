from django.views.generic import ListView, DetailView
from .models import Question


class IndexView(ListView):
    model = Question
    template_name = 'index.html'

    def get_queryset(self):
        if self.model is not None:
            queryset = self.model.objects.all()
        return queryset[:5]


class PollDetailView(DetailView):
    model = Question
    template_name = 'detail.html'
    queryset = Question.objects.all()


class PollResultsView(DetailView):
    model = Question
    template_name = 'results.html'







