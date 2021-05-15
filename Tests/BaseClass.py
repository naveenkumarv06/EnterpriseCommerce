import allure
import pytest

from Utilities.EventLog import Log


@pytest.mark.usefixtures("setup")
class BaseTest(Log):

    def attach_screenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

