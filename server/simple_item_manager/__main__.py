#!/usr/bin/env python3

import connexion
from flask_cors import CORS

from simple_item_manager import encoder
from simple_item_manager.db import db
from server.simple_item_manager.db import init_db
from simple_item_manager.config import DevelopmentConfig


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '簡易物品管理WebAPI'},
                pythonic_params=True)

    # add CORS support
    CORS(app.app)

    # 設定読み込み
    app.app.config.from_object(DevelopmentConfig())

    # DB初期化
    app.app.app_context().push()
    init_db(app.app)

    app.run(port=5001)


if __name__ == '__main__':
    main()
