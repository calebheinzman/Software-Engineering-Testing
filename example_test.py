import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    grading_system.login('thtrhg', 'fhjhjdhjdfh')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem