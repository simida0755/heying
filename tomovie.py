from app import create_app

from flask_cors import CORS

app = create_app()


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0',port=8080,debug=app.config['DEBUG'])
