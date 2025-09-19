from fastapi import FastAPI
from app.routes.users.userRoutes import router as users_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth.authRoutes import router as auth_router

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
# Include auth routes (OAuth2 form login)
app.include_router(auth_router, prefix="/auth")


@app.get("/")
def health_check():
    return {"status": "ok"}


