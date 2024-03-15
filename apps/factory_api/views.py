from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer
from .utils import GetMaterials


class GetProductList(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)


class GetProduct(APIView):
    queryset = Product.objects.all()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "id": {"type": "integer"},
                "count": {"type": "integer"}
            },
            required=["id", "count"]
        )
    ))
    def post(self, request):
        """
        Mahsulotlar list shaklida yuboriladi
            [{
                "id": integer,
                "count": integer
                  },
            {
                "id": integer,
                "count": integer
            }]

        Va kerakli natija qaytadi
        :param request:
        :return:
        """
        request_data = request.data
        res = GetMaterials(request_data).get_products_data()

        return Response({"result": res})
