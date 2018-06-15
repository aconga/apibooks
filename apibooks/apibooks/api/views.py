from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework import filters
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from apibooks.books.models import Libro
from .permissions import IsOwnerOrReadOnly
from .serializers import LibroSerializer, UserSerializer


class LibroAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'slug'
    serializer_class = LibroSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('vendido',)
    ordering = ('-fecha_de_publicacion',)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            qs = Libro.objects.filter(user=self.request.user)
        else:
            qs = Libro.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(nombre__icontains=query)|
                    Q(resumen__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        print()
        return {"request": self.request}


class LibroCrudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = LibroSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Libro.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
