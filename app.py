
from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/get_code")
def send_code():
    # التأكد من مسار الملف
    file_path = os.path.join(os.getcwd(), "a3.py")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype='text/plain')
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
