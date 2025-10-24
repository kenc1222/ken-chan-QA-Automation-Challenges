import pytest
import requests
from pytest_bdd import scenario, given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytz import timezone
from datetime import datetime
from datetime import date, timedelta
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Task 2
FEATURE_FILE = "9day_forecast_API.feature"


@scenario(FEATURE_FILE, "Test the request response status is whether successful or not")
@then("extract the relative humidity for the day after tomorrow from the API response")
def test_9_day_forcast_API():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
    today = datetime.now(timezone("Asia/Hong_Kong")).date()

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        pytest.fail(f"API request failed: {e}")

    if response.status_code != 200:
        logger.error(f"API request failed with status code: {response.status_code}")
        pytest.fail(f"API request failed with status code: {response.status_code}")

    data = response.json()
    target_date = (today + timedelta(days=2)).strftime("%Y%m%d")
    target_date_display = (today + timedelta(days=2)).strftime("%A, %B %d, %Y")

    api_humidity = None
    for forecast in data["weatherForecast"]:
        if forecast["forecastDate"] == target_date:
            api_humidity = f"{forecast['forecastMinrh']['value']} - {forecast['forecastMaxrh']['value']}%"
            print(f"Relative humidity for {target_date_display}: {api_humidity}")
            break
    if not api_humidity:
        logger.error(f"No forecast found for {target_date_display}")
        pytest.fail(f"No forecast found for {target_date_display}")