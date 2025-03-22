FROM python:3.12-slim

ENV TZ=UTC

WORKDIR /FLET

COPY requirements.txt /FLET/

RUN python3 -m venv /venv

RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

COPY . /FLET/

ENV PATH="/venv/bin:$PATH"

EXPOSE 5001

CMD ["flet","run", "main.py"]
