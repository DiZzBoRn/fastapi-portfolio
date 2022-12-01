from fastapi import FastAPI, Depends, Header, Request
from pydantic import BaseModel


app = FastAPI()


fake_items_db = [
    {
        "item_name": "Foo"
    },
    {
        "item_name": "Bar"
    }
]

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit

class CommonQueryParamsPy(BaseModel):
    q: str | None = None
    skip: int = 0
    limit: int = 100

@app.get("/items")
# async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
# async def read_items(commons=Depends(CommonQueryParams)):
# async def read_items(commons: CommonQueryParams = Depends()):
async def read_items(commons: CommonQueryParamsPy = Depends(CommonQueryParamsPy)):
    response = {}
    print(commons)
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip:commons.skip + commons.limit]
    response.update({"items": items})
    return response


@app.get("/users")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons



class BodyData(BaseModel):
    name: str
    age: int

    
@app.get("/body-data")
def get_post_data(data: BodyData):
    return data


class QueryParams(BaseModel):
    q: str
    limit: int

    
@app.get("/query-params")
def get_post_data(q: QueryParams = Depends()):
    return q

    
@app.get("/header")
def get_post_data(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}

@app.get("/headers")
def get_post_data(request: Request):
    return {"headers": request.headers}