# -*- coding: utf-8 -*-

# # Third Party Stuff
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from . import models, serializers
from rest_framework.decorators import list_route, detail_route


class UserAuthViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

	permission_classes = (AllowAny,)
	# queryset = models.City.objects.filter(is_published=True)
 #    serializer_class = serializers.CitySerializer

	@list_route(methods=['post'])
	def register(self, request):
		print("hello in side register")
		serialized = UserSerializer(data=request.DATA)
#     permission_classes = (AllowAny,)
#     queryset = models.City.objects.filter(is_published=True)
#     serializer_class = serializers.CitySerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         for index, item in enumerate(queryset):
#             if item.for_festival == True:
#                 queryset[index].country = "All Fetivals"
#                 queryset[index].state = "/"
#         return paginated_response(request, queryset, serializers.CitySerializer)
	
	def login(self, request):
		print( "I am here in login ")
