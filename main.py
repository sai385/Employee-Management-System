from fastapi import FastAPI
from app.database.db import engine, Base
from app.routes.emproute import router as emproute
from app.routes.signup import router as signup


app = FastAPI(
    title="Employee Management API",
    description="CRUD APIs for Employee table using FastAPI & SQLAlchemy",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)


app.include_router(emproute)
app.include_router(signup)



@app.get("/")
def root():
    return {"message": "Employee API is running"}


from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Employee Management API",
        version="1.0.0",
        description="API with JWT Bearer authentication for protected routes only",
        routes=app.routes,
    )

   
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

  
    protected_paths = ["/employees", "/departments"]  
    for path in openapi_schema["paths"]:
        if any(path.startswith(p) for p in protected_paths):
            for method in openapi_schema["paths"][path]:
                if isinstance(openapi_schema["paths"][path][method], dict):
                    openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



