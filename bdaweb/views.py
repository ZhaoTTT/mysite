from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required

from .models import User, itemCFrecommendation
from .forms import LoginForm


    




# def index(request,userid):
#     # ls = ToDoList.objects.get(id=id)
#     user = get_object_or_404(User, userid=userid)
#     return render(request, "bdaweb/home.html", {'user': user})

# def reg(request):
#     if request.method == 'POST':
#         assert isinstance(request, HttpRequest) 
#         # userid = request.POST.get(user.userid)
#         userid = request.POST['userid']
#     # return render(request, "bdaweb/landingpage.html", {userid: userid})
#     return HttpResponseRedirect(reverse('bdaweb:landingpage', args=(userid,)))

def home(request):
    num_users=User.objects.all().count()
    return render(request, "bdaweb/home.html", {'num_users':num_users})


def reg(request):
    # if this is a POST request we need to process the form data
    # user = get_object_or_404(User, userid=userid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            userid = form.cleaned_data['userid']
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('bdaweb:landingpage', args=(userid,)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'bdaweb/home.html', {'form': form})



def landingpage(request,userid):
    # itemCFresult = itemCFrecommendation.objects.get(userid=userid)
    itemCFresult = get_object_or_404(itemCFrecommendation, userid=userid)
    context = {'itemCFresult': itemCFresult}
    # return HttpResponse(itemCFresult)
    return render(request, "bdaweb/landingpage.html", context)



# def CBrecommendation(request, userid):
#     user = get_object_or_404(User, pk=userid)
#     try:
#         selected_choice = user.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))