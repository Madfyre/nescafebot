FROM python:3.10.13-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY bot ./bot/

ARG NESCAFEBOT_TOKEN
ENV NESCAFEBOT_TOKEN $NESCAFEBOT_TOKEN

CMD ["bash"]