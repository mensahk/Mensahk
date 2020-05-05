import pytest
import System
import Staff
import datetime



def passDue_test(grading_system):
    grading_system.login('goggins', 'augurrox')
    due = '04/16/20'
    present = datetime.datetime.now()
    assignment_due = datetime.datetime.strptime(due, '%m/%d/%y')
    grading_system.usr.create_assignment('assignment6', due, 'comp_sci')
    assert assignment_due.date() > present.date()

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
