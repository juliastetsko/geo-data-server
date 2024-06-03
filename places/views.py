from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from places.models import Place
from places.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "nearest location",
                type=str,
                description="Coordinates in 'x,y' format (eg '24.930,60.169')",
            ),
        ]
    )
    @action(
        methods=["GET"],
        detail=False,
        url_path="nearest-point",
    )
    def find_nearest_point(self, request):
        location = request.query_params.get("location")
        if location is None:
            return Response(
                {"error": "Parameter 'location' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        x, y = location.split(",")
        point = Point(float(x), float(y), srid=4326)
        nearest_place = (
            Place.objects.annotate(distance=Distance("location", point))
            .order_by("distance")
            .first()
        )
        if nearest_place:
            serializer = self.get_serializer(nearest_place)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No places found"}, status=status.HTTP_404_NOT_FOUND)
