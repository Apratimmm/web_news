# Web_News app

This is a Django-based web app that fetches and displays the latest news headlines by category using the [NewsAPI.org](https://newsapi.org/) service.




# Features

- Browse top headlines by category (e.g., General, Sports, Technology)
- Each news card has components like image, title, description, source, url_to_details, author and date_published
- Responsive layout with Bootstrap 4
- API-powered data (no local database needed)



## Technologies Used

- Python 3
- Django
- HTML, CSS, Bootstrap
- NewsAPI



## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Apratimmm/web_news.git
   cd web_news

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate
    
3. **Install dependencies**

    ```bash
    pip install -r requirements.txt

4. **Add your NewsAPI key**

    ```bash
    NEWSAPI_KEY=your_api_key_here

5. **Run the server**

    ```bash
    python manage.py runserver
    
