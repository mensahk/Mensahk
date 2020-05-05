import pytest
import System
import json

def anotherAssignment_test(grading_system):
    username = 'saab'
    password = 'boomr345'
    course = 'databases'
    newAssignment = 'assignment000'
    newDueDate = '4/14/20'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(newAssignment, newDueDate, course)
    #professor are not allowed to carry this out.
    assert json_courses()[course]['assignments'][newAssignment]['due_date'] is None 

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

def json_courses():
    with open('Data/courses.json') as f:
        courses = json.load(f)
    return courses
