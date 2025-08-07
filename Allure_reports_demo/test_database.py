import pytest
from modules.database import Database
import allure
from allure_commons.types import AttachmentType


@pytest.fixture
def db():
    """Provide a fresh instance of database class and clear up after the test runs"""
    database = Database()
    yield database  # yields for test to run after test runs proceeds to next line
    database.data.clear()  # Clears database


@allure.severity(allure.severity_level.CRITICAL)
def test_add_user(db):
    db.add_user(1, "javid")

    assert db.get_user(1) == "javid"


@allure.severity(allure.severity_level.CRITICAL)
def test_add_duplicate_user(db):
    db.add_user(1, "javid")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "david")


@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user(db):
    db.add_user(2, "akram")
    db.delete_user(2)
    assert db.get_user(2) is None
