from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from fastapi import FastAPI

app = FastAPI()


# Mount static files like CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello from FastAPI!"})

@app.get("/api/greet")
async def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}


