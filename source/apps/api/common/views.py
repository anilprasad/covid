from django.template.exceptions import TemplateDoesNotExist

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from source.apps.core.permissions import IsOwnerOrAdminPermission
from source.apps.core.tasks.core.tasks import send_mail


class CommonViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ('list',):
            self.permission_classes = [AllowAny, ]
        if self.action in ('send_email',):
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdminPermission, ]

        return super(CommonViewSet, self).get_permissions()

    @action(
        methods=['post'],
        detail=False,
        url_path=r'send-email',
        url_name='send_email'
    )
    def send_email(self, request):
        """
        Send email to one or multiple users. The request param should contain an array with
        valid user ids. Example: id = [1,2,3,4]

        :param request:
        :return:
        """
        try:
            template = 'email/freetext.html'
            send_mail.delay(
                subject='Test',
                to=['rada.calin@gmail.com'],
                template=template,
                data={
                    'subject': 'Test',
                    'text': 'Bla bla bla free text'
                }
            )
        except TemplateDoesNotExist:
            return Response({
                'error': 'Template %s does not exist' % template
            }, HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'error': str(e)
            }, HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'ok'
        }, HTTP_200_OK)

    def list(self, request):
        """
        Retrieve common data
        :param request:
        :return:
        """
        data = {
            'version': '1.0',
        }

        return Response(data)
