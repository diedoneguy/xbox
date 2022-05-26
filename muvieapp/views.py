from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import CategorySerializer,GenreSerializer,MovieSerializer,MovieShotsSerializer,VotesSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieShotsViewSet(ModelViewSet):
    queryset = MovieShots.objects.all()
    serializer_class = MovieShotsSerializer


class VotesViewSet(ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer
    permission_classes = [IsAuthenticated]  

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()

