# Undergraduate-Project-2020
Bachelor of Business Information Technology

## Project structure (dir)
Undergraduate-Project-2020/
<br>├── LICENSE
<br>├── main
<br>│   ├── backend
<br>│   │   ├── database.py
<br>│   │   ├── db_data
<br>│   │   │   └── products.db
<br>│   │   └── __pycache__
<br>│   │       └── database.cpython-37.pyc
<br>│   ├── frontend
<br>│   └── test_db.py
<br>├── README.md
<br>└── try-out
<br>    ├── links.txt
<br>    └── scraper.ipynb

### 

## Database Structure
| id | product_name | date_posted | demand |
|----| ------------ | ----------- | ------ |
| 0  |*product name*| *01/01/2000*| 5      |
| 1  |*product name*| *01/01/2001*| 8      |
* **id**: Primary key
* **product_name**: Text
* **date_posted**: Text
* **demand**: INTEGER

## Crawler Websites
* [Mkulima Young](http://www.mkulimayoung.com/)
* [Farmbiz Africa](https://farmbizafrica.com/)

## Handling AJAX Loading and Infinite Loading
Sometimes, fetching content from dynamic sites is actually straightforward, as they are highly dependent on API calls. In asynchronous loading, most of the time, data is loaded by making GET and POST requests; you can watch these API calls in the Network tab of Developer Tools.
