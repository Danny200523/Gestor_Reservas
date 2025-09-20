from fastapi import FastAPI
from app.routes.users.userRoutes import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth.authRoutes import router as auth_router
from app.routes.reservas.reservaRoutes import router as reservas_router

''' 


    ####################################################################
    # Base de datos trabajada desde un cluster(nube) todo desde el .env#
    ####################################################################

    ####################################################################
    #                  COMANDO PARA INICIAR EL API                     #
    #   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000       #
    ####################################################################


'''

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origines, ajusta según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include user routes (includes register and JSON login)
app.include_router(users_router, prefix="/user")
app.include_router(auth_router, prefix="/auth")
app.include_router(reservas_router, prefix="/reservas")



@app.get("/")
def health_check():
    return {"status": "ok"}

