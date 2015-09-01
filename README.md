# Git-Issue-Tracker
App created in django tracks the open issues of a public git repo for last 1 month

In order to run the app you need to have following dependencies
    
    python >= 2.7
    django ==1.7
    
After you have met all the dependencies open the terminal just clone the repo and do as following 

    $ git clone https://github.com/harshitanand/Git-Issue-Tracker.git
    $ cd Git_Issue_Tracker
    $ python manage.py migrate
    $ python manage.py runserver
    
Now Open your browser navigate to 

    localhost:8000/track
    Enter a valid URL in the input box and track your repo issue for past 1 month
