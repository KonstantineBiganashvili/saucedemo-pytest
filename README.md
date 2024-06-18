
# SauceDemo Automation Testing

This project contains automated test scripts for the [SauceDemo website](https://www.saucedemo.com/) using Selenium, pytest, and Allure for reporting. The tests are designed following the Page Object Model (POM) pattern.

## Project Structure

```
saucedemo_automation/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_saucedemo.py
│
├── allure-results/
│
├── .env
│
├── requirements.txt
│
└── pytest.ini
```

## Setup Instructions

### Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd saucedemo_automation
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # For Windows PowerShell
   source .venv/bin/activate      # For macOS/Linux
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the ChromeDriver path:**

   - Create a `.env` file in the project root directory with the following content:

     ```plaintext
     CHROMEDRIVER_PATH="C:/Users/desktop-sarkie/Desktop/Uni Related/Testing-Automation/quiz3/chromedriver.exe"
     ```

### Running the Tests

1. **Run the tests using pytest:**

   ```bash
   pytest
   ```

2. **Generate and view the Allure report:**

   ```bash
   allure serve allure-results
   ```

## Test Scenarios

The following test scenarios are covered:

1. **Login Tests:**
   - Valid login
   - Invalid login

2. **Post-Login Actions:**
   - Sort products from low to high
   - Assert specific product price
   - Add to cart
   - Verify "Add to cart" button changes to "Remove"
   - Go to cart
   - Assert product price in cart matches the product price on the inventory page
   - Assert product name
   - Go to checkout
   - Click Continue and verify the error message

## Project Files

### `pages/login_page.py`

Contains the `LoginPage` class that encapsulates the login page interactions.

### `pages/inventory_page.py`

Contains the `InventoryPage` class that encapsulates the inventory page interactions.

### `pages/cart_page.py`

Contains the `CartPage` class that encapsulates the cart page interactions.

### `pages/checkout_page.py`

Contains the `CheckoutPage` class that encapsulates the checkout page interactions.

### `tests/conftest.py`

Contains the pytest fixture for setting up and tearing down the WebDriver instance. Also includes a hook to capture screenshots on test failures.

### `tests/test_saucedemo.py`

Contains the test cases for the SauceDemo website.

## Collaborations

This project was developed in collaboration with:
- Konstantine Biganashvili
- Aleksandre Mikashavidze

## Contributions

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
