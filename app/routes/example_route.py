from fastapi import APIRouter

router = APIRouter()

@router.get("/hello", summary="Saludo simple", description="Retorna un saludo desde la API de ejemplo.")
def hello():
    return {"message": "Hola desde la ruta de ejemplo"}

@router.get("/goodbye", summary="Despedida simple", description="Retorna una despedida desde la API de ejemplo.")
def goodbye():
    return {"message": "Adiós desde la ruta de ejemplo"}