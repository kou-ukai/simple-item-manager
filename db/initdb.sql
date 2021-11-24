-- Table: public.m_item

-- DROP TABLE public.m_item;

CREATE TABLE public.m_item
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    image bytea,
    created_at timestamp with time zone,
    created_by character varying COLLATE pg_catalog."default",
    updated_at timestamp with time zone,
    updated_by character varying COLLATE pg_catalog."default",
    CONSTRAINT item_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.m_item
    OWNER to simple;

COMMENT ON TABLE public.m_item
    IS '物品マスタ';

COMMENT ON COLUMN public.m_item.id
    IS '物品ID';

COMMENT ON COLUMN public.m_item.name
    IS '物品名';

COMMENT ON COLUMN public.m_item.image
    IS '物品画像';

COMMENT ON COLUMN public.m_item.created_at
    IS '作成日時';

COMMENT ON COLUMN public.m_item.created_by
    IS '作成者';

COMMENT ON COLUMN public.m_item.updated_at
    IS '更新日時';

COMMENT ON COLUMN public.m_item.updated_by
    IS '更新者';


-- Table: public.m_user

-- DROP TABLE public.m_user;

CREATE TABLE public.m_user
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    serial_no character varying COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone,
    created_by character varying COLLATE pg_catalog."default",
    updated_at timestamp with time zone,
    updated_by timestamp with time zone,
    CONSTRAINT user_pkey PRIMARY KEY (id, name)
)

TABLESPACE pg_default;

ALTER TABLE public.m_user
    OWNER to simple;

COMMENT ON TABLE public.m_user
    IS 'ユーザマスタ';

COMMENT ON COLUMN public.m_user.id
    IS 'ユーザID';

COMMENT ON COLUMN public.m_user.name
    IS 'ユーザ名';

COMMENT ON COLUMN public.m_user.serial_no
    IS 'NFCのシリアル番号';

COMMENT ON COLUMN public.m_user.created_at
    IS '作成日時';

COMMENT ON COLUMN public.m_user.created_by
    IS '作成者';

COMMENT ON COLUMN public.m_user.updated_at
    IS '更新日時';

COMMENT ON COLUMN public.m_user.updated_by
    IS '更新者';


-- Table: public.t_usage

-- DROP TABLE public.t_usage;

CREATE TABLE public.t_usage
(
    id integer NOT NULL DEFAULT nextval('t_usage_id_seq'::regclass),
    user_id integer,
    start_at timestamp with time zone,
    end_at timestamp with time zone,
    CONSTRAINT t_usage_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.t_usage
    OWNER to simple;

COMMENT ON TABLE public.t_usage
    IS '使用履歴';

COMMENT ON COLUMN public.t_usage.id
    IS '使用履歴ID';

COMMENT ON COLUMN public.t_usage.user_id
    IS '使用者ユーザID';

COMMENT ON COLUMN public.t_usage.start_at
    IS '使用開始日時';

COMMENT ON COLUMN public.t_usage.end_at
    IS '使用終了日時';


-- Table: public.t_usage_item

-- DROP TABLE public.t_usage_item;

CREATE TABLE public.t_usage_item
(
    usage_id integer NOT NULL,
    item_id integer NOT NULL,
    CONSTRAINT t_usage_item_pkey PRIMARY KEY (usage_id, item_id)
)

TABLESPACE pg_default;

ALTER TABLE public.t_usage_item
    OWNER to simple;

COMMENT ON TABLE public.t_usage_item
    IS '使用した物品組合せトラン';

COMMENT ON COLUMN public.t_usage_item.usage_id
    IS '使用履歴ID';

COMMENT ON COLUMN public.t_usage_item.item_id
    IS '物品ID';