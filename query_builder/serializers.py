from rest_framework import serializers

class QueryParamsSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=False, allow_blank=True)
    industry = serializers.CharField(required=False, allow_blank=True)
    year_founded = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    employees_from = serializers.IntegerField(required=False)
    employees_to = serializers.IntegerField(required=False)

class QueryResultSerializer(serializers.Serializer):
    count = serializers.IntegerField()
