FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip

RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

EXPOSE 5000

CMD ["python", "main.py"]