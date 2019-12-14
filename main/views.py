from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from main.models import DataModel
from main.serializers.DataModelSerializer import DataModelSerializer


class CreateDataView(CreateAPIView):
    model = DataModel
    serializer_class = DataModelSerializer


class FileUpdateView(APIView):
    @staticmethod
    def post(request):
        serializer = DataModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
