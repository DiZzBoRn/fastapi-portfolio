from app import models, schemas, oauth2
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter, Response
from typing import List, Optional
from app import oauth2 
from sqlalchemy import func
router = APIRouter(prefix="/posts", tags=['Posts'])


@router.get("", response_model=List[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user), 
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ''
    ):    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
                models.Vote, models.Vote.post_id == models.Post.id, isouter=True
            ).group_by(models.Post.id).filter(
                models.Post.title.contains(search)
            ).limit(limit).offset(skip).all()
    
    return posts

@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
                models.Vote, models.Vote.post_id == models.Post.id, isouter=True
            ).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"post with id: {id} was not found")
    
    return post


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(
    post: schemas.PostCreate, 
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(
    id: int, 
    updated_post: schemas.PostCreate, 
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
    ):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exists")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized!")


    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()

@router.delete("/{id}")
def delete_user(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exists")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized!")
    
    post_query.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)