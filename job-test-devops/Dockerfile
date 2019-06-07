FROM python:3
WORKDIR /app
ADD parser.py json.log file.log /  
RUN pip install pystrich
CMD ["python", "parser.py"]