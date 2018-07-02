import os
from waitress import serve
from app import server

serve(app,host="0.0.0.0",port=os.environ["PORT"])