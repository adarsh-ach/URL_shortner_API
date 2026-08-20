import secrets
import string

from sqlalchemy.orm import Session

from .models import URL


def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def create_short_url(db: Session, original_url: str) -> URL:
    while True:
        short_code = generate_short_code()

        existing_url = (
            db.query(URL)
            .filter(URL.short_code == short_code)
            .first()
        )

        if not existing_url:
            break

    url = URL(
        original_url=original_url,
        short_code=short_code,
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url


def get_url_by_short_code(db: Session, short_code: str) -> URL | None:
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )