from typing import Sequence, Union

from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import subprocess


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/workflows")
async def get_workflows():
    return {"workflows": ""}


@app.post("/workflows")
async def run_workflow(request: Request):
    print('----------Run Workflow!---------')
    wf_json = await request.json()
    print(wf_json)
    # write wf_body to a file
    with open("sample.json", "w") as outfile:
        json.dump(wf_json, outfile)
    # run workflow compiler
    subprocess.run(["pwd"])

    # subprocess.run(["conda activate wic"], shell=True)
    subprocess.run(
        ["wic --yaml sample.json  --run_local True"], shell=True)
    # ../../examples/gromacs/test.yml 
    return wf_json
