# mycelium-api
The API for the mycelium project.

## Requirements

```
pip3 install fastapi
pip3 install uvicorn
pip3 install pyjwt
pip3 install passlib
pip3 install python-multipart
```
Needs `python 3.6` and above

## Run API 
```
uvicorn app.main:app --reload
```

* For API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc