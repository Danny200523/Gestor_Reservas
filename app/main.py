from fastapi import FastAPI
from app.routes.users.userRoutes import rout as users_router
from app.routes.example_route import router as example_router

app = FastAPI()

# app.include_router(auth_router, prefix="/api/auth")
app.include_router(example_router, prefix="/api")
app.include_router(users_router, prefix="/user")

@app.get("/")
def health_check():
    return {"status": "ok"}


