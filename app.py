from flask import Flask, jsonify, request
from db import get_students, insert_student, update_student, delete_student, get_student
app = Flask(__name__)

class Test:
    def __init__(self):
        self.name = name
        self.age = age

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello world!"})

@app.route('/students', methods=["GET", "POST", "PATCH", "DELETE"])
def students_api():
    if request.method == "GET":
        students = get_students()
        return jsonify(students)
    elif request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")
        insert_student(name, age)
        return jsonify({"name": name, "age": age}), 201
    else:
        return jsonify({"message": "Method not allowed"}), 405


@app.route('/students/<int:id>', methods=["PATCH", "DELETE", "GET"])
def student_api(id):
    if request.method == "PATCH":
        data = request.get_json(id)
        name = data.get("name")
        age = data.get("age")
        update_student(id, name, age)
        return jsonify({"name": name, "age": age})
    elif request.method =="DELETE":
        delete_student(id)
        return "", 204
    elif request.method == "GET":
        student = get_student(id)
        if not student:
            return jsonify({"message": "Not found"}), 404
        return jsonify(student)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

