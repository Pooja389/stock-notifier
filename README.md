# stock-notifier
 Monitor Tesla's stock performance and send email alerts with related news headlines.
# Stock Price and News Notifier

This script monitors the stock price of a specified company (Tesla Inc in this case) and sends an email alert when there is a significant price change. The email also includes the top three recent news headlines related to the company.

## Features
- Fetches the latest stock price and compares it with the previous day's closing price.
- Calculates the percentage change in stock price and determines if the stock price increased (🔺) or decreased (🔻).
- Retrieves the top three news articles about the company from NewsAPI.
- Sends an email with the stock's performance summary and news headlines.

## Setup Instructions

### 1. Prerequisites
- Python installed on your system.
- The following Python modules: `datetime`, `requests`, and `smtplib`.

### 2. Required APIs
- **Alpha Vantage API**: To fetch stock price data.  
  Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key) to get your API key.
- **NewsAPI**: To fetch the latest news articles.  
  Sign up at [NewsAPI](https://newsapi.org/) to get your API key.

### 3. Google App Password
To send emails using Gmail, generate an **App Password** by following these steps:
1. Go to your Google Account settings.
2. Navigate to **Security** and enable **2-Step Verification**.
3. Under the "Signing in to Google" section, select **App Passwords**.
4. Generate a password for the "Mail" app and copy it. Use this in the script.

### 4. Your Coordinates
Replace the placeholders with your personal information:
- `my_email`: Your Gmail address.
- `other_email`: The recipient's email address.
- `app_password`: The App Password generated in step 3.
- `api_key`: Your NewsAPI key.
- `api_stock`: Your Alpha Vantage API key.

### 5. Running the Script
1. Save the script as a `.py` file (e.g., `stock.py`).
2. Run the script using `python stock.py`.

### Email Output
The email includes:
1. The stock's name.
2. The percentage change in price with an increase (🔺) or decrease (🔻) symbol.
3. The top three news headlines about the company.


### Note: Automating with PythonAnywhere
To automate this script and run it daily, you can use PythonAnywhere, a cloud-based Python hosting service
