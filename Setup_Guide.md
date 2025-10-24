# Setup Guide

### Step 1: Set Up Python
1. **Grab Python**:
   - Head to [python.org](https://www.python.org/downloads/) and download Python 3.9 or newer
   - When installing, make sure to check “Add Python to PATH” so you can run it from anywhere.
   - Finish the install and close the installer.

2. **Check It Works**:
   - Open Command Prompt and type:
     ```bash
     python --version
     pip --version
     ```
   - You should see something like `Python 3.11.0` and `pip 23.3.1`. If not, double-check the installation.

### Step 2: Install Python Packages
1. **Get the Necessary Libraries**:
   - In Command Prompt, run:
     ```bash
     pip install pytest pytest-bdd requests Appium-Python-Client selenium pytz
     ```
   - This grabs everything the script needs: `pytest` for testing, `pytest-bdd` for the feature file, `requests` for API calls, `Appium-Python-Client` for automation, `selenium` for waiting on UI elements, and `pytz` for time zones.

2. **Make Sure They’re Installed**:
   - Run these one by one:
     ```bash
     python -c "import pytest; print(pytest.__version__)"
     python -c "import pytest_bdd; print(pytest_bdd.__version__)"
     python -c "import requests; print(requests.__version__)"
     python -c "import appium; print(appium.__version__)"
     python -c "import selenium; print(selenium.__version__)"
     python -c "import pytz; print(pytz.__version__)"
     ```
   - You should see version numbers (like `pytest 7.4.0`, `requests 2.32.3`). If any fail, rerun the `pip install` command.

### Step 3: Set Up Appium
1. **Install Node.js** (Appium needs this):
   - Go to [nodejs.org](https://nodejs.org/en/download/) and download the LTS version (18.x or 20.x is fine).
   - Install it and check:
     ```bash
     node --version
     npm --version
     ```
2. **Install Appium**:
   - In Command Prompt, run:
     ```bash
     npm install -g appium
     ```
   - Check the version:
     ```bash
     appium --version
     ```
   - Install the Android driver:
     ```bash
     appium driver install uiautomator2
     ```
3. **Start Appium**:
   - Run:
     ```bash
     appium
     ```
   - It’ll start a server at `http://127.0.0.1:4723`. Keep this terminal open while testing.

### Step 4: Get Your Android Setup Ready
1. **Install Android Studio**:
   - Download it from [developer.android.com](https://developer.android.com/studio).
   - Install and set up an emulator:
     - Open Android Studio → Device Manager → Create Virtual Device.
     - Pick a device with API level 35 (Android 15).
     - Choose a system image with Google Play and download it.
     - Start the emulator.

2. **Set Up ADB (Android Debug Bridge)**:
   - ADB comes with Android Studio (look in `C:\Users\<YourUser>\AppData\Local\Android\Sdk\platform-tools`).
   - Add that folder to your Windows PATH:
     - Right-click This PC → Properties → Advanced system settings → Environment Variables → Edit “Path” → Add the `platform-tools` path.
   - Check it:
     ```bash
     adb --version
     ```

3. **Confirm Your Device/Emulator**:
   - Run:
     ```bash
     adb devices
     ```
   - Look for `emulator-5554` (or your device ID). If nothing shows, ensure the emulator is running or your device is connected via USB with USB debugging on.

### Step 5: Install the MyObservatory App
1. **Get the APP**:
   - Download the MyObservatory from Google Play

### Step 6: Set Up the Feature File
1. **Create `9day_forecast.feature`**:
   - Save this in the same folder as `test_9day_forcast.py` (e.g., `step/`):
     Feature: 9-day forecast

2. **Check the Path**:
   - Make sure `FEATURE_FILE = '9day_forecast.feature'` in `test_9day_forcast.py` points to the right file (e.g., `step/9day_forecast.feature`).

### Step 7: Check Appium Setup
1. **Verify `conftest.py`**:
   - Your `conftest.py` sets up the Appium driver with:
     - Package: `hko.MyObservatory_v1_0`
     - Activity: `.Main2Activity`
     - Device: `emulator-5554`
     - Options: `UiAutomator2`, `noReset: True`, `autoGrantPermissions: True`
   - Save it in the same folder as `test_9day_forcast.py` (e.g., `step/`).
   - It’s already good to go, but confirm `emulator-5554` matches your device (`adb devices`).

2. **Ensure Appium Is Running**:
   - The server should be at `http://127.0.0.1:4723` (as in `conftest.py`).

### Step 8: Confirm UI Elements
1. **Use Appium Inspector**:
   - Start the Appium server and emulator.
   - Grab Appium Inspector from [appium.io](https://appium.io/docs/en/2.0/guides/inspector/).
   - Connect to `http://127.0.0.1:4723` using the capabilities from `conftest.py`.

2. **Run the Test**:
   - In Command Prompt:
     ```bash
     pytest -v -s
     ```