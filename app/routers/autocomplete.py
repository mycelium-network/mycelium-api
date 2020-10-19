from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.get("/autocomplete/")
async def autocomplete_info():
    return {"info": "OpenLibrary API Call to create an autocomplete, more info see https://openlibrary.org/developers/api"}


@router.get("/autocomplete/isbn/{isbn}")
async def read_autocomplete_isbn(isbn: int):
    r = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:"+str(isbn)+"&format=json&jscmd=data")
    return r.json()

@router.get("/autocomplete/ean/{ean}")
async def read_autocomplete_ean(ean: int):
    return {"status":"Not Implemented"}