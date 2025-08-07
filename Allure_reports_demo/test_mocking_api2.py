import pytest
import allure
from modules.api_mock_2 import UserService,APIClient

@allure.epic("API Mock")
@allure.feature("Response Headers")
@allure.title("Validate Standard Headers")
@allure.severity(allure.severity_level.TRIVIAL)
def test_get_username_with_mock(mocker):
    mock_api_client=mocker.Mock(spec=APIClient) #mocking class also can mock method also

    mock_api_client.get_user_data.return_value={"id":1,"name":"Aladin"}
    service=UserService(mock_api_client)
    result=service.get_username(1)

    #Assert
    assert result=="ALADIN"
    mock_api_client.get_user_data.assert_called_once_with(1)