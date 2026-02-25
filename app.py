from flask import Flask, Response, jsonify
import os
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Server is running",
        "cwd": os.getcwd(),
        "files": os.listdir()
    })

@app.route("/get_code")
def send_code():
    # محاولة إيجاد الملف في مسارات مختلفة
    possible_paths = [
        os.path.join(os.getcwd(), "a3.py"),
        os.path.join(os.path.dirname(__file__), "a3.py"),
        "a3.py"
    ]
    
    for file_path in possible_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                return Response(content, mimetype='text/plain')
            except Exception as e:
                return jsonify({
                    "error": f"Error reading file: {str(e)}",
                    "path": file_path
                }), 500
    
    # إذا ما لقينا الملف
    return jsonify({
        "error": "File not found",
        "cwd": os.getcwd(),
        "files": os.listdir(),
        "searched_paths": possible_paths
    }), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting server on port {port}")
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📄 Files: {os.listdir()}")
    app.run(host="0.0.0.0", port=port, debug=False)
