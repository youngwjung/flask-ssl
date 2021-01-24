from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def index():
    print(request)
    if request.is_secure:
        return """
        <style>body {background-color: green}</style>
        <h1 style='color:white'>You are visiting a secure website!</h1>"
        """
    else:
        return """
        <style>body {background-color: red}</style>
        <h1 style='color:black'>You are visiting an insecure website!</h1>"
        """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)