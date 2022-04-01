# Web Crawl Word Count

## Overview
This is a simple Python service that accepts a website URL and returns the frequency of the 
occurrence of words from that URL.

## Technologies
+ [**Flask**](https://flask.palletsprojects.com/en/2.1.x/): Flask is a Python microframework for 
building web applications and API services. For this project, Flask was a suitable choice because it
is fast to get started and spin up a backend service without having to worry about configurations
and boilerplate setup.
+ [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [**lxml**](https://lxml.de/):
BeautifulSoup and lxml are one of the most popular and performant Python parsing libraries for 
pulling data from HTML and XML files. BeautifulSoup's default parser is a little slow, but it allows
leveraging other parsers. This is where lxml comes in. lxml is a high-performance, 
production-quality HTML and XML parsing library and has the advantage of being really fast as it 
uses *libxml2* and *libxslt* C libraries. These libraries are required to be able to crawl the 
provided URL to get and count the words.
+ [**Requests**](https://docs.python-requests.org/): Requests is an HTTP library for Python. The
major reason for using the Request library is its ease of use and readability - tools for writing 
more elegant and maintainable code. The response from the Request library is passed to the parser.
+ [**pytest**](https://docs.pytest.org/): pytest is a framework that makes it easy to write small,
readable test. It was chosen because of its simplicity and ability to scale to support more complex
testing. It also works seamlessly with Flask.
+ [**Coverage**](https://coverage.readthedocs.io/): This is a tool for measuring code coverage of 
programs written in Python. It's a great tool for generating testing coverage report and works well
with *pytest*.

### Stress Test
+ [**Locust**](https://docs.locust.io/): Locust is an easy-to-use performance testing tool.


## Setup
+ Ensure you have [**Docker**](https://docker.com) and **docker compose** installed.
+ Clone the repository 
```
$ git clone https://github.com/osaetinevbuoma/web_crawl_word_count.git
```
+ In the project's root directory, run
```
$ docker-compose up
```
This builds the docker container and starts the Flask server (`http://localhost:5000`).

## Usage
Using a tool like Postman, Insomnia or curl, you can make a `GET` request to the following endpoints
+ `/health`: returns a JSON object with the status update of how long the server has been alive.
```
    {
        "message": "alive since Fri Apr  1 12:51:19 2022",
        "status": "UP"
    }
```
+ `/count-words?url=<website_url>`: returns a JSON object with the words scraped from the provided 
`website_url` and the number of occurrence of each word.
```
    GET: http://127.0.0.1:5000/count-words?url=https://www.google.com
    Response: {
        "2022": 1,
        "about": 1,
        "advanced": 1,
        "advertising": 1,
        "business": 1,
        "drive": 1,
        "gmail": 1,
        ...
    }
```

### Testing
+ To re-run the unit test suites, enter the following command in the terminal (project's root directory)
```
$ coverage run -m pytest -vv

// Sample output
tests/test_crawler.py::test_count_words_returns_expected_occurrences PASSED                [ 11%]
tests/test_crawler.py::test_count_words_returns_404_if_url_is_not_provided PASSED          [ 22%]
tests/test_crawler.py::test_count_words_returns_404_if_url_does_not_exist PASSED           [ 33%]
...

```
+ To generate the coverage report, use the following command
```
$ coverage report  // displays the report in terminal

// or 

$ coverage html  // generates HTML version of the report
```
The HTML version of the coverage is available in the **`htmlcov`** directory.

### Stress Testing
In the terminal (project's root directory), enter the following command:
```
$ locust
```
This starts the Locust server to begin the stress test. Point your browser to `http://0.0.0.0:8089`
![Sample Locust page](https://docs.locust.io/en/stable/_images/webui-splash-screenshot.png)

**NOTE**: Locust is not bundled in the Docker container for this project. Therefore, you have to 
install Locust on your host machine (`pip3 install locust`).
