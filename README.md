![pytest](https://github.com/mycelium-network/mycelium-api/workflows/pytest/badge.svg)

# Mycelium Network API
The API for the Mycelium-Network project.

## Requirements
Clone this repository and navigate in the cloned folder:
```
pip install -r requirements.txt
```
Needs `python 3.6` or above.

## Run API 
```
uvicorn app.main:app --reload
```

* For API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc
