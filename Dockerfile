FROM python:3.13.7-alpine3.21 AS builder

WORKDIR /jobsites

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./modules /jobsites/modules

FROM python:3.13.7-alpine3.21 AS final

WORKDIR /jobsites

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=builder /jobsites/modules /jobsites/modules

RUN adduser -D jobsuser
USER jobsuser

ENTRYPOINT ["python","-m", "modules.integrate"]


