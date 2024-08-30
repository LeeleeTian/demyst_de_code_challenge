FROM python:3.8-slim

WORKDIR /app

COPY spec.json /app/
COPY fixed_width_parser.py /app/
COPY input_data.txt /app/

CMD ["python", "fixed_width_parser.py"]
