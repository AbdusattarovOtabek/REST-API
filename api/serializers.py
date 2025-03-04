from rest_framework.serializers import ModelSerializer
from carbase.models import Car
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.first_name
        token["username"] = user.username

        return token



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = ["id", "username", "carname", "color","mark", "mileage", "price", "img"]