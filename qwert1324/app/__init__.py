from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from qwert1324.app.presentation import bp as presentation_bp
from qwert1324.app.data_access.models import Base


app = Flask(__name__, template_folder="presentation/templates/", static_folder="presentation/static")

engine = create_engine('postgresql://hirurg:1324@localhost/qwert1324')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

app.register_blueprint(presentation_bp)

if __name__ == '__main__':
    app.run(debug=True)
