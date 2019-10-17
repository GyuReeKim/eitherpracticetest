from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'questions/index.html', {'questions': questions})

def detail(request, id):
    question = get_object_or_404(Question, id=id)
    choice_form = ChoiceForm()

    choices = question.choice_set.all()

    total_1 = choices.filter(pick=1).count()
    total_2 = choices.filter(pick=2).count()

    total_sum = total_1 + total_2

    if total_sum == 0:
        persent_1 = 0
        persent_2 = 0
    else:
        persent_1 = total_1 / total_sum * 100
        persent_2 = total_2 / total_sum * 100

    context = {
        'question': question,
        'choice_form': choice_form,
        'persent_1': persent_1,
        'persent_2': persent_2,
    }
    return render(request, 'questions/detail.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        form.save()
        return redirect('questions:index')
    else:
        form = QuestionForm()
        context = {
            'form':form,
        }
    return render(request, 'questions/form.html', context)

def update(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:detail', id)
    else:
        form = QuestionForm(instance=question)

    context = {
        'form':form,
    }
    return render(request, 'questions/form.html', context)

def delete(request, id):
    if request.method == "POST":
        question = get_object_or_404(Question, id=id)
        question.delete()
        return redirect('questions:index')
    else:
        return redirect('questions:detail', id)

@require_POST
def choice_create(request, id):
    question = get_object_or_404(Question, id=id)
    choice_form = ChoiceForm()
    if choice_form.is_valid():
        choice_form.save()
    return redirect("questions:detail", id)


@require_POST
def choice_delete(request, question_id, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    choice.delete()
    return redirect('questions:detail', question_id)
