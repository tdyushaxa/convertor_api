from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PdfToWordSerializers
from rest_framework import status


@api_view(["get", "post"])
def pdf_to_word(request):
    serializers = PdfToWordSerializers()
    if request.method == "POST":
        data = request.data
        serializers = PdfToWordSerializers(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=status.HTTP_200_OK, data={
                "message": "success",
                "data": serializers.data
            })

    return Response(data={
        "message": serializers.errors
    })


@api_view(["get", "post"])
def image_to_pdf(request):
    serializers = PdfToWordSerializers()
    if request.method == "POST":
        data = request.data
        serializers = PdfToWordSerializers(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(status=status.HTTP_200_OK, data={
                "message": "success",
                "data": serializers.data
            })

    return Response(data={
        "message": serializers.errors
    })
