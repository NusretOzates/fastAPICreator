# FastAPI Creator CLI
This is a CLI application written with [Typer](https://typer.tiangolo.com/) from the creator of [FastAPI](https://fastapi.tiangolo.com/)!

    Usage: fast_creator.py [OPTIONS] PROJECT_NAME

    Arguments:
      PROJECT_NAME  [required]
    
    Options:
      --routers TEXT                  Router names to create, write every router
                                      name with spaces  [default: ]
    
      --models TEXT                   Model names to create, write every router
                                      name with spaces  [default: ]
    
      --install-completion [bash|zsh|fish|powershell|pwsh]
                                      Install completion for the specified shell.
      --show-completion [bash|zsh|fish|powershell|pwsh]
                                      Show completion for the specified shell, to
                                      copy it or customize the installation.
    
      --help                          Show this message and exit.

Usage Example:

    python fast_creator.py fastboy --models "user team" --routers "users teams"

Example Result:

    fastboy
        │   main.py
        │
        └───app
            │   main.py
            │   __init__.py
            │
            ├───models
            │       team.py
            │       user.py
            │       __init__.py
            │
            └───routers
                    teams.py
                    users.py
                    __init__.py
