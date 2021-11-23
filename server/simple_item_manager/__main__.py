#!/usr/bin/env python3

import connexion
from flask_cors import CORS

from simple_item_manager import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '簡易物品管理WebAPI'},
                pythonic_params=True)

    # add CORS support
    CORS(app.app)

    app.run(port=5001)


if __name__ == '__main__':
    main()
