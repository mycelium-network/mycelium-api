from fastapi import Depends, FastAPI, Header, HTTPException

from app.routers import items, users

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(
    users.router,
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    items.router,
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)