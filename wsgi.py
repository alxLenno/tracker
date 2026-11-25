"""WSGI entry point for production hosting."""
from app import create_app

application = create_app()
