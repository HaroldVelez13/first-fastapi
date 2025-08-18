#entrypoint.py
import app.models as model # importamos todos los modelos dentro del archivo
from app.config import engine

# El motor mapea y crea el modelo en la DB
model.Base.metadata.create_all(bind=engine)