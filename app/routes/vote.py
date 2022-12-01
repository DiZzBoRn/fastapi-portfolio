from app import models, schemas, utils, oauth2, database
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter, Response


router = APIRouter(prefix='/votes', tags=['Votes'])


@router.post("", status_code=status.HTTP_201_CREATED)
def add_vote(
    vote: schemas.Vote, 
    db: Session = Depends(database.get_db), 
    current_user: int = Depends(oauth2.get_current_user)
    ):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {vote.post_id} doesn't exists")

    vote_query = db.query(models.Vote).filter(
                models.Vote.post_id == vote.post_id, 
                models.Vote.user_id == current_user.id
                )
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"meassage": "successfuly added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote {vote.post_id} doesn't exists")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"meassage": "successfuly deleted vote"}