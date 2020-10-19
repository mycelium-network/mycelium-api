from fastapi import APIRouter, HTTPException, Path
from app.models import things

router = APIRouter()


@router.get("/things/")
async def read_things():
    return [{"name": "thing Foo"}, {"name": "thing Bar"}]


@router.get("/thing/{thing_id}")
async def read_thing(thing_id: str):
    return {"name": "Fake Specific thing", "thing_id": thing_id}


@router.post("/thing/")
async def create_thing(thing: things.ThingBase):
    return thing

@router.put(
    "/thing/{thing_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_thing(thing_id: str = Path(..., title="Identifier for a specific thing.")):
    if thing_id != "foo":
        raise HTTPException(
            status_code=403, detail="You can only update the thing: foo")
    return {"thing_id": thing_id, "name": "The Fighters"}

@router.delete("/thing/{thing_id}")
async def delete_thing(thing_id: str):
    return {"uuid": thing_id, "status":"delted"}
