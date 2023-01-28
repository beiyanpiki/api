FROM python:3.8-alpine
WORKDIR /app

COPY ./api /app/api
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

RUN apk update && apk add python3-dev gcc libc-dev --no-cache
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

HEALTHCHECK --interval=10s --timeout=5s CMD curl -sS 'http://0.0.0.0:5000/api/ping' || exit 1
ENV ADMIN_TOKEN=miku
EXPOSE 5000
CMD ["python", "main.py"]