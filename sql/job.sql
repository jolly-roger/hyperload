create sequence id_job_seq minvalue 0 start 0;


create table job (
	id_job bigint primary key not null default nextval('id_job_seq'),	
	"alias" varchar(256) not null
);


create table resource_job (
    resource_id bigint not null,
    job_id bigint not null
);