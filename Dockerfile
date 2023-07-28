FROM python:3

WORKDIR /in

COPY . .

CMD ["python3", "read_file.py"]