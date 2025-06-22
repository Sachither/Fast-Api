from fastapi import Depends, HTTPException, status, Response, APIRouter
from sqlalchemy import or_, func
from app import models
from app import oauth2
from app.database import get_db
from typing import Optional
from sqlalchemy.orm import Session
from app.schemas import PostCreate, PostResponse, PostVote

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[PostVote])
def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # SQL query to fetch all posts
    # cur.execute("SELECT * FROM posts")
    # posts = cur.fetchall()
    
    # SQLAlchemy ORM query to fetch all posts
    # posts = (
    #     db.query(models.Post)
    #     .filter(
    #         or_(
    #             models.Post.title.ilike(f"%{search}%"),
    #             models.Post.content.ilike(f"%{search}%")
    #         )
    #     )
    #     .limit(limit)
    #     .offset(skip)
    #     .all()
    # )
    post = (
        db.query(models.Post, func.count(models.Vote.post_id)
        .label("votes"))
        .join(models.Vote, models.Post.id == models.Vote.post_id, isouter=True)
        .group_by(models.Post.id)
        .filter(
            or_(
                models.Post.title.ilike(f"%{search}%"),
                models.Post.content.ilike(f"%{search}%")
            )
        )
        .limit(limit)
        .offset(skip)
        .all()
    )
    # Create a list of PostVote objects
    response = [PostVote(post=post, votes=votes) for post, votes in post]

    return response

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # SQL query to insert a new post
    # cur.execute("""
    #          INSERT INTO posts (title, content, published)
    #          VALUES (%s, %s, %s) RETURNING * 
    #     """,
    #     (post.title, post.content, post.published)
    #     )
    # new_post = cur.fetchone()
    
    # conn.commit()
    
    # SQLAlchemy ORM query to insert a new post
    # Note: `owner_id` is set to the current user's id
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # Refresh the instance to get the updated data from the database
    return new_post

@router.get("/{id}", response_model=PostVote)
def get_post_by_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # SQL query to fetch a post by id
    # cur.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cur.fetchone()
    # print(post)
    
    # SQLAlchemy ORM query to fetch a post by id
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    
    post_with_votes = (
        db.query(models.Post, func.count(models.Vote.post_id)
        .label("votes"))
        .join(models.Vote, models.Post.id == models.Vote.post_id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id).first()
    )
    
    if not post_with_votes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id:{id} not found"
        )
    
    post, votes = post_with_votes
    response = PostVote(post=post, votes=votes)
    return response

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # SQL query to delete a post by id
    # cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
    # deleted_post = cur.fetchone()
    # conn.commit()
    
    # SQLAlchemy ORM query to delete a post by id
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id:{id} not found"
        )

    if deleted_post.first().owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )
        
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=PostResponse)
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # SQL query to update a post by id
    # cur.execute("""
    #             UPDATE posts SET title = %s, content = %s, published = %s 
    #             WHERE ID = %s RETURNING *""",
    #             (post.title, post.content, post.published, str(id)))
    # updated_post = cur.fetchone()
    # conn.commit()
    
    # SQLAlchemy ORM query to update a post by id
    updated_post = db.query(models.Post).filter(models.Post.id == id)  

    if updated_post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id:{id} not found"
        )

    if updated_post.first().owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    updated_post.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return updated_post.first()

