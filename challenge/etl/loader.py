from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models import CakeModel


def connect(connection_url: str) -> Session:
    """
    Connects to the database and returns a Session object.

    Args:
        connection_url: the URL to an SQL database.
    """
    Session = sessionmaker()
    Session.configure(bind=create_engine(connection_url, echo=True))
    return Session()


class Loader:
    def __init__(self, cake_data: List[CakeModel], connection_url: str):
        """
        This class loads transformed data into the database

        Args:
            cake_data: transformed data
            connection_url: the URL to an SQL database.
        """
        self.session = connect(connection_url)
        self.cake_data = cake_data

    def load_data(self):
        """
        Inserts data into the database
        """
        raise NotImplementedError
