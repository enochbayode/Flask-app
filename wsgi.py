"""App entry point."""
from flask_tutorial import create_app

app = create_app()
# app.config.from_pyfile('config.py')
app.config.from_object('config.DevConfig')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)