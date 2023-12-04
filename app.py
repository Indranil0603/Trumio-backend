from flask import Flask
from models.connection import get_courses  # Assuming your folder structure is correct
app = Flask(__name__)

@app.route('/course')  # Change from @app.get to @app.route
def courses_show():
    try:
        courses = get_courses()
        return courses
    except Exception as e:
        print(e)
        return {"no data":"no"}