"""Bind to the port supplied by Railway, or 8000 locally."""
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
workers = 1
accesslog = "-"
errorlog = "-"
