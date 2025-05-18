# src/uvx_tool_demo/__init__.py

import typer

app = typer.Typer()


@app.command()
def hello(name: str = "world"):
    """Say hello to someone."""
    typer.echo(f"👋 Hello, {name}!")
