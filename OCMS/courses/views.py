from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
@api_view(['GET', 'POST'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated = paginator.paginate_queryset(data, request)
        serializer = CategorySerializer(paginated, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def category_detail(request, id):
    try:
        obj = Category.objects.get(id=id)
    except:
        return Response({'error': 'Category not found'}, status=404)
    if request.method == 'GET':
        return Response(CategorySerializer(obj).data)
    if request.method == 'PUT':
        serializer = CategorySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        serializer = CategorySerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'POST'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def course_list(request):
    if request.method == 'GET':
        data = Course.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated = paginator.paginate_queryset(data, request)
        serializer = CourseSerializer(paginated, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def course_detail(request, id):
    try:
        obj = Course.objects.get(id=id)
    except:
        return Response({'error': 'Course not found'}, status=404)
    if request.method == 'GET':
        return Response(CourseSerializer(obj).data)
    if request.method == 'PUT':
        serializer = CourseSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        serializer = CourseSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'POST'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def module_list(request):
    if request.method == 'GET':
        data = Module.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated = paginator.paginate_queryset(data, request)
        serializer = ModuleSerializer(paginated, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def module_detail(request, id):
    try:
        obj = Module.objects.get(id=id)
    except:
        return Response({'error': 'Module not found'}, status=404)
    if request.method == 'GET':
        return Response(ModuleSerializer(obj).data)
    if request.method == 'PUT':
        serializer = ModuleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        serializer = ModuleSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'POST'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def lecture_list(request):
    if request.method == 'GET':
        data = Lecture.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated = paginator.paginate_queryset(data, request)
        serializer = LectureSerializer(paginated, many=True)
        return paginator.get_paginated_response(serializer.data)
    if request.method == 'POST':
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@cache_page(100)
@permission_classes([IsAuthenticated])
def lecture_detail(request, id):
    try:
        obj = Lecture.objects.get(id=id)
    except:
        return Response({'error': 'Lecture not found'}, status=404)
    if request.method == 'GET':
        return Response(LectureSerializer(obj).data)
    if request.method == 'PUT':
        serializer = LectureSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        serializer = LectureSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)