FROM python:3.8
WORKDIR /usr/src/app

## Install packages 
COPY requirements.txt .
RUN pip install -r requirements.txt

## Copy all src files 
COPY *.py .

ENTRYPOINT ["python", "./app.py"] 

# 1) local build
# docker built -t nineking424/csvdown .

# 2) multi-platform build
# docker buildx build -t nineking424/csvdown --platform linux/arm64,linux/amd64 . --push

# 3) pull && run
# docker pull nineking424/csvdown
# docker run --rm -v ~/csvdown:/data nineking424/csvdown -o /data
# docker run --name csvdown -v ~/csvdown:/data nineking424/csvdown -o /data
# docker start csvdown