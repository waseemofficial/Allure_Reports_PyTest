# import allure_pytest
from modules.main import division, is_prime
import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# severity level on class level and also can be method level the decurator is same
# severity can be NORMAL, MINORM, CRITICAL AND BLOCKING
@allure.severity(allure.severity_level.NORMAL)
class TestGenralSetupOptions:
    @pytest.fixture(autouse=True)  # this runs before every subsequent test
    def setup_and_teardown(self):
        options = Options()
        options.add_argument("--headless")  # Run in headless mode for CI/CD
        # options.add_argument("--start-maximized")  # optional

        # Automatically get the matching ChromeDriver version
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        yield  # Test runs here

        self.driver.quit()

    def test_logo(self):
        self.driver.get("https://www.google.com")
        current_url = self.driver.current_url
        assert "google.com" in current_url, f"Expected 'google.com' in URL, but got {current_url}"

    def test_listemployes(self):
        pytest.skip("list not found - test data not available")

    # with this the browser is not opened
    @pytest.mark.skip(reason="login test not implemented yet")
    def test_login(self):
        pass

    # severity level on method level and also can be class level the decurator is same
    # severity can be NORMAL, MINORM, CRITICAL AND BLOCKING
    @allure.severity(allure.severity_level.MINOR)
    def testScteenShot(self):
        self.driver.get("https://juice-shop.herokuapp.com/")
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="juice-shop ", attachment_type=AttachmentType.PNG)
        assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            division(10, 0)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("num, expeted", [(1, False), (2, True), (3, True), (4, False), (17, True), (18, False), (19, True), (25, False)])
    def check_is_prime(self, num, expeted):
        assert is_prime(num) == expeted
