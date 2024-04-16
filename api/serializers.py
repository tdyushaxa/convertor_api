from rest_framework import serializers
from .models import PDF_TO_WORD, ImageOCR, ImageToPdf


class PdfToWordSerializers(serializers.ModelSerializer):
    class Meta:
        model = PDF_TO_WORD
        fields = ('id', 'file_name', 'pdf_file', 'result', "word_file")

    def to_representation(self, instance):
        representation = super(PdfToWordSerializers, self).to_representation(instance)
        domain_name = "127.0.0.1:8000"
        if representation['word_file'] is not None:
            full_path = domain_name + instance.word_file.url
            representation['word_file'] = full_path.replace("/media-files/word/", "")
            return representation

    def validate(self, validated_data):
        pdf_file = validated_data.get('pdf_file')
        file_name = pdf_file.name
        if file_name.split(".")[-1] != "pdf":
            return serializers.ValidationError({
                "status": False,
                "message": "File type not allowed! Please upload a pdf file"
            })
        return validated_data


class ImageOcrSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageOCR
        fields = ('id', 'file_name', 'image', 'result', 'lang')

    def to_representation(self, instance):
        representation = super(ImageOcrSerializers, self).to_representation(instance)
        domain_name = "127.0.0.1:8000"
        if representation['image'] is not None:
            full_path = domain_name + instance.image.url
            representation['image'] = full_path
            return representation

    def validate_image(self, validated_data):
        file_name = validated_data.name
        if file_name.split(".")[-1] not in ["jpg", "jpeg", "png", "heic", "svg"]:
            return serializers.ValidationError({
                "status": False,
                "message": "File type not allowed! Please upload a pdf file"
            })
        return validated_data


class ImageToPdfSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageToPdf
        fields = ("id", "file_name", "image", "result")
