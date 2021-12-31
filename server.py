import os
import datetime
from fastapi import FastAPI, Response, Request
import json
import uvicorn


app = FastAPI()


@app.get(
    "/",
    status_code=200,
)
async def hello(req: Request, response: Response):

    try:
        req_data = await req.json()
    except:
        None
    caller_ip = req.client.host
    response = json.dumps(
        {"message": f"Hello Son/Daughter/They of a gun.. Your IP is {caller_ip}"}
    )

    return Response(status_code=200, content=response)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=80, reload=True)
