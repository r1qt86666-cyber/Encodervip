# اختيار نسخة بايثون
FROM python:3.9-slim

# تحديد مجلد العمل
WORKDIR /app

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ كل الملفات (بما فيها a3.py و app.py) إلى السيرفر
COPY . .

# فتح المنفذ الخاص بالسيرفر
EXPOSE 5000

# أمر التشغيل
CMD ["python", "app.py"]
