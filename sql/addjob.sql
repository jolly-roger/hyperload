CREATE OR REPLACE FUNCTION addjob(jobalias varchar(256), resourceid bigint)
 RETURNS bigint
AS $BODY$
declare
    new_job_id bigint;
BEGIN
    insert into job ("alias") values (jobalias) returning id_job
        into new_job_id;
    insert into resource_job values (resourceid, new_job_id);
    
    return new_job_id;
END;
$BODY$
  LANGUAGE plpgsql;