import pytest
import System
import TA

def checkTA_test(grading_system):
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('assignment_final', '05/14/22', 'cloud_computing')
    assert grading_system.usr.name == 'heisenberg'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
    
    
    unsuccessful test
