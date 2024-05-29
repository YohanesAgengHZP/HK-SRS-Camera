from flask import Blueprint

# Create a Blueprint object for grouping routes related to streaming
streaming_routes = Blueprint('streaming_routes', __name__)

# Import the routes defined in streaming_routes.py
from . import streaming_routes