FROM python:3.8.13 as base


ENV PYTHONPATH=$PYTHONPATH:/src/

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ /src/

FROM base AS test
RUN ["python", "-m", "pytest", "-v", "/src/tests"]

FROM base AS build

COPY . .
EXPOSE 8080
CMD ["python3", "app/app.py"]
