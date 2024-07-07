from rest_framework import serializers

class QueryParamsSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=False, allow_blank=True)
    industry = serializers.CharField(required=False, allow_blank=True)
    year_founded = serializers.IntegerField(required=False, allow_null=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    employees_from = serializers.IntegerField(required=False, allow_null=True)
    employees_to = serializers.IntegerField(required=False, allow_null=True)

    def to_internal_value(self, data):
        for field in ['year_founded', 'employees_from', 'employees_to']:
            if field in data and data[field] == '':
                data[field] = None
        return super().to_internal_value(data)

class QueryResultSerializer(serializers.Serializer):
    count = serializers.IntegerField()
