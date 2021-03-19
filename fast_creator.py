import typer
import os


def main(project_name: str,
         routers: str = typer.Option(default='', help='Router names to create, write every router name with spaces'),
         models: str = typer.Option(default='', help='Model names to create, write every router name with spaces')):
    typer.confirm(f'Project name: {project_name} \n routers: {routers} \n models: {models}', default=True, abort=True)
    # Create the base directory
    os.mkdir(project_name)
    # Create high level main file
    create_base_main(project_name)

    # Create the app package
    os.mkdir(f'{project_name}/app')
    open(f'{project_name}/app/__init__.py', 'w').close()

    # If there are model classes to create then create these classes as well
    if models != '':
        create_models(project_name, models.split())

    # If there are routers to create then create these as well
    if routers != '':
        create_routers(project_name, routers.split())

    # Create the base fastapi main file. FastAPI object will be created here
    create_main(project_name, routers.split())


def create_base_main(project_name: str):
    main_file = """import uvicorn
from app.main import app

if __name__ == '__main__':
    uvicorn.run(app)"""
    with open(f'{project_name}/main.py', 'w', encoding='utf8') as file:
        file.write(main_file)


def create_main(project_name: str, router_names: []):
    open(f'{project_name}/app/main.py', 'w').close()
    lines = [
        'from fastapi import FastAPI\n',
    ]

    for router in router_names:
        lines.append(f'from .routers.{router} import {router}\n')

    lines.append('\napp = FastAPI()\n\n')

    for router in router_names:
        lines.append(f"app.include_router({router},prefix='/{router}')\n")

    lines.append("""
    
@app.get('/')
def hello():
    return 'Hello World!'""")
    with open(f'{project_name}/app/main.py', 'w', encoding='utf8') as file:
        file.writelines(lines)


def create_routers(project_name: str, router_names: []):
    os.mkdir(f'{project_name}/app/routers')
    open(f'{project_name}/app/routers/__init__.py', 'w').close()

    for router in router_names:
        with open(f'{project_name}/app/routers/{router}.py', 'w', encoding='utf8') as file:
            file.write(f"""from fastapi import APIRouter


{router} = APIRouter()
""")


def create_models(project_name: str, model_names: []):
    os.mkdir(f'{project_name}/app/models')
    open(f'{project_name}/app/models/__init__.py', 'w').close()

    for model in model_names:
        with open(f'{project_name}/app/models/{model}.py', 'w', encoding='utf8') as file:
            file.write(f"""from pydantic import BaseModel


class {model.capitalize()}(BaseModel):
    pass""")


if __name__ == "__main__":
    typer.run(main)
