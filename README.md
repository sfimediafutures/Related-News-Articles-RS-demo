# MediaFutures annual meeting demo

## Installation and running
1. Copy necessary files into a new folder `data/`
2. Create a virtual environment and activate it
3. install packages with `pip install -r requirements_all.txt`
4. run webapp with `python app.py` and open the IP address specified in the terminal

## Project Structure

- `app.py`: The main Flask application file and entry point to starting the web app.
- `utils.py`: Contains utility functions and classes for retrieving articles and recommendations.
- `templates/`: HTML templates using jinja2 templating for rendering web pages.
- `static/`: Static file like CSS for styling the web pages.