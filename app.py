from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running"

@app.route("/get_code")
def send_code():
    file_path = os.path.join(os.getcwd(), "a3.py")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype='text/plain')
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # تأكد أن PORT مأخوذ من متغيرات البيئة
    port = int(os.environ.get("PORT", 8080))  # Railway يعطي PORT متغير
    print(f"🚀 Starting server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
