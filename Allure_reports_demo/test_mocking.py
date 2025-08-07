import pytest
from modules.api_mock import get_weather

def test_get_weather(mocker):
    mock_get=mocker.patch("modules.api_mock.requests.get")
    mock_response = mocker.Mock()
    mock_response.status_code=200
    mock_response.json.return_value={"temperature":25,"condition": "Sunny"}
    mock_get.return_value = mock_response
    result=get_weather("Dubai")

    assert result == {"temperature":25,"condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")