from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/expense/$', views.submit_expense, name='submit_expense'), 
    # yani agar in url ra didi va $ yani harchizi, boro be views dar pusheye web va tabe'e submit_expense ra farakhani kon
    url(r'^submit/income/$', views.submit_income, name='submit_income'), 
]