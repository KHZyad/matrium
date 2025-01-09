from app import create_app

app = create_app()

@app.route('/')
def health_check():
    return "Matrium!", 200
