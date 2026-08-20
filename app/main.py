from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortener built with FastAPI and PostgreSQL.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}


@app.post("/shorten", response_model=schemas.URLResponse,status_code=201,)
def shorten_url(
    url_data: schemas.URLCreate,
    db: Session = Depends(get_db),
):
    url = crud.create_short_url(
        db=db,
        original_url=str(url_data.url),
    )

    return schemas.URLResponse(
        short_code=url.short_code,
        short_url=f"http://localhost:8000/{url.short_code}",
    )


@app.get("/{short_code}")
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db),
):
    url = crud.get_url_by_short_code(
        db=db,
        short_code=short_code,
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found",
        )

    return RedirectResponse(
        url=url.original_url,
        status_code=307,
    )