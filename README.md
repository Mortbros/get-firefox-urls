# get-firefox-urls
[A simple python script for obtaining the most recently accessed urls in Firefox.](./get_firefox_urls.py)
A Firefox window must be open for this program to function correctly. Importantly, this program **does not** rely on Selenium or the Win32 API.

## Dependencies
### Applications
Firefox must be installed.

### Python modules
lz4, os, glob, json, time

All dependancies except for [lz4](https://pypi.org/project/lz4/) are part of the python standard library.

Install lz4 via pip:

```
pip install lz4
```

## JSON keys
The following data can be accessed using the following JSON keys: 

### Tab titles
```python
['windows'][n]['tabs'][n]['entries'][0]['title']
```
### UNIX time when tab was last accessed
```python
['windows'][n]['tabs'][n]['lastAccessed']
```

### Tab local history 
The history for the tab at
```python
['windows'][n]['tabs'][n]['entries'][-1]['url']
```
is obtained with
```python
['windows'][n]['tabs'][n]['entries'][n]
```
