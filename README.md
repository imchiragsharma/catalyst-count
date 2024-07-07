# Django Project for CSV Data Upload and Query Building

## Overview

This Django project allows users to upload large CSV files, update the database with the contents of the uploaded file, and filter the data using a web interface. The project includes features like dynamic form fields that are populated from the database and visual progress bars during file uploads.

## Features

- **CSV Upload**: Upload large CSV files to update the database.
- **Dynamic Filtering**: Filter data dynamically based on fields like industry, city, state, country, and year founded.
- **Progress Bar**: Visual progress bar during CSV file uploads.
- **Admin Interface**: View and manage uploaded data through the Django admin interface.

## Directory Structure


## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- PostgreSQL

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/catalyst-count.git
    cd catalyst-count
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
   Create a .env file in the project root and add the following environment variables:
    ```sh
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT =

    ```

6. **Run database migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

### Usage

1. **Access the admin interface**:
    Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials.

2. **Upload CSV files**:
    Go to the CSV upload page and select a file to upload. The progress bar will display the upload status.

3. **Filter data**:
    Use the filter form on the main page to dynamically filter the data based on available options.

### API Endpoints

- **GET /query_builder/api/filter-options/**: Fetch distinct filter options from the database.
- **POST /query_builder/api/query-builder/**: Filter data based on selected criteria.

### Upload CSV
- Navigate to the CSV upload page.
- Upload your CSV file and wait for the progress bar to complete.
- Filter Data
   
### Navigate to the query builder page.
- Use the form to select your filter criteria.
- Submit the form to see the count of records matching the criteria.


