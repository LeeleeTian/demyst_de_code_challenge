FROM python:3.8-slim

WORKDIR /app

COPY fixed_width_parser.py /app/
COPY spec.json /app/
COPY tests /app/tests/
COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]