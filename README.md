# Veeam Careers Test

This project contains a Selenium WebDriver test for the Veeam Careers website (https://cz.careers.veeam.com/vacancies) using Python, Selenium, and pytest.

## Prerequisites

- Python 3.8

## Setup

1. Install Python 3.8 from https://www.python.org/downloads/ if you don't have it already.

2. Download or clone this repository.

3. Open a terminal or command prompt and navigate to the project folder `veeam_careers_test`.

4.  Create and ctivate the virtual environment:

`python -m venv env`

- Windows:

`env\Scripts\activate.ps1`

- Linux/Mac:

`source env/bin/activate`

5. Install the required packages:

`pip install -r requirements.txt`

## Configure

In the `test_veeam_careers.py` file you can configure department, language and expected number of jobs.

## Run

Run the test:

`pytest`

