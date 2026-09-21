import pytest
from src.registration import Registration


@pytest.mark.unit
def test_registration_fee_is_paid():
    # Arrange
    registration = Registration()

    # Act
    result = registration.fee_is_paid()

    # Assert
    assert result is True
