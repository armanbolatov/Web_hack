
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .parser import parse_schema
from django.http import JsonResponse



    
@api_view(['GET'])
def parse(request):
    f = open("/Users/macbook/Desktop/tutorial/tutorial/quickstart/src/first_text.txt", "r")
    physical_plan = f.read()
    
    
    graph1 =  parse_schema(physical_plan)
    
    dict1 = {'id': 1, 'filename' : 'first_text', 'code' : 'some code'}
    dict1.update(graph1)
    
    result = [dict1]
    
    print(result)
    
    
    return JsonResponse(result, safe=False)
     
    #return Response({"message": "Hello, world!"})

