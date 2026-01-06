FROM python:3.9-slim

# הגדרת תיקיית העבודה בקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות והתקנתן (זה נשאר אותו דבר)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- השינוי כאן ---
# במקום: COPY test_grid.py .
# נכתוב:
COPY . .

# הסבר: הפקודה הזו מעתיקה את כל התיקייה הנוכחית (כולל תיקיית tests)
# לתוך תיקיית /app בקונטיינר.
# בגלל שיש לנו .dockerignore, זה לא יעתיק זבל כמו allure-results או venv.

# פקודת ברירת המחדל (לא חובה כי אנחנו דורסים אותה בג'נקינס, אבל טוב שיהיה)
CMD ["pytest"]