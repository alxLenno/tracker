"""Import this application from the PythonAnywhere Web tab WSGI file."""
from app import create_app

application = create_app()
