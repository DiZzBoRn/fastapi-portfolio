from fastapi import FastAPI, status, HTTPException, Response, Depends, Body
from pydantic import BaseModel
from typing import Optional, Union, List
from random import randrange
from . import utils
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import get_db, engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
# while True:
    # try:
    #     conn = psycopg2.connect(
    #             host="localhost", 
    #             port=5433,
    #             database="fastapi_local", 
    #             user="postgres", 
    #             password="1118",
    #             cursor_factory=RealDictCursor
    #             )
    #     cursor = conn.cursor()
    #     print('Database connection was successfully')
    #     break
    # except Exception as ex:
        # print('Connecting to database failed')
        # print('Error: ', ex)
        # time.sleep(3)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}


# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute(
#                 """SELECT * FROM posts WHERE id = %s""",
#                 (str(id),)
#             )
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=404, detail=f"post with id: {id} was not found")
#     return {"post_detail": post}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute(
#                 """INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""", 
#                 (post.title, post.content)
#             )
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute(
#                 """DELETE FROM posts WHERE id = %s RETURNING *""", 
#                 (str(id),)
#             )
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post is None:
#         raise HTTPException(status_code=404, detail=f"post with id {id} doesn't exists")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute(
#                 """UPDATE posts SET title = %s, content = %s WHERE id = %s RETURNING *""", 
#                 (post.title, post.content, str(id))
#             )
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post is None:
#         raise HTTPException(status_code=404, detail=f"post with id {id} doesn't exists")
#     return {"updated_post": updated_post}
