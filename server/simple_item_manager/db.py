# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MItem(db.Model):
    __tablename__ = 'm_item'
    __table_args__ = {'comment': '物品マスタ'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('m_item_id_seq'::regclass)"), comment='物品ID')
    name = db.Column(db.String, comment='物品名')
    image = db.Column(db.LargeBinary, comment='物品画像')
    created_at = db.Column(db.DateTime(True), comment='作成日時')
    created_by = db.Column(db.Integer, comment='作成者')
    updated_at = db.Column(db.DateTime(True), comment='更新日時')
    updated_by = db.Column(db.Integer, comment='更新者')


class MUser(db.Model):
    __tablename__ = 'm_user'
    __table_args__ = {'comment': 'ユーザマスタ'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('m_user_id_seq'::regclass)"), comment='ユーザID')
    name = db.Column(db.String, comment='ユーザ名')
    serial_no = db.Column(db.String, comment='NFCのシリアル番号')
    is_valid = db.Column(db.Boolean, comment='有効フラグ')
    created_at = db.Column(db.DateTime(True), comment='作成日時')
    created_by = db.Column(db.Integer, comment='作成者')
    updated_at = db.Column(db.DateTime(True), comment='更新日時')
    updated_by = db.Column(db.Integer, comment='更新者')


class TUsage(db.Model):
    __tablename__ = 't_usage'
    __table_args__ = {'comment': '使用履歴'}

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('t_usage_id_seq'::regclass)"), comment='使用履歴ID')
    user_id = db.Column(db.Integer, comment='使用者ユーザID')
    start_at = db.Column(db.DateTime(True), comment='使用開始日時')
    end_at = db.Column(db.DateTime(True), comment='使用終了日時')


class TUsageItem(db.Model):
    __tablename__ = 't_usage_item'
    __table_args__ = {'comment': '使用した物品組合せトラン'}

    usage_id = db.Column(db.Integer, primary_key=True, nullable=False, comment='使用履歴ID')
    item_id = db.Column(db.Integer, primary_key=True, nullable=False, comment='物品ID')
