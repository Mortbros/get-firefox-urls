# get-firefox-urls
A simple python script for obtaining the most recently accessed urls in Firefox.

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