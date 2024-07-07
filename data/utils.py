import csv
# import logging
from unidecode import unidecode
from query_builder.models import Company
from django.utils.encoding import smart_str
# logger = logging.getLogger(__name__)

def process_csv(file):
    # logger.info("Starting CSV processing")
    reader = csv.DictReader(file.read().decode('utf-8-sig').splitlines())
    
    for row in reader:
        try:
            # Extracting city and state from locality
            locality = row.get('locality', '').split(', ')
            city = locality[0].strip() if len(locality) > 0 else None
            state = locality[1].strip() if len(locality) > 1 else None
            
            # Cleaning and validating data
            name = unidecode(row['name']) if row['name'] else None
            domain = unidecode(row['domain']) if row['domain'] else None
            year_founded = clean_int(row['year founded'])
            industry = unidecode(row['industry']) if row['industry'] else None
            size_range = unidecode(row['size range']) if row['size range'] else None
            locality = unidecode(row['locality']) if row['locality'] else None
            city = unidecode(city) if city else None
            state = unidecode(state) if state else None
            country = unidecode(row['country']) if row['country'] else None
            linkedin_url = unidecode(row.get('linkedin url', '')) if row.get('linkedin url', '') else None
            current_employees = clean_int(row['current employee estimate'])
            total_employees_estimate = clean_int(row['total employee estimate'])

            # Ensuring all string fields are properly encoded
            company = Company(
                name=smart_str(name),
                domain=smart_str(domain),
                year_founded=year_founded,
                industry=smart_str(industry),
                size_range=smart_str(size_range),
                locality=smart_str(locality),
                city=smart_str(city),
                state=smart_str(state),
                country=smart_str(country),
                linkedin_url=smart_str(linkedin_url) if linkedin_url else None,
                current_employees=current_employees,
                total_employees_estimate=total_employees_estimate
            )
            company.save()
            # logger.info(f"Saved company: {company.name}")
        except Exception as e:
            # logger.error(f"Error saving company: {e}")
            pass

def clean_int(value):
    """Converts value to integer if possible, otherwise returns None."""
    if value.strip():  # Check if the value is not empty after stripping whitespace
        try:
            return int(value)
        except ValueError:
            return None
    return None

