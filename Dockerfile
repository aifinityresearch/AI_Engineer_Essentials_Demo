FROM python:3.11-slim

WORKDIR /app

RUN mkdir ~/.streamlit

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./shakesphere_app.py shakesphere_app.py

COPY .streamlit/ ./.streamlit/

EXPOSE 8051

ENTRYPOINT ["streamlit", "run"]

CMD ["shakesphere_app.py"]
