FROM python:3.8
WORKDIR /usr/src/app

## Install packages 
COPY requirements.txt .
RUN pip install -r requirements.txt

## Copy all src files 
COPY . .

ENTRYPOINT ["python", "./app.py"] 

# docker built -t nineking424/csvdown .
# docker run --rm nineking424/csvdown