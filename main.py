from flask import Flask
from views import views as product_module

app = Flask(__name__)

app.register_blueprint(product_module)

if __name__ == '__main__':
    app.run(debug=True, port=5500)