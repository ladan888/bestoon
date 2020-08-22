from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt

from web.models import User, Token, Expense, Income

from datetime import datetime


@csrf_exempt
def submit_income(request):
    this_token = request.POST.get('token', False)
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user, amount=request.POST['amount'], text = request.POST['text'], 
    date=date)
    
    return JsonResponse({
        'status' : 'OK',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_expense(request):
    this_token = request.POST.get('token', False)
    # this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token)
    if 'date' not in request.POST:
        date = datetime.now()
    #Expense.objects.create(user = this_user, amount=12, text = social lunch, date=date)
    Expense.objects.create(user = this_user, amount=request.POST.get('amount', False), 
                text = request.POST.get('text', False), date=date)
    return JsonResponse({
        'status' : 'OK',
    }, encoder=JSONEncoder)

