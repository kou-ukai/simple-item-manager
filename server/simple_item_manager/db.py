# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, Integer, LargeBinary, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MItem(Base):
    __tablename__ = 'm_item'
    __table_args__ = {'comment': '物品マスタ'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('m_item_id_seq'::regclass)"), comment='物品ID')
    name = Column(String, comment='物品名')
    image = Column(LargeBinary, comment='物品画像')
    created_at = Column(DateTime(True), comment='作成日時')
    created_by = Column(Integer, comment='作成者')
    updated_at = Column(DateTime(True), comment='更新日時')
    updated_by = Column(Integer, comment='更新者')


class MUser(Base):
    __tablename__ = 'm_user'
    __table_args__ = {'comment': 'ユーザマスタ'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('m_user_id_seq'::regclass)"), comment='ユーザID')
    name = Column(String, comment='ユーザ名')
    serial_no = Column(String, comment='NFCのシリアル番号')
    is_valid = Column(Boolean, comment='有効フラグ')
    created_at = Column(DateTime(True), comment='作成日時')
    created_by = Column(Integer, comment='作成者')
    updated_at = Column(DateTime(True), comment='更新日時')
    updated_by = Column(Integer, comment='更新者')


class TUsage(Base):
    __tablename__ = 't_usage'
    __table_args__ = {'comment': '使用履歴'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('t_usage_id_seq'::regclass)"), comment='使用履歴ID')
    user_id = Column(Integer, comment='使用者ユーザID')
    start_at = Column(DateTime(True), comment='使用開始日時')
    end_at = Column(DateTime(True), comment='使用終了日時')


class TUsageItem(Base):
    __tablename__ = 't_usage_item'
    __table_args__ = {'comment': '使用した物品組合せトラン'}

    usage_id = Column(Integer, primary_key=True, nullable=False, comment='使用履歴ID')
    item_id = Column(Integer, primary_key=True, nullable=False, comment='物品ID')
