from django.urls import path
from .views import IndexView, PollDetailView, PollResultsView
from .services import vote


app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PollDetailView.as_view(), name='detail'),
    path('<int:pk>/results', PollResultsView.as_view(), name='results'),
    path('<question_id>/vote', vote, name='vote'),

]