#!/usr/bin/env python
# coding=utf-8

from source.apps.core.models.user.models import User, UserProfile
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class PasswordRecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()
    uid = serializers.CharField()
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ('new_password', 'confirm_password', 'uid', 'token')


class UserProfileSerializer(serializers.ModelSerializer):

    age = serializers.ReadOnlyField(source='get_age')

    class Meta:
        model = UserProfile
        exclude = ('user', )
        depth = 1

class UserListSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_joined', 'profile',)
        depth = 1


class UserDetailSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'is_staff', 'date_joined', 'email', 'profile',)
        depth = 1


class UserRegisterSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'profile'
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
