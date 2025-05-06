# cli.py
import typer
from rich import print

app = typer.Typer()

@app.callback()
def main():
    print("[bold green]Welcome to MCP Orchestrator CLI![/bold green]")

@app.command()
def hello():
    """Say hello from the orchestrator."""
    print("👋 Hello from the MCP CLI!")

if __name__ == "__main__":
    app()
