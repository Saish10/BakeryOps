"""
Serializers for user authentication
"""

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from base.models import Country, State
from .models import UserAccount

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        """
        Validate the user credentials
        """
        email = attrs.get("email", "").strip().lower()
        password = attrs.get("password", "")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if user is None:
            raise serializers.ValidationError(_("Invalid email or password."))

        # Check if the user is active
        if not user.is_active:
            raise serializers.ValidationError(
                _("Your account has been deactivated.")
            )

        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        # If needed, define the create logic here
        raise NotImplementedError("Create method not implemented.")

    def update(self, instance, validated_data):
        # If needed, define the update logic here
        raise NotImplementedError("Update method not implemented.")


class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for user details
    """

    class Meta:
        """
        Meta options for the UserSerializer
        """
        model = UserAccount
        fields = ("internal_id", "email", "first_name", "last_name")


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for user details
    """

    class Meta:
        """
        Meta options for the UserSerializer
        """
        model = UserAccount
        fields = [
            "email",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "phone",
            "address",
            "city",
            "state",
            "country",
        ]

