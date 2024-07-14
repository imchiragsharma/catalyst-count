from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import QueryParamsSerializer, QueryResultSerializer
from .models import Company
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging

logger = logging.getLogger('django')

@login_required
def query_builder(request):
    industries = Company.objects.values_list('industry', flat=True).distinct()
    years_founded = Company.objects.values_list('year_founded', flat=True).distinct()
    cities = Company.objects.values_list('city', flat=True).distinct()
    states = Company.objects.values_list('state', flat=True).distinct()
    countries = Company.objects.values_list('country', flat=True).distinct()
    
    context = {
        'industries': list(industries),
        'cities': list(cities),
        'states': list(states),
        'countries': list(countries),
        'years_founded': list(years_founded),
    }
    logger.debug("Filter Options Data: %s", context)

    return render(request, 'query_builder/query_builder.html', context)


class QueryBuilderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        return self.process_request(request)

    def process_request(self, request):
        logger.info("Received query request")
        
        # Create a mutable copy of the QueryDict
        if request.method == 'GET':
            mutable_data = QueryDict(request.GET.urlencode(), mutable=True)
        else:
            mutable_data = request.data.copy()
        
        logger.debug(f"Request data: {mutable_data}")
        
        serializer = QueryParamsSerializer(data=mutable_data)
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
                query = query.filter(
                    Q(name__icontains=keyword) | 
                    Q(domain__icontains=keyword) |
                    Q(industry__icontains=keyword) |
                    Q(city__icontains=keyword) |
                    Q(state__icontains=keyword) |
                    Q(country__icontains=keyword)
                )
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
                query = query.filter(current_employees__gte=employees_from, current_employees__lte=employees_to)

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
        
        
from django.http import QueryDict

@login_required
def download_csv(request):
    # Create a mutable copy of the QueryDict
    mutable_get = QueryDict(request.GET.urlencode(), mutable=True)

    # Extract the filter parameters from the mutable QueryDict
    keyword = mutable_get.get('keyword', '')
    industry = mutable_get.get('industry', '')
    year_founded = mutable_get.get('year_founded')
    city = mutable_get.get('city', '')
    state = mutable_get.get('state', '')
    country = mutable_get.get('country', '')
    employees_from = mutable_get.get('employees_from')
    employees_to = mutable_get.get('employees_to')

    # Query the Company model based on the filters
    query = Company.objects.all()

    if keyword:
        query = query.filter(
            Q(name__icontains=keyword) | 
            Q(domain__icontains=keyword) | 
            Q(industry__icontains=keyword) | 
            Q(city__icontains=keyword) | 
            Q(state__icontains=keyword) | 
            Q(country__icontains=keyword) | 
            Q(linkedin_url__icontains=keyword)
        )

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
    
    if employees_from:
        query = query.filter(current_employees__gte=employees_from)
    
    if employees_to:
        query = query.filter(current_employees__lte=employees_to)

    # Create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Domain', 'Year Founded', 'Industry', 'Size Range', 'Locality', 'City', 'State', 'Country', 'LinkedIn URL', 'Current Employees', 'Total Employees Estimate'])

    for company in query:
        writer.writerow([
            company.id, company.name, company.domain, company.year_founded, company.industry, 
            company.size_range, company.locality, company.city, company.state, company.country, 
            company.linkedin_url, company.current_employees, company.total_employees_estimate
        ])

    return response