from rest_framework import serializers
from django.contrib.auth import get_user_model
from apibooks.books.models import Libro


UserModel = get_user_model()


class LibroSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Libro
        fields = ('id', 'url', 'nombre', 'vendido', 'paginas',
                  'fecha_de_publicacion', 'idioma',
                  'portada', 'generos', 'doc', 'resumen')
        read_only_fields = ['id', 'user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = Libro.objects.filter(nombre__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("El título ya es usado")
        return value


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('username', 'password')
