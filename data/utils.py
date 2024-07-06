import csv
import logging
from query_builder.models import Company

# logger = logging.getLogger(__name__)

def process_csv(file):
    # logger.info("Starting CSV processing")
    reader = csv.DictReader(file.read().decode('utf-8-sig').splitlines())
    
    for row in reader:
        try:
            name = row.get('name', '')  # Using .get() with a default value to handle missing keys gracefully
            domain = row.get('domain', '')
            year_founded = clean_int(row.get('year founded', ''))
            industry = row.get('industry', '')
            size_range = row.get('size range', '')
            locality = row.get('locality', '')
            city = row.get('city', '')
            state = row.get('state', '')
            country = row.get('country', '')
            linkedin_url = row.get('linkedin url', '') if row.get('linkedin url', '') else None
            current_employees = clean_int(row.get('current employee estimate', ''))
            total_employees_estimate = clean_int(row.get('total employee estimate', ''))

            company = Company(
                name=name,
                domain=domain,
                year_founded=year_founded,
                industry=industry,
                size_range=size_range,
                locality=locality,
                country=country,
                linkedin_url=linkedin_url,
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

