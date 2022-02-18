import requests
import unittest


class Flasktest(unittest.TestCase):

    def test_books(self):
        URL = 'http://localhost:5000/api/v1/books/'
        resp = requests.get(URL)
        self.assertEqual(resp.status_code, 200)
        print("Books works")

    def test_single_book_by_id(self):
        URL = 'http://localhost:5000/api/v1/books/4'
        resp = requests.get(URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['id'], 4)
        print("Single book works: id")

    def test_single_book_by_category(self):
        URL = 'http://localhost:5000/api/v1/books/novela'
        resp = requests.get(URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()[0]['category'], 'novela')
        print("Single book works: category")
        
    def test_create_book(self):
        URL = 'http://localhost:5000/api/v1/books/new'
        data = {
        "title":"",
        "category":"",
        "description":"",
        "image":"",
        "price": "",
        "seller":""
        }
        resp = requests.post(URL, json=data)
        self.assertEqual(resp.status_code, 200),
        print("Create book works")

    def test_delete_book(self):
        last_item = requests.get('http://localhost:5000/api/v1/books/')
        last_item = last_item.json()
        last_item_id = last_item[-1]['id']
        URL = f'http://localhost:5000/api/v1/books/delete/{last_item_id}'
        resp = requests.delete(URL)
        self.assertEqual(resp.status_code, 200)
        print("Delete book works")

if __name__ == "__main__":
    tester = Flasktest()
    tester.test_books()
    tester.test_single_book_by_id()
    tester.test_single_book_by_category()
    tester.test_create_book()
    tester.test_delete_book()

