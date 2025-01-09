from app import create_app

app = create_app()

@app.route('/')
def health_check():
    return "Flask app is running on Vercel!", 200
