# Instagram Followers Bot
A bot which finds the followers of a similar Instagram account and 
following them in order to get more followers 

## Installation

Install all the required packages from the requirements.txt

```bash
pip install -r requirements.txt
```

**NOTE: you need to replace the Chrome WebDriver file according to your OS**

Rename the .env.example file to .env and change the values

```bash
 cp .env.example .env
```

## Usage

Fill/change all the required values in the .env file

```python
# Your Instagram password
PASSWORD=""
# Your Instagram profile name
USERNAME=""
# Your Instagram Email
EMAIL=""
# The path to the chrome webdriver
CHROME_DRIVER_PATH="./chromedriver.exe"
# The Instagram profile you want to get his followers to follow you
SIMILAR_ACCOUNT_NAME=""

```

