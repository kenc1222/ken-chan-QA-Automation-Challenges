import pytest
import requests
from pytest_bdd import scenario, given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Task 1
FEATURE_FILE = "9day_forecast.feature"


@scenario(FEATURE_FILE, "User check 9-day forecast")
def test_go_to_9day_forecast():
    pass


@given("I launch Myobservatory")
def launch_application():
    print("Application launched.")


@when("I go to 9-day forecast page")
def goto_9day_forcast(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up").click()
    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Collapsed\nForecast & Warning Services"
    ).click()
    driver.find_element(
        AppiumBy.XPATH,
        "//android.widget.TextView[@resource-id='hko.MyObservatory_v1_0:id/title' and @text='9-Day Forecast']",
    ).click()


@then('I should see the "9-Day Forecast"')
def verify_9day_forecast_page(driver):
    nine_day_forecast_summary_id = "hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit"
    nine_day_view_detail_id = "hko.MyObservatory_v1_0:id/mainAppSevenDayView"

    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ID, nine_day_forecast_summary_id)
            )
        )
        element = wait.until(
            EC.visibility_of_element_located((AppiumBy.ID, nine_day_view_detail_id))
        )

        print(f"Go to 9-Day Forecast successfully.")

    except Exception as e:
        print(
            f"Error: Could not find element with ID '{nine_day_forecast_summary_id}'."
        )
        print(f"Error: Could not find element with ID '{nine_day_view_detail_id}'.")
        print(f"Details: {e}")
        raise


@scenario(FEATURE_FILE, "User switch to other tab")
def test_switch_to_other_tab():
    pass


@then('I switch to "Local Forecast" tab and "Extended Outlook" tab')
def switch_the_tab(driver):
    try:
        local_forecast_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Local Forecast")',
                )
            )
        )
        local_forecast_element.click()

    except Exception as e:
        print(f"Failed to click 'Local Forecast': {e}")
        raise

    try:
        extended_outlook_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Extended Outlook")',
                )
            )
        )
        extended_outlook_element.click()
    except Exception as e:
        print(f"Failed to click 'Extended Outlook': {e}")
        raise


@scenario(FEATURE_FILE, "User open remarks")
def test_go_to_remarks():
    pass


@then("I go to remarks page")
def switch_the_tab(driver):
    wait = WebDriverWait(driver, 10)

    try:
        more_options_element = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("More options")',
                )
            )
        )
        more_options_element.click()
    except Exception as e:
        raise AssertionError(f"Could not access 'More options' menu: {str(e)}")

    try:
        content_element = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "hko.MyObservatory_v1_0:id/content")
            )
        )
        content_element.click()

    except Exception as e:
        raise AssertionError(f"Could not interact with content: {str(e)}")
