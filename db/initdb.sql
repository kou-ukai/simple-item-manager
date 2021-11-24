-- Table: public.user

-- DROP TABLE public."user";

CREATE TABLE public."user"
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

ALTER TABLE public."user"
    OWNER to simple;

-- Table: public.user

-- DROP TABLE public."user";

CREATE TABLE public."user"
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

ALTER TABLE public."user"
    OWNER to simple;