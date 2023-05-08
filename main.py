from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    name : str
    status : bool

todos = {
    1: {
        "name" : "Study",
        "description" : "Learn book",
        "status" : True
    }
}

@app.get("/get-activity/{todo_id}")
def get_activity(todo_id:int):
    return todos[todo_id]

@app.post ("/add-activity/{todo_id}")
def add_activity(todo_id:int,todo:Todo):
    if todo_id in todo:
        return {"Activity is already on the list"}
    todos[todo_id] = todo
    return todos[todo_id]

@app.delete ("/remove-activity/{todo_id}")
def delete_activity(todo_id:int):
    if todo_id in todos:
        todos["status"] = False
        del todos[todo_id]
        return todos["status"]