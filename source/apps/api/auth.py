from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email, ValidationError

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from source.apps.core.models.user.models import User, UserPasswordRecoveryRequest
from source.apps.api.user.serializers import (
    AuthSerializer,
    PasswordRecoverySerializer,
    ChangePasswordSerializer
)
from source.apps.core.email import send_email


class CursorSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    ordering = '-id'
    max_page_size = 20
    paginate_by = 20


class AuthViewSet(viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = AuthSerializer
    http_method_names = ['get', 'post']
    pagination_class = CursorSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthSerializer
        if self.action == 'password_recovery_request':
            return PasswordRecoverySerializer
        if self.action == 'password_recovery_process':
            return ChangePasswordSerializer
        return AuthSerializer

    def list(self, request):
        """
        Dummy method implemented for generating the docs
        :return:
        """
        return Response({True})

    @csrf_exempt
    @permission_classes((AllowAny,))
    @action(methods=['post'], detail=False)
    def login(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response({'error': _('Please enter your email and/or password')}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if not user:
            return Response({'error': _('Invalid credentials')}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'first_name': user.first_name,
            'is_authenticated': True,
            'user_id': user.pk,
            'email': user.email,
            'is_staff': user.is_staff
        },  status=HTTP_200_OK)

    @csrf_exempt
    @permission_classes((AllowAny,))
    @action(methods=['post'], detail=False)
    def password_recovery_request(self, request):
        email = request.data.get("email")

        try:
            validate_email(email)
        except ValidationError as e:
            return Response({'error': e.message}, status=HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as e:
            return Response({'error': _('This email is not registered')}, status=HTTP_404_NOT_FOUND)

        try:
            UserPasswordRecoveryRequest.objects.get(user=user)
            return Response({
                'error': _('You have already requested to change your password.')
            }, status=HTTP_400_BAD_REQUEST)
        except UserPasswordRecoveryRequest.DoesNotExist:
            pass

        try:
            token = default_token_generator.make_token(user)

            send_email(
                to=email,
                subject=_('(app)%s - password reset'),
                data={
                    'username': user.first_name,
                    'token': token,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode()
                }
            )

            uprr = UserPasswordRecoveryRequest(user=user, token=token)
            uprr.save()

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=HTTP_400_BAD_REQUEST)

        return Response({True})

    @csrf_exempt
    @permission_classes((AllowAny,))
    @action(methods=['post'], detail=False)
    def password_recovery_process(self, request):
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")
        uidb64 = request.data.get("uid")
        token = request.data.get("token")

        if new_password != confirm_password:
            return Response({'error': _("Password don't match")}, status=HTTP_400_BAD_REQUEST)

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': _('Account does not exist')}, status=HTTP_404_NOT_FOUND)

        if not default_token_generator.check_token(user, token):
            return Response({'error': _('Invalid token')}, status=HTTP_404_NOT_FOUND)

        try:
            user.set_password(new_password)
            user.save()

            UserPasswordRecoveryRequest.objects.filter(user=user).delete()

            token, b = Token.objects.get_or_create(user=user)
        except Exception:
            return Response({
                'error': _("We couldn't reset the password. Please try again later.")
            }, status=HTTP_400_BAD_REQUEST)

        return Response({
            'token': token.key,
            'first_name': user.first_name,
            'is_authenticated': True,
            'password_changed': True,
        })
