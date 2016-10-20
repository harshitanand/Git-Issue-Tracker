from django.shortcuts import render
import requests as req
import json
import datetime
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
            res = req.get(path, params={"state":"open", "direction":"desc"}).json()
            total_issues =  total_issues + len(res)
            one_day = datetime.datetime.now() - datetime.timedelta(hours = 24)
            res = req.get(path, params={"state":"open", "direction": "desc", "since": one_day.strftime('%Y-%m-%d %H:%M:%S')}).json()
            lastday_issues = lastday_issues + len(res)
            one_week = one_day - datetime.timedelta(hours = 7*24)
            res = req.get(path, params={"state":"open", "direction":"desc", "since": one_week.strftime('%Y-%m-%d %H:%M:%S')}).json()
            lastweek_issues = lastweek_issues + len(res)
            return render(request, 'index.html', {'total_issues':total_issues, "lastday_issues":lastday_issues, "lastweek_issues":lastweek_issues, "before_week":total_issues - lastweek_issues - lastday_issues})
        else:
            return render(request, 'index.html', {'error': 'Link to GitHub Repository is incorrect it should be like  \'https://github.com/Shippable/support/issues\''})
