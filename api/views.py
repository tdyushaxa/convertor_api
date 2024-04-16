from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PdfToWordSerializers, ImageOcrSerializers
from rest_framework import status


@api_view(["post"])
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


@api_view(["post"])
def image_to_text(request):
    serializers = ImageOcrSerializers()
    if request.method == "POST":
        serializers = ImageOcrSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": "succesfully created and convert",
                    "data": serializers.data
                }
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializers.errors
        )
    return Response(
        status=status.HTTP_400_BAD_REQUEST,
        data=serializers.errors
    )
