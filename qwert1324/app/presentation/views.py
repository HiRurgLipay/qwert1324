from typing import Any, Dict

from flask import Blueprint, render_template, request, jsonify
from qwert1324.app.data_access.models import FormData

bp: Blueprint = Blueprint('presentation', __name__)


@bp.route('/')
def index() -> Any:
    return render_template('index.html')


@bp.route('/submit', methods=['POST'])
def submit() -> Any:
    data: Dict[str, str] = request.form.to_dict()
    form_data: FormData = FormData(data=data)
    form_data.save()
    return jsonify(success=True)
