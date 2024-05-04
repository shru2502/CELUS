from .extractor import Extractor
from .loader import Loader
from .models import create_tables
from .transformer import Transformer


def run_etl(input_file: str, connection_url: str):
    """
    Runs whole ETL pipeline

    Args:
        input_file: path to the source file
        connection_url: the URL to an SQL database.
    """
    create_tables(connection_url)
    extractor = Extractor(input_file)
    transformer = Transformer(extractor.extract_data())
    loader = Loader(transformer.transform_data(), connection_url)

    loader.load_data()
