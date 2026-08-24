# app/api/routes/__init__.py

from .cruise_search import fetch_cruise
from .ship_details import fetch_ship

__all__ = ["fetch_cruise","fetch_ship"]