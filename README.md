
# Clone-Pinterest

Clone-Pinterest is a web application built with Flask, Python, and SQLite that simulates the basic functionalities of an image-sharing social network, similar to Pinterest. Users can create accounts, log in, upload photos, and view profiles.

## Technologies

- **Python**: Programming language used for the backend.
- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Flask-Login**: User session management.
- **SQLite**: Database used to store information.
- **Werkzeug**: Utility library for file handling.
- **Flask-WTF**: Integration of WTForms with Flask for creating forms.
- **Flask-Bcrypt**: Password hashing using Bcrypt.
- **WTForms**: Library for creating and validating forms.
- **email-validator**: Email validation for WTForms.

## Requirements

- Python 3.x
- Flask
- Flask-Login
- SQLAlchemy
- Werkzeug
- Flask-WTF
- Flask-Bcrypt
- WTForms
- email-validator
- pytz
- SQLite (included with Python)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gabriellemosc/Fake-Pinterest/
   cd fakepinterest
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**

   ```bash
   flask run
   ```

## Usage

1. **Homepage:** The main page where users can log in.
2. **Create Account:** Page to create a new user account.
3. **Profile:** User profile page where they can upload photos and view their own profile or others' profiles.
4. **Logout:** Option to log out of the current account.

## Routes

- `/`: Main route for login.
- `/criarconta`: Route to create a new account.
- `/perfil/<id_usuario>`: Route to view a user's profile, where `<id_usuario>` is the user's ID.
- `/logout`: Route to log out of the current session.

## Project Structure

- `app.py`: Main Flask application file with route definitions.
- `models.py`: Database model definitions.
- `forms.py`: Form definitions used in the application.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory for static files like CSS and JavaScript.
- `uploads/`: Directory to store images uploaded by users.
- `requirements.txt`: List of project dependencies.

## Contributing

1. Fork this repository.
2. Create a branch for your changes (`git checkout -b my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



