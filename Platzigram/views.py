from datetime import datetime
from django.http import HttpResponse
import json
"""   {}    []  """

def hello_world(request):
    return HttpResponse('Oh hl current server time  is {now}' .format(
        now = datetime.now().strftime(' %b %dth, %Y -%H : %M hrs')
    ))

def sort_integers(request):
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'number': sorted_ints,
        'message':'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type = 'application/jason'
    )

def say_hl(request,name,age):
    if age < 12:
        message ='sorry {},you are not allowed here'.format(name)
    else:
        message = 'hello {}!, welcome to Platzigram'.format(name)
    return HttpResponse(message)