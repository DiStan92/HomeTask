from .models import TodoListItem
from django.http import HttpResponseRedirect

def add_Item(request):
    text = request.POST.get('content', None)
    new_item = TodoListItem(content=text)
    new_item.save()
    return HttpResponseRedirect(redirect_to='/todo/')


def delete_item(request, object):
    item = TodoListItem.objects.get(pk=object)
    item.delete()
    return HttpResponseRedirect(redirect_to='/todo/')