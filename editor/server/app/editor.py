# SPDX-License-Identifier: MIT

import os

from flask import (
    Blueprint,
    send_from_directory,
)

from . import root_dir
default_res_folder = os.path.join(root_dir, 'editor/web/dist')

bp = Blueprint('editor', __name__, url_prefix='/')


@bp.route('/', defaults={'path': 'index.html'})
@bp.route('/<path:path>')
def index(path: str):
    return send_from_directory(default_res_folder, path)
