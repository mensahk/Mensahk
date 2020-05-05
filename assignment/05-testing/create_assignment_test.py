import pytest
import System
import Staff

def create_assignment_test(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignment5', '05/10/21', 'databases')
    assert 'assignment5' in grading_system.usr.all_courses['databases']['assignments']


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


successful test
