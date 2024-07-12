# Django Inline Admin: TabularInline and StackedInline Examples

## Prerequisites

- Python 3.8+
- Django 4

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MehediMK/Django_Inline_Admin.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django_Inline_Admin
   python -m venv venv
   source venv/bin/activate (*linux) or venv\Scripts\activate (*Windows)
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py collectstatic
   python manage.py makemigrations
   python manage.py migrate
   ```
5. create superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run project locally
   ```bash
   python manage.py runserver
   ```