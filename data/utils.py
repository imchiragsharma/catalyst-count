import csv
from query_builder.models import Company

def process_csv(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        Company.objects.create(
            # id=row['id'],
            name=row['name'],
            domain=row['domain'],
            year_founded=int(row['year_founded']),
            industry=row['industry'],
            size_range=row['size range'],
            locality=row['locality'],
            country=row['country'],
            linkedin_url=row['LinkedIn URL'],
            current_employees=int(row['current employees']),
            total_employees_estimate=int(row['total employees estimate'])
        )
        Company.save()
