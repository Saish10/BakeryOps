import click
import importlib
import datetime
from app import app, db
from sqlalchemy import inspect



@app.cli.command('loaddata')
@click.option('--file')
def loaddata(file):
    fixture_file = importlib.import_module(f"fixtures.{file}")
    json_data = fixture_file.data
    for data in json_data:
        model = getattr(importlib.import_module('models'), data["model"])
        fields = data["fields"]
        object = model.query.filter_by(id=fields["id"])

        if object.count() != 0:
            model_object = object.update(fields)
        else:
            model_object = model(**fields)
            db.session.add(model_object)

    db.session.commit()
    print("Fixture data loaded successfully.")


@app.cli.command('dumpdata')
@click.option('--model')
@click.option('--file')
def dumpdata(model, file):
    imported_model = getattr(importlib.import_module('models'), model)
    objects = imported_model.query.order_by('id')
    file = open(f'fixtures/{file}.py', "w")
    fixture_data = []
    for data in objects:
        fixture_dict = {"model": model, "fields": {}}
        for c in inspect(data).mapper.column_attrs:
            field = getattr(data, c.key)
            if isinstance(field, (datetime.datetime, datetime.date)):
                field = field.isoformat()
            fixture_dict["fields"][c.key] = field

        fixture_data.append(fixture_dict)

    file.write(f"data = {repr(fixture_data)}\n")
    file.close()
    print("Fixture data added successfully.")
