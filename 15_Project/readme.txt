Learn Permission
1.Settings.py --> iT WILL APPLY TO ALL classes
   REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

2.We Can also write Class Based or Function BAsed.

In Class Based.

from rest_framework.permissions import IsAuthenticated
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

In Function Based
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)

Types
1. ALLOWANY -->
2. IsAuthenticated -->Only login user can access
3. IsAdminUser --> Only Admin can access
4.IsAuthenticatedorReadonly --> Login user can access edit, rest can just view
5.CustomPermission