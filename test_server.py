import requests

def test_students_api():
    name = "Lena"
    age = 22

    response=requests.post("http://127.0.0.1:5000/students", json={"name": name, "age": age})
    print(response.status_code)
    print(response.json())

def test_students_update():
    age = 21
    response=requests.patch("http://127.0.0.1:5000/students/1", json={"age": age})
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    test_students_update()