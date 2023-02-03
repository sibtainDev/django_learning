from django.db.models import Q
from django_rest_passwordreset.serializers import PasswordValidateMixin, PasswordTokenSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions

from user.models import User, ToDoTask
from utils.helper import check_email


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'email', 'password', 'username']

    def create(self, validated_data):
        user = User(
            username=validated_data.get('email').split('@')[0],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            phone=validated_data.get('phone'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['phone'] = user.phone

        return token

    def validate(self, attrs):
        user_name = attrs.get("email")
        password = attrs.get("password")

        if check_email(user_name) is False:
            try:
                user = User.objects.get(Q(username=user_name) | Q(phone=user_name))
                if user.check_password(password):
                    attrs['email'] = user.email

                """
                 In my case, I used the Email address as the default Username 
                 field in my custom User model. so that I get the user email 
                 from the Users model and set it to the attrs field. You can 
                 be modified as your setting and your requirement 
                """

            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed(
                    'No such user with provided credentials'.title())

        data = super().validate(attrs)
        return data


class ResetPasswordConfirmSerializer(PasswordTokenSerializer):
    password2 = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and Password2 does not match")
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()
    old_password = serializers.CharField()

    def validate(self, attrs):
        password = attrs.get("new_password")
        password2 = attrs.get("new_password2")
        if password != password2:
            raise serializers.ValidationError("Both Password does not match")
        return attrs


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'
