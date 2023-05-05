from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import UnitSerializer
from .models import Unit

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/unit-list/',
        'Detail View': '/unit-detail/<str:pk>/',
        'Create': '/unit-create/',
        'Update': '/unit-update/<str:pk>',
        'Delete': '/unit-delete/<str:pk>',
    }

    return Response(api_urls)


@api_view(['GET'])
def unit_list(request):
    units = Unit.objects.all()
    serializer = UnitSerializer(units, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def unit_detail(request, pk):
    units = Unit.objects.get(id=pk)
    serializer = UnitSerializer(units, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def unit_create(request):
    """
    Create view
    """
    serializer = UnitSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def unit_update(request, pk):
    """
    Update current unit by pk
    """
    unit = Unit.objects.get(id=pk)
    serializer = UnitSerializer(instance=unit ,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def unit_delete(request, pk):
    """
    Delete unit by pk
    """
    unit = Unit.objects.get(id=pk)
    unit.delete()

    return Response("Unit succsesfully delete!")
