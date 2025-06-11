# run.py
from app import create_app
import webbrowser
import threading
import os

app = create_app()

def open_browser():
    webbrowser.open_new("http://localhost:5000/apidocs")

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") == "false":
        threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
