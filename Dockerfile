FROM python:3-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "gunicorn", "NotesApp.wsgi:application"]
