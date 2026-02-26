from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.models import User
from courses.models import Course
from enrollments.models import Enrollment
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analytics(request):
    data = {
        "total_users": User.objects.count(),
        "total_courses": Course.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
    }
    return Response(data)