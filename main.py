import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.v1.endpoints import router as v1_router
from api.v2.endpoints import router as v2_router
from api.debug.endpoints import router as debug_router

app = FastAPI(
    title="AI Server Mock-up API",
    description="AI 서버의 v1, v2 및 디버그 라우트를 포함한 API 구조",
    version="0.0.2"
)

# Root path
@app.get("/")
async def root():
    # return {"message": "AI Schema Model API is running. Check /docs for API documentation."}
    return JSONResponse(status_code=400, content={
        "error": "INVALID_INPUT",
        "message": "AI Schema Model API is running. Check /docs for API documentation.",
    })

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

# Include routers with version prefix
app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
app.include_router(v2_router, prefix="/api/v2", tags=["v2"])
app.include_router(debug_router, prefix="/api/debug", tags=["Debug"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
