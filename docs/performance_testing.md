# Performance testing

## What is it?

The aim of a performance test is to observe system behaviour under immense load, seeing where the bottlenecks are and what breaks. In our case this means a lot of requests from many simulated users.


## Requirements

* locustio - Python package (included in requirements.txt) for simulating user behaviour


## How it works?

There is a file `flocsweb/tests/locustfile.py` containing predefined user behaviour. The behaviour is somewhat randomized to more closely mimic the real users. Right now, the behaviour is loosely is equivalent to the following user behaviour.

1. user coming to a main page and initiating session
2. randomly selecting task from all the tasks available in the system
3. making random number of edits to the program
4. solving the task by running the program

## How to run the test?

1. start Django server
2. run `locust -f path/to/locustfile.py --host=HOST_URL` where `path/to/locustfile.py` is relative or absolute path to file with user behaviour definition and `HOST_URL` is the url to the server to send request to. When testing locally this should by `http://127.0.0.1:8000`.
3. visit Locust web interface at `http://127.0.0.1:8089/`
4. set number of users and spawn rate
5. let the simulated users do the work

## How to analyse the results?

Locust web interface provides some statistics and overviews of the requests made together with the time it took the server to process them. There are also some data available for export as csv files. This is useful to detect any anomalies and strange behaviour.

If there were any failed request (=response status code is other than 2xx) the response is saved. The log file with such responses to failed requests will be located at the directory from which the locust command was run and will be named `request_errors.log`. This file may contain anything from nicely formatted HTML pages produced by Django in debug mode to just a JSON with error message depending on the server settings.

The Djnago server in debug mode will output all the SQL queries it has made and the time it took to execute them. By default it is printed to the stderr together with the processed requests. To capture this outputs for further analysis one can run `2>sever.log ./manage.py runserver` resulting in debug messages stored in a file `server.log`.
