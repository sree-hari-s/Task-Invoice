# Django - Task

## Create a Django application (Django Rest Framework) using the given information:

- You need to create a single url `/invoices/` for this

```python
/invoices/
/invoices/<int:pk>/
```
- Create two Django models viz. Invoice and Invoice Detail.
  - Invoice model fields -> Date, Invoice CustomerName.
  - InvoiceDetail model fields -> invoice (ForeignKey), description, quantity, unit_price, price.
- Create APIs using Django Rest Framework for all the HTTP methods for the invoice models. 
- The API should also accept invoice_details in the payload and create/update the associated invoice details too 
- Create test cases to test all the API endpoints.

## Installation

Follow these steps to set up and run the GreatKart E-commerce Website on your local machine:

1. Clone the GitHub Repository:

   ```bash
   git clone https://github.com/sree-hari-s/Task-Invoice.git
   ```

2. Install and create a virtual environment:

   ```cmd
   virtualenv env
   ```

3. Activate the virtual environment:
   - On Windows:

     ```cmd
     env\Scripts\activate
     ```

4. Install the project requirements:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` File and Fill in Required Environment Variables
   In your project directory, create a `.env` file and fill in the required environment variables as follows:

   ```python
   SECRET_KEY=django_secret_key
   DEBUG=True/False
   ```
6. Migrate the project to the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the project:

   ```bash
   python manage.py runserver
   ```
