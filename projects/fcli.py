import typer

app = typer.Typer()

@app.command()
def hello():
    print("Hello")

@app.command()
def goodbye():
    print("Goodbye")

if __name__ == "__main__":
    app()