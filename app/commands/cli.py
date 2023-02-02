import os
import typer
import csv
from app.database.session import SessionLocal
from app.models.collection import Collection
from app.models.question import Question

app = typer.Typer()


@app.command()
def import_collections():
    data_path = os.path.join(os.path.dirname(__file__), './data')

    db = SessionLocal()
    with open(os.path.join(data_path, 'collections.csv')) as file:
        collections = csv.DictReader(file)
        for data in collections:
            collection = db.query(Collection).filter(
                Collection.slug == data['slug']).first()
            if collection:
                print(f'collection {collection.slug} is already exists')
                continue

            print(f'Creating collection {data["slug"]}.')
            collection = Collection(**data)
            db.add(collection)
        db.commit()


@app.command()
def import_questions():
    data_path = os.path.join(os.path.dirname(__file__), './data')

    db = SessionLocal()
    with open(os.path.join(data_path, 'questions.csv')) as file:
        questions = csv.DictReader(file)
        for data in questions:
            question = db.query(Question)\
                .filter(Question.title == data['title'])\
                .first()

            if question:
                print('Question is already exists')
                continue

            print(f'Creating question.')

            collection_slugs = data['collection_slug']
            data.pop('collection_slug')
            data['answer'] = int(data['answer'])

            question = Question(**data)

            for slug in collection_slugs.split(','):
                collection = db.query(Collection).filter(
                    Collection.slug == slug).first()

                if not collection:
                    print(f'collection {slug} is not found.')
                    continue

                collection.questions.append(question)
                db.add(collection)
            db.add(question)

        db.commit()
