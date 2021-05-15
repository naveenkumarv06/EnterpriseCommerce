import os
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
    )
    parser.addoption(
        "--url", action="store", default="stage", help="my option: stage or qe"
    )


driver = None

@pytest.fixture( scope="class")  # scope = function,class,module,session
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()

    if url == "Stage":
        driver.get("https://hendrix.stage.adobe.com/radon_java_webapp/hx5/#/login?mode=qa")


    elif url =="QE":
        driver.get("https://hendrix.qe.adobe.com/radon_java_webapp/hx5/#/login?mode=qa")

    request.cls.driver = driver
    yield
    driver.close()




PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), '..', p))

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):

            add_name = '{}_{}'.format(report.nodeid.split("::")[1], datetime.now().strftime("%y-%m-%d_%H.%M.%S"))

            file_name = PATH('./Screenshots'+'/'+add_name+'.png')

            #allure_filename = PATH('./AllureScreenshots'+'/'+add_name)

            #file_name = report.nodeid.replace("::", "_") + ".png"

            cp_file_name ="../Screenshots"+'/'+add_name+".png"

            _capture_screenshot(file_name)



            #allure report

            #allure.attach(driver.get_screenshot_as_png(), name=allure_filename, attachment_type=AttachmentType.PNG)
            #allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', AttachmentType.HTML)



            if file_name:
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % file_name

                html = '<div><img src='+cp_file_name+' alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>'


                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.save_screenshot(f".\\AllureScreenshots\\fail_{now}.png")


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)



