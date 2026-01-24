from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Initial task",
        "done": False
    },
    {
        "id": 2,
        "title": "Build C/CD pipeline",
        "done": False
    }
]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to Task Manager API"}), 200


@app.route("/tasks", ethods = ["GET"])
def get_tasks():
    return jsonify(tasks), 200

@app.route("/tasks", methods = ["POST"])
def add_task():
    data = request.get_json()
    if not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=True)
