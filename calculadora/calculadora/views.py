from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse

@api_view()
def api_root(request):
    return Response({
        'hello_world': reverse('hello_world', request=request),
        'add': reverse('add', request=request),
        'mult': reverse('mult', request=request),
    })

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view()
def add(request):
    """
    **host**/add/?a=1&b=1
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        result = first_number + second_number
        print('result: ', result)
        return Response({'function': 'add','result': result})
    except Exception as e:
        return Response({'function': 'add','result': 'there was an error ' + str(e)})

@api_view()
def mult(request):
    """
    **host**/mult/?a=1&b=1
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        result = first_number * second_number
        print('result: ', result)
        return Response({'function': 'mult','result': result})
    except Exception as e:
        return Response({'function': 'mult','result': 'there was an error ' + str(e)})