from database import get_engine
from extract import extract
from transform import transform
from load import load
from models import metadata


def run_pipeline():
    engine = get_engine()
    metadata.create_all(engine)

    raw_data = extract()
    if raw_data is None:
        return

    transformed_data = transform(raw_data)
    load(engine, transformed_data)
    print("Pipeline executado com sucesso.")


if __name__ == "__main__":
    run_pipeline()