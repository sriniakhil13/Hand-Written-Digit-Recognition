__author__ = 'jhonjairoroa87'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jsonp.renderers import JSONPRenderer


class Multiply(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        try:
            first_number = int(request.GET.get('a'))
            second_number = int(request.GET.get('b'))
            return Response({'Answer': first_number * second_number})
        except Exception as e:
            return Response({'Answer': 'There was an error,Try again ' + str(e)})


class Divide(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        try:
            first_number = int(request.GET.get('a'))
            second_number = int(request.GET.get('b'))
            return Response({'Answer': first_number / second_number})
        except Exception as e:
            return Response({'Answer': 'There was an error,Try again ' + str(e)})

