from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import RealEstate
from .serializers import RealEstateSerializer


@api_view(["GET"])
def get_routes(request):
    routes = [
        "/api/real_estate/",
        "/api/real_estate/create/",
        "/api/real_estate/upload/",
        "/api/real_estate/<id>/reviews/",
        "/api/real_estate/top/",
        "/api/real_estate/<id>/",
        "/api/real_estate/delete/<id>/",
        "/api/real_estate/update/<id>/",
    ]
    return Response(routes)


@api_view(["GET"])
def get_real_estates(request):
    real_estates = RealEstate.objects.all()
    serializer = RealEstateSerializer(real_estates, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_real_estate(request, pk):
    real_estate = RealEstate.objects.get(_id=pk)
    serializer = RealEstateSerializer(real_estate)
    return Response(serializer.data)
