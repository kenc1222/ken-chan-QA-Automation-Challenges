import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PACKAGE = "hko.MyObservatory_v1_0"
APP_ACTIVITY = ".Main2Activity"

DEVICE_NAME = "emulator-5554"


@pytest.fixture(scope="function")
def appium_driver():
    """Fixture to initialize and tear down the Appium driver."""

    capabilities = {
        "platformName": "Android",
        "deviceName": DEVICE_NAME,
        "appPackage": APP_PACKAGE,
        "appActivity": APP_ACTIVITY,
        "automationName": "UiAutomator2",
        "newCommandTimeout": 600,
        "noReset": True,
        "autoGrantPermissions": True,
    }

    options = UiAutomator2Options().load_capabilities(capabilities)

    appium_server_url = "http://localhost:4723"

    print(f"Connecting to Appium server at {appium_server_url}")
    print(f"Desired capabilities: {capabilities}")

    driver = None
    try:
        driver = webdriver.Remote(appium_server_url, options=options)
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        print(f"Failed to initialize Appium driver: {e}")
        pytest.fail(f"Could not start Appium session: {e}")
    finally:
        if driver:
            driver.quit()


@pytest.fixture
def driver(appium_driver):
    return appium_driver
