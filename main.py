from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {'data':{'name':'supratim'}}

@app.get("/about/{id}")
def about(id:int):
    # return {'data':{'about':'testing Aboutpage {id}' }}
    return {'data':{id, 2 }}
