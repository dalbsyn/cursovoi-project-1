FROM python:3.12

WORKDIR /

COPY requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY server.py /server.py

CMD ["fastapi", "run", "server.py", "--port", "80"]

