import requests

def delete_by_id(id):
    requests.delete(f'http://localhost:5000/api/v1/books/delete/{id}')