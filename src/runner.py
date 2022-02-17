from src import create_app
from flask_cors import CORS

application = create_app()
CORS(application)