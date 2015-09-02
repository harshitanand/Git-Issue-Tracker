from django.shortcuts import render
import requests as req
import json
from datetime import time, date, datetime, timedelta
# Create your views here.

def result(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        url = request.POST['address'].split('/')
        if len(url) == 6 and url[2] == "github.com":
            err = False
        else:
            err = True
        if not err:
            owner, repo_name = url[3], url[4]
            path = "https://api.github.com/repos/%s/%s/issues" %  (owner,repo_name)
            total_issues = 0
            lastday_issues = 0
            lastweek_issues = 0
            for i in range(1,10):
                res = req.get(path, params={"state":"open", "page":i,"per_page":"100"}).json()
                total_issues =  total_issues + len(res)
            current = str(datetime.now()).split(" ")
            for i in range(1,10):
                res = req.get(path, params={"state":"open", "page":i,"per_page":"100","since":str(date.today() -timedelta(1)) + "T" + current[1]}).json()
                lastday_issues = lastday_issues + len(res)
            for i in xrange(1,10):
                res = req.get(path, params={"state":"open", "page":i,"per_page":"100","since":str(date.today() -timedelta(7)) + "T" + current[1]}).json()
                lastweek_issues = lastweek_issues + len(res)
            return render(request, 'index.html', {'total_issues':total_issues, "lastday_issues":lastday_issues, "lastweek_issues":lastweek_issues, "before_week":total_issues - lastweek_issues})
        else:
            return render(request, 'index.html', {'error': 'The link git hub repo issues is incorrect it should be like  \'https://github.com/Shippable/support/issues\''})