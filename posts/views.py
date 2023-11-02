from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

"""   {}    []  """

posts = [
    {
        'Title':' La Vida es bella',
        'user':{
            'name':'Jonathan',
            'picture':'https://fastly.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
        },
        'timestamp': datetime.now().strftime(' %b %dth, %Y -%H : %M hrs'),
        'photo':'https://fastly.picsum.photos/id/173/200/200.jpg?hmac=avUVgEVHNuQ4yZJQhCWlX3wpnR7d_fGOKvwZcDMLM0I',
    },
    {
        'Title':' Messi Lover',
        'user':{
            'name':'Milagros',
            'picture':'https://fastly.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
        },
        'timestamp': datetime.now().strftime(' %b %dth, %Y -%H : %M hrs'),
        'photo':'https://fastly.picsum.photos/id/24/4855/1803.jpg?hmac=ICVhP1pUXDLXaTkgwDJinSUS59UWalMxf4SOIWb9Ui4',
    },
    {
        'Title':' Messi Lover',
        'user':{
            'name':'Milagros',
            'picture':'https://fastly.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
        },
        'timestamp': datetime.now().strftime(' %b %dth, %Y -%H : %M hrs'),
        'photo':'https://fastly.picsum.photos/id/846/200/300.jpg?grayscale&hmac=llq2Wb--5I8_R9Vl4ahxS2HGnpppc19G_pbZ34R-_js',
    },
    {
        'Title':' Messi Lover',
        'user':{
            'name':'Milagros',
            'picture':'https://fastly.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
        },
        'timestamp': datetime.now().strftime(' %b %dth, %Y -%H : %M hrs'),
        'photo':'https://picsum.photos/seed/picsum/200/300',
    },
]

def list_posts(request):
    return render(request,'posts/feed.html',{'posts':posts})