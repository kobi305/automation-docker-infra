FROM python:3.9-slim

WORKDIR /app

# 1. קודם מעתיקים רק את רשימת הקניות
COPY requirements.txt .

# 2. מתקינים את הספריות (דגל no-cache-dir חוסך מקום באימג')
RUN pip install --no-cache-dir -r requirements.txt

# 3. רק בסוף מעתיקים את הקוד שלנו (שמשתנה לעיתים קרובות)
COPY test_grid.py .

CMD ["python", "test_grid.py"]