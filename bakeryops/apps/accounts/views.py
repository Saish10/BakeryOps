"""
View for account app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from accounts.serializers import (
    LoginSerializer,
    UserDetailSerializer,
    UserListSerializer,
)
from accounts.utils import UserManager
from base.utility.pagination import StandardPagination
from base.utility.response import APIResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


class SignupView(APIView):
    """
    View for user signup.
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="signup",
        tags=["Auth"],
        request_body=UserDetailSerializer,
    )
    def post(self, request):
        """
        Handle user signup.
        """
        serializer = UserDetailSerializer(data=request.data)
        if not serializer.is_valid():
            response = APIResponse.error(errors=serializer.errors)
            return Response(response, status=HTTP_400_BAD_REQUEST)
        user = UserManager(request).signup(**request.data)
        if not user:
            response = APIResponse.error(message="User not created")
            return Response(response, status=HTTP_400_BAD_REQUEST)
        response = APIResponse.success(message="User signed up successfully")
        return Response(response, status=HTTP_200_OK)

class LoginView(APIView):
    """
    View for user login.
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="login",
        tags=["Auth"],
        request_body=LoginSerializer,
    )
    def post(self, request):
        """
        Handle user login.
        """
        serializer = LoginSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            response = APIResponse.success(
                message="User logged in successfully",
                data={
                    "token": token.key,
                    "user_id": user.internal_id,
                },
            )
            return Response(response, status=HTTP_200_OK)

        response = APIResponse.error(errors=serializer.errors)
        return Response(response, status=HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    View for user logout.
    """

    @swagger_auto_schema(
        operation_id="logout",
        tags=["Auth"],
    )
    def post(self, request):
        """
        Handle user logout.
        """
        if hasattr(request.user, "auth_token"):
            request.user.auth_token.delete()
            response = APIResponse.success(
                message="User logged out successfully"
            )
            return Response(response, status=HTTP_200_OK)

        response = APIResponse.error(message="User is not authenticated")
        return Response(response, status=HTTP_400_BAD_REQUEST)


class UserView(ViewSet):
    """
    View for Users
    """

    # userlist
    # userdetails
    # userdelete
    # userpatch
    # usercreate
    permission_classes = (AllowAny,)
    lookup_field = "internal_id"
    @swagger_auto_schema(
        operation_id="user_list",
        tags=["User Management"],
    )
    def list(self, request):
        """
        List users
        """
        print(request.tenant)
        queryset = UserManager(request).get_all_users()
        if not queryset:
            response = APIResponse.success(message="No users found", data=[])
            return Response(response, status=HTTP_400_BAD_REQUEST)
        data = StandardPagination(request).paginate(
            queryset, UserListSerializer
        )
        response = APIResponse.success(
            message="User list retrieved successfully", data=data
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="user_details",
        tags=["User Management"],
        manual_parameters=[
            openapi.Parameter(
                "internal_id",
                openapi.IN_PATH,
                description="User Internal ID",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True,
            ),
        ],
    )
    def retrieve(self, request, internal_id):
        """
        Retrieve user details
        """
        user = UserManager(request).get_user(internal_id)
        if not user:
            response = APIResponse.error(message="User not found")
            return Response(response, status=HTTP_400_BAD_REQUEST)
        data = UserDetailSerializer(user).data
        response = APIResponse.success(
            message="User details retrieved successfully", data=data
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="user_update",
        tags=["User Management"],
    )
    def update(self, request, internal_id):
        """
        Update user details
        """
        user = UserManager(request).update_user(internal_id, **request.data)
        if not user:
            response = APIResponse.error(message="User not found")
            return Response(response, status=HTTP_400_BAD_REQUEST)
        response = APIResponse.success(
            message="User details updated successfully"
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="user_partial_update",
        tags=["User Management"],
    )
    def partial_update(self, request, internal_id):
        """
        Update user details
        """
        return

    @swagger_auto_schema(
        operation_id="user_delete",
        tags=["User Management"],
    )
    def destroy(self, request, internal_id):
        """
        Delete user
        """
        return
