# Mountainside Roleplay - Website

A comprehensive Django-based website for the Mountainside Roleplay FiveM server featuring ticket system, shop, staff applications, and whitelist management.

## Features

- **User Authentication**: Register, login, and profile management with Discord/Steam ID integration
- **Ticket System**: Support ticket creation and management with staff responses
- **Shop System**: Item catalog with categories, purchases, and order history
- **Staff Applications**: Apply for moderator, admin, developer, or support positions
- **Whitelist Applications**: Character-based whitelist application system
- **Admin Panel**: Full Django admin interface for managing all aspects

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd msrp_site
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Create media and static directories:
```bash
mkdir media static
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000` in your browser

## Usage

### Admin Access

1. Go to `http://127.0.0.1:8000/admin`
2. Login with your superuser credentials
3. Add shop categories and items
4. Manage tickets, applications, and user profiles

### PyCharm Integration

This project is configured to work with PyCharm:

1. Open the project in PyCharm
2. PyCharm will automatically detect the virtual environment in `.venv`
3. Set the Python interpreter to `.venv/Scripts/python.exe`
4. Use PyCharm's integrated terminal to run Django commands

### Git Workflow

The project is already initialized with Git. To push to GitHub:

1. Create a new repository on GitHub (don't initialize with README)
2. Add the remote:
```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
```

3. Add and commit your changes:
```bash
git add .
git commit -m "Initial commit"
```

4. Push to GitHub:
```bash
git push -u origin main
```

PyCharm will automatically sync changes to GitHub when you commit through the IDE.

## Project Structure

```
msrp_site/
├── accounts/          # User authentication and profiles
├── applications/      # Staff and whitelist applications
├── home/              # Homepage and main views
├── shop/              # Shop items and purchases
├── tickets/           # Support ticket system
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── media/             # User uploaded files
└── msrp_site/         # Project settings
```

## Configuration

### Important Settings

Edit `msrp_site/settings.py` for production:

- Change `SECRET_KEY` to a secure value
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS` with your domain
- Configure a production database (PostgreSQL recommended)
- Set up email backend for notifications

### Environment Variables

For production, use environment variables:

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

## Technologies Used

- Django 5.2.7
- Bootstrap 5.3
- Font Awesome 6.4
- Pillow (image handling)
- Django Crispy Forms (form styling)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is private and proprietary to Mountainside Roleplay.

## Support

For issues or questions, create a support ticket through the website or contact the development team.
