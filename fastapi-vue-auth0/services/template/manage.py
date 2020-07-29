import click


@click.group()
def cli():
    pass


@cli.command("test")
def test():
    import os
    import sys
    import pytest
    _environ = dict(os.environ)
    try:
        os.environ["APP_ENV"] = "test"
        result = pytest.main(["-x", "app/test"])
        if result == pytest.ExitCode.OK:
            return 0
        sys.exit(result.value)
    finally:
        os.environ.clear()
        os.environ.update(_environ)


@cli.command("init")
def init():
    import os

    from sqlalchemy import create_engine

    from app.main.database import Base
    from app.main.api.user.models import User # noqa

    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(bind=engine)


@cli.command("drop-tables")
def drop_tables():
    import os

    from sqlalchemy import create_engine

    from app.main.database import Base
    from app.main.api.user.models import User

    tables = [User.__table__]
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.drop_all(bind=engine, tables=tables)



if __name__ == "__main__":
    cli()
