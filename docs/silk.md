# Silk profiling tool

## What is it?

Silk is a tool for extensive Django profiling. It allows one to inspect times of every request as well as number of SQL queries and their times. Documentation can be found at [readthedocs](http://silk.readthedocs.io/en/latest/index.html). 


## Requirements

* django-silk - Python package (git version included in requirements.txt) 


## How it works?

The Silk introduces special middleware for intercepting request and save all the metadata and statistics in the database.

## How to enable it?

To enable Silk, server must be run with environment variable SILK with string value "True".

## Where can I find profiling data?

Once the Silk is running, one can browse request statistics at hostname/silk/. One can browse request by different criteria (use funnel in the top right corner). After selecting a specific request, the profiling info is shown including all the SQL queries and their execution times.
