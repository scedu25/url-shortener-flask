# URL Shortener

This service shortens user-input URLs, stores them in a nonpersistent dictionary, and uses the shortened URLs to create new routes that redirect to the original URL.
If a route doesn't exist, a 404 is returned.

## Running the app

See [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) to create a virtual environment. Activate the virtual environment, then invoke `pip install -r requirements.txt` to install the needed packages.

Start the app from the command line using `flask run`. The app runs on `http://localhost:5000` by default. Open this URL in a browser to access the UI.
