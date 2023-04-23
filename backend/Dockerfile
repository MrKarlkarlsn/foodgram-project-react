FROM python:3.7-slim

CMD sudo apt-get update && sudo apt-get upgrade
CMD sudo apt-get install fontconfig
COPY tupo-vyaz_regular.ttf /usr/share/fonts/truetype
CMD sudo fc-cache -f -v

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt --no-cache-dir

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]