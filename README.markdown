# WTF bot

WTFBot helps you keep your terminology straight in slack.

## Dependencies

(virtualenv recommended)
pip install -r requirements.txt

## Modules

This project splits different functionality into different modules to facilitate maintainability. Below is a description of each module.

- `__init__.py` - Constructs the Flask app object and configures it. Imports the other modules to emulate a single-module application.
- `config.py` - Contains the app configuration.
- `forms.py` - Contains WTForms Form objects for use in views and templates.
- `hooks.py` - Contains Flask and Jinja helper methods.
- `models.py` - Contains the database model classes for SQLAlchemy.
- `views.py` - Contains the app views.

## Running

    python main.py

## Loading test data

  Initial terms data are in a special secret format because they're an export from another system. Ask Ted for the JSON. Once you have it, you can run:

  `scripts/load_acronyms.py`
