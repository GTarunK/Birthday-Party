from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates

tempaltes = Jinja2Templates(directory = "html_templates")

app = FastAPI()

userBirthDays = []

@app.get('/')
def root(request: Request):
        return tempaltes.TemplateResponse("form.html", {"request":request})

@app.get('/hi/{id}')
def root(id: int):
        return {"id": id}

@app.post('/save_form_data')
def save_form_data(Name: str = Form(...),Year: str = Form(...),Month: str = Form(...),Day:str = Form(...)):
        userBirthDays.append({"name":Name,"year":Year,"month":Month,"day":Day})
        print(userBirthDays)
        