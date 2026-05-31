from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.recipe_router import router as recipe_router

app = FastAPI(
    title="BrewHelpy API",
    description="API for BrewHelpy backend"
)

# CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to BrewHelpy API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


app.include_router(recipe_router, prefix="/recipes", tags=["recipes"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)