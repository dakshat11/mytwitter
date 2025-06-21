# MyTwitter

A simple Twitter-like web application built with Django.

## Features

- User registration and authentication
- Create, edit, and delete tweets
- Upload photos with tweets
- Responsive UI with Bootstrap and Tailwind CSS
- Admin panel for managing users and tweets

## Project Structure

```
mytwitter/
├── db.sqlite3
├── manage.py
├── media/
│   └── photos/
├── mytwitter/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── static/
├── templates/
│   └── layout.html
├── theme/
│   └── ...
└── tweet/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...
```

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/mytwitter.git
    cd mytwitter
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (admin):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Install and build Tailwind CSS (optional, for development):**
    ```sh
    cd mytwitter/theme/static_src
    npm install
    npm run build
    cd ../../..
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Access the app:**
    - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Notes

- Media uploads (like photos) are stored in the `media/` directory.
- Static files are managed via Django and Tailwind CSS.
- For more details, see the `notes.markdown` and `project creation using Django.txt` files.

## License

This project is licensed under the MIT License.
