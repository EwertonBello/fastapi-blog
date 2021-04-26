from sqlalchemy.orm import Session
from app.blogs import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session, user_id: int):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session, user_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.user_id == user_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted successfully'


def update(id: int, request: schemas.Blog, db: Session, user_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id, models.Blog.user_id == user_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    _update = {}
    request = request.dict()

    for _key in request:
        if request[_key]:
            _update[_key] = request[_key]

    blog.update(_update)
    db.commit()
    return 'updated successfully'


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog
