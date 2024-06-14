# Online Store Inventory and Supplier Management API

Welcome to the Online Store Inventory and Supplier Management API! This API allows you to manage items and suppliers for an online store.

The Postman collection can be found [here](https://documenter.getpostman.com/view/20850921/2sA3XPE3bM).


Check out the project overview [here](https://www.loom.com/share/69f2287e3d1c48a1984a5e02585e87a3?sid=458b016b-4b48-43d3-aaa2-0940fa3cb2dd)

## Setup Instructions

To run the project locally follow the instructions below

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd prioritysoft_task
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

### Items
- **Create Item:** `POST /api/items/`
- **Get All Items:** `GET /api/items/`
- **Get Item by ID:** `GET /api/items/{id}/`
- **Update Item:** `PATCH /api/items/{id}/`
- **Delete Item:** `DELETE /api/items/{id}/`
- **Get Suppliers for Item:** `GET /api/items/{item_id}/suppliers/`

### Suppliers
- **Create Supplier:** `POST /api/suppliers/`
- **Get All Suppliers:** `GET /api/suppliers/`
- **Get Supplier by ID:** `GET /api/suppliers/{id}/`
- **Update Supplier:** `PATCH /api/suppliers/{id}/`
- **Delete Supplier:** `DELETE /api/suppliers/{id}/`
- **Get Items for Supplier:** `GET /api/suppliers/{supplier_id}/items/`

## Running Tests

To run the tests, execute the following command:
```bash
python manage.py test
