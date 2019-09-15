from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from website_tools.models import Question, Choice


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('website/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))
class IndexView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, template_name='website/detail.html', context={'question': question})
class DetailView(generic.DetailView):
    template_name = 'website/detail.html'
    model = Question


# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'website/result.html', context={'question': question})

class ResultView(generic.DetailView):
    template_name = 'website/result.html'
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'website/detail.html', {'question': question, 'errormessage': '你没有选择选项'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('website_tools:result', args=(question.id,)))
