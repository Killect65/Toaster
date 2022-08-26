from django.shortcuts import render
from toster.models import QandAModel

def index(request):
    return render(request, 'toster/index.html')

def test(request):
    QfromData = QandAModel.objects.all()
    lst = []
    for q in QfromData:
        lst.append(q.question)
    context = {'Q1': lst[0], 'Q2': lst[1], 'Q3': lst[2], 'Q4': lst[3], 'Q5': lst[4]}
    if request.method == 'POST':
        result = request.POST
        request.session['res'] = result
    return render(request, 'toster/test.html', context)

def result(request):
    A11 = request.session['res']['A1']
    A22 = request.session['res']['A2']
    A33 = request.session['res']['A3']
    A44 = request.session['res']['A4']
    A55 = request.session['res']['A5']
    answers = [A11, A22, A33, A44, A55]
    right_answers = []
    qs = QandAModel.objects.all()
    for a in qs:
        right_answers.append(a.answer)
    k = 0
    mistakes = []
    for i in range(5):
        if answers[i] == right_answers[i]:
            k += 1
        else:
            mistakes.append(i+1)
    context = {'result': k, 'mistakes': mistakes}
    return render(request, 'toster/result.html', context)

