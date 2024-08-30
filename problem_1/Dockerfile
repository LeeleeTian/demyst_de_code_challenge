FROM python:3.8-slim

WORKDIR /app

COPY fixed_width_parser.py /app/
COPY spec.json /app/
COPY tests /app/tests/
COPY entrypoint.sh /app/

# Make sure all files have execution permissions
RUN chmod +x /app/entrypoint.sh

# Default command is to run the entrypoint script
CMD ["/app/entrypoint.sh"]