from datetime import datetime
from django.shortcuts import render
def home(request):
    now = datetime.now()
    date_str = now.strftime('%B %d, %Y')
return render(request, 'home.html’, {"date_today": date_str})
