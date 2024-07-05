from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import QueryParamsSerializer, QueryResultSerializer
from .models import Company
from django.contrib.auth.decorators import login_required

@login_required
def query_builder(request):
    return render(request, 'query_builder/query_builder.html')

class QueryBuilderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = QueryParamsSerializer(data=request.data)
        if serializer.is_valid():
            keyword = serializer.validated_data.get('keyword')
            industry = serializer.validated_data.get('industry')
            year_founded = serializer.validated_data.get('year_founded')
            city = serializer.validated_data.get('city')
            state = serializer.validated_data.get('state')
            country = serializer.validated_data.get('country')
            employees_from = serializer.validated_data.get('employees_from')
            employees_to = serializer.validated_data.get('employees_to')

            query = Company.objects.all()

            if keyword:
                query = query.filter(keyword__icontains=keyword)
            if industry:
                query = query.filter(industry=industry)
            if year_founded:
                query = query.filter(year_founded=year_founded)
            if city:
                query = query.filter(city=city)
            if state:
                query = query.filter(state=state)
            if country:
                query = query.filter(country=country)
            if employees_from is not None and employees_to is not None:
                query = query.filter(employees__gte=employees_from, employees__lte=employees_to)

            count = query.count()
            result_serializer = QueryResultSerializer(data={'count': count})
            if result_serializer.is_valid():
                return Response(result_serializer.data)
            else:
                return Response(result_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
