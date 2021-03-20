import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates
# The templates are supposed to be just a local reference, but when running with the vscode runners, this fails.
# the solution is to use a full absolute path.  
templates = Jinja2Templates('/workspaces/modern-apis-with-fastapi/ch05-realistic-api-roel/templates')
router = fastapi.APIRouter()

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')

