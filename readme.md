# Pagination Generator

This project provides a function to generate pagination links for a website footer based on specified parameters such as the current page, total number of pages, the boundaries, and the pages around the current page. The output includes ellipses (`...`) to indicate hidden pages for better navigational clarity.

## Table of Contents
- [Pagination Generator](#pagination-generator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Usage](#usage)
- [Installation](#installation)
- [1. Clone this repository:](#1-clone-this-repository)
- [2. Install the required packages:](#2-install-the-required-packages)
- [3. Running Tests:](#3-running-tests)

## Features

- Generate pagination links based on:
  - `current_page`: The active page being viewed.
  - `total_pages`: The total number of available pages.
  - `boundaries`: How many links to the first and last pages should be shown.
  - `around`: How many pages to show before and after the current page.

## Usage

You can use the `generate_pagination` function to create pagination links. Below are some examples:

```python
from main import generate_pagination

# Example 1
current_page = 4
total_pages = 5
boundaries = 1
around = 0
result = generate_pagination(current_page, total_pages, boundaries, around)
print(result)  # Expected output: 1 ... 4 5

# Example 2
current_page = 4
total_pages = 10
boundaries = 2
around = 2
result = generate_pagination(current_page, total_pages, boundaries, around)
print(result)  # Expected output: 1 2 3 4 5 6 ... 9 10

```

# Installation

To set up the environment for this project, you need to have Python installed on your machine. You can download the latest version from python.org.

# 1. Clone this repository:

```
git clone https://github.com/ayomidetobi/pagination.git
cd pagination
```

# 2. Install the required packages:
This project uses pytest for testing. You can install it using pip:

```
pip install pytest
```
# 3. Running Tests:
To ensure that everything is working properly, you can run the tests provided in the test_pagination.py file. Inside your terminal, navigate to the project directory and run:

```
pytest
```

Python Version
This project is compatible with Python 3.6 and above. Make sure you have the correct version installed before running the code.