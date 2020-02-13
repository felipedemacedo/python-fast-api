FROM felipederodrigues/python37withpyodbc:v2

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]