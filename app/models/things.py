from typing import List, Optional, Set
from pydantic import BaseModel, HttpUrl
from fastapi import Query

class Image(BaseModel):
    url: HttpUrl

class Comment(BaseModel):
    user_id: str
    comment: str
    date: int

class Document(BaseModel):
    url: HttpUrl
    name: str = Query(None, min_length=3, max_length=50, regex=r"^[ a-zA-Z0-9\-\_\.]*$")

class ThingBase(BaseModel):
    title: str = Query(..., min_length=3, max_length=50)
    description: str = Query(..., min_length=10, max_length=1000)
    category: str
    status: str
    shared_with: Optional[Set[str]]
    shared_start_date: Optional[int] = Query(None, gt=0)
    shared_end_date: Optional[int] = Query(None, gt=0)
    shared_notification_required: bool
    visibility: Set[str]
    images: List[Image]
    comments: Optional[List[Comment]]
    documents: Optional[Set[Document]]
    location: Optional[str]
    tags: Optional[Set[str]]
    likes: Optional[Set[str]]
    ean: Optional[str]

    class Config:
        schema_extra = {
            "example":{
                "title" : "Demo",
                "description" : "#Title\nEin kleiner text leicht formatiert\n-Erster Punkt\n- Zweiter Punkt",
                "category" : "thing",
                "status" : "shared",
                "shared_notification_required":True,
                "visibility":["0"],
                "images":[
                    {"url":"https://www.mycelium.space/img/brand/favicon/logo-white-120.png"}
                ]
            }
        }
    

class ThingInDB(ThingBase):
    date_creation: int = Query(..., gt=0)
    date_modification: int = Query(..., gt=0)
    owner_group: str
    creator: str
    uuid: str
    internal_barcode: int = Query(..., gt=0)

class ThingOutDB(ThingBase):
    date_creation: int
    date_modification: int
    owner_group: str
    creator: str
    uuid: str
    internal_barcode: int

class Book(ThingBase):
    authors: List[str]
    isbn: int
    publisher: str
    publish_date: str
    language: str

