from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import QueryParamsSerializer, QueryResultSerializer
from .models import Company
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

@login_required
def query_builder(request):
    industries = Company.objects.values_list('industry', flat=True).distinct()
    years_founded = Company.objects.values_list('year_founded', flat=True).distinct()
    cities = Company.objects.values_list('city', flat=True).distinct()
    states = Company.objects.values_list('state', flat=True).distinct()
    countries = Company.objects.values_list('country', flat=True).distinct()
    
    context = {
        'industries': industries,
        'years_founded': years_founded,
        'cities': cities,
        'states': states,
        'countries': countries,
    }
    
    return render(request, 'query_builder/query_builder.html', context)






class QueryBuilderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logger.info("Received query request")
        logger.debug(f"Request data: {request.data}")
        
        serializer = QueryParamsSerializer(data=request.data)
        if serializer.is_valid():
            logger.info("Serializer is valid")
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
            logger.info(f"Query count: {count}")

            result_serializer = QueryResultSerializer(data={'count': count})
            if result_serializer.is_valid():
                return Response(result_serializer.data)
            else:
                logger.error(f"Result serializer errors: {result_serializer.errors}")
                return Response(result_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class QueryBuilderView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = QueryParamsSerializer(data=request.data)
#         if serializer.is_valid():
#             keyword = serializer.validated_data.get('keyword')
#             industry = serializer.validated_data.get('industry')
#             year_founded = serializer.validated_data.get('year_founded')
#             city = serializer.validated_data.get('city')
#             state = serializer.validated_data.get('state')
#             country = serializer.validated_data.get('country')
#             employees_from = serializer.validated_data.get('employees_from')
#             employees_to = serializer.validated_data.get('employees_to')

#             query = Company.objects.all()

#             if keyword:
#                 query = query.filter(keyword__icontains=keyword)
#             if industry:
#                 query = query.filter(industry=industry)
#             if year_founded:
#                 query = query.filter(year_founded=year_founded)
#             if city:
#                 query = query.filter(city=city)
#             if state:
#                 query = query.filter(state=state)
#             if country:
#                 query = query.filter(country=country)
#             if employees_from is not None and employees_to is not None:
#                 query = query.filter(employees__gte=employees_from, employees__lte=employees_to)

#             count = query.count()
#             result_serializer = QueryResultSerializer(data={'count': count})
#             if result_serializer.is_valid():
#                 return Response(result_serializer.data)
#             else:
#                 return Response(result_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
