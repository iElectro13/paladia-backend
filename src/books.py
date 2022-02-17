from flask import Blueprint, request, jsonify
from src.database import Books, db

books = Blueprint("books", __name__,url_prefix="/api/v1/books")

@books.get("/")
def get_books():
    all_books = Books.query.all()
    data = []
    for book in all_books:
        data.append({
            'id': book.id,
            'title': book.title,
            'category': book.category,
            'description': book.description,
            'image': book.image,
            'price': book.price,
            'seller': book.seller,
            'created_at': book.created_at,
            'updated_at': book.updated_at,
        })
    return jsonify(data)

@books.get("/<int:id>")
def get_book_by_id(id):
    book = Books.query.filter_by(id = id).first()
    return jsonify({
            'id': book.id,
            'title': book.title,
            'category': book.category,
            'description': book.description,
            'image': book.image,
            'price': book.price,
            'seller': book.seller,
            'created_at': book.created_at,
            'updated_at': book.updated_at,
        })

@books.get("/<category>")
def get_books_by_category(category):
    all_books = Books.query.filter_by(category= category).all()
    data = []
    for book in all_books:
        data.append({
            'id': book.id,
            'title': book.title,
            'category': book.category,
            'description': book.description,
            'image': book.image,
            'price': book.price,
            'seller': book.seller,
            'created_at': book.created_at,
            'updated_at': book.updated_at,
        })
    return jsonify(data)

@books.post("/new")
def create_book():
    title = request.json['title']
    category = request.json['category']
    description = request.json['description']
    image = request.json['image']
    price = request.json['price']
    seller = request.json['seller']

    book = Books(title=title, category=category, description=description, image=image, price=price, seller=seller)

    db.session.add(book)
    db.session.commit()
    return "New Book Created"


"""
Esquema para enviar post request:
{
    "title":"Cien años de soledad",
    "category":"Realismo magico",
    "description":"Cien años de soledad es una novela del escritor colombiano Gabriel García Márquez, ganador del Premio Nobel de Literatura en 1982.",
    "image":"no-image",
    "price": 100,
    "seller":"Enmanuel Pereira"
}
"""