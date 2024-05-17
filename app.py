import os
from dotenv import load_dotenv
from waitress import serve

from project import create_app

load_dotenv()

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8000
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"

if __name__ == '__main__':
    if os.getenv('SERVE') == DEVELOPMENT:
        create_app(os.getenv('DATABASE_URI')).run(port=DEVELOPMENT_PORT, debug=True)

    elif os.getenv('SERVE') == PRODUCTION:
        serve(create_app(os.getenv('DATABASE_URI')), host=HOST, port=PRODUCTION_PORT)