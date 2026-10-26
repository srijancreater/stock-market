from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .analyze import app as analyze_app

app = FastAPI()

@app.get("/")
def read_root():
    from .analyze import HTML_TEMPLATE
    return HTMLResponse(content=HTML_TEMPLATE)

app.include_router(analyze_app.router if hasattr(analyze_app, 'router') else analyze_app)
