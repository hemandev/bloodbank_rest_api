from django.contrib.auth.models import User, Group
from rest_framework import viewsets, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, GroupSerializer, BankDataSerializer
from .models import DonerDetails
from rest_framework.decorators import api_view, parser_classes
from .gmaps import LocationDetails
from collections import OrderedDict
import operator


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BankDataViewSet(viewsets.ModelViewSet):
    queryset = DonerDetails.objects.all()
    serializer_class = BankDataSerializer


class DetailsView(APIView):

    def get(self,request,format=None):
        doner_data = DonerDetails.objects.all()
        serializer = BankDataSerializer(doner_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


@parser_classes(('JSONParser', ))
@api_view(['GET', 'POST'])
def change_details(request, pk):
    if request.method == 'POST':
        donated_recently = request.data['recently_donated']
        donated_recently = True if donated_recently == 'True' else False
        doner_object = DonerDetails.objects.get(pk=pk)
        doner_object.change_donation_status(donated_recently)
        doner_object.save()
        return Response({'status': True})

    elif request.method == 'GET':
        object = DonerDetails.objects.get(pk=pk)
        serializer = BankDataSerializer(object)
        return Response(serializer.data)


@api_view(['GET'])
def query_users(request,):
    if request.method == 'GET':
        doner_details = {}
        dictt = {}
        group = request.query_params.get('group')
        user_location = request.query_params.get('location')
        doners = DonerDetails.objects.filter(blood_group__exact=group)
        for item in doners:
            doner_location = item.location
            distance = LocationDetails().get_distance(user_location, doner_location)
            doner_details[item.name] = distance
            sorted_list = OrderedDict(sorted(doner_details.items(), key=operator.itemgetter(1)))

        return Response(sorted_list)











