import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

engine = create_engine('sqlite:///db/bellybutton.sqlite')
Base = automap_base()
Base.prepare(engine, reflect = True)

SampleMetaData = Base.classes.sample_metadata

session = Session(engine)
session.querry(SampleMetaData).all()


if __name__ == "__main__":
    app.run()
