from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.get("/autocomplete/")
async def read_autocomplete():
    return {"info": "OpenLibrary API Call to create an autocomplete, more info see https://openlibrary.org/developers/api"}


@router.get("/autocomplete/{isbn}")
async def read_autocomplete(isbn: int):
    r = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:"+str(isbn)+"&format=json&jscmd=data")
    return r.json()
