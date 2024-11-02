FROM python:3.12

WORKDIR /

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY server.py /server.py

CMD ["fastapi", "run", "server.py", "--port", "8000"]

