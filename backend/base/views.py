from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    return Response()


@api_view(["GET"])
def get_real_estate(request, pk):
    return Response()
