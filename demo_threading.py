"""Brief Demo of Threading

Fetch web requests in parallel.

"""

import threading
import urllib
import collections

urls = [
	'https://www.python.org',
	'http://www.jython.org',
	'http://ironpython.net',
	'https://pypy.org',
	'http://micropython.org',
]

# Deque objects are thread-safe. That means we can access them
# from different threads simultaneously without race conditions.

responses = collections.deque()

def get(url):
    "Get a url and append the response to responses."
    con = urllib.urlopen(url)
    data = con.read()
    con.close()
    responses.append(data)

# Construct thread objects.

threads = []
for url in urls:
    thread = threading.Thread(target=get, args=(url,))
    threads.append(thread)

# Start threads. Simultaneous execution begins here.

for thread in threads:
    thread.start()

# Wait for threads to return.

for thread in threads:
    thread.join()

# Display length of each response.
# Beware! Order is not reliable.

print map(len, responses)
