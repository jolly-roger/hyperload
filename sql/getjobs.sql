CREATE OR REPLACE FUNCTION getjobs(resourceid bigint)
 RETURNS setof job
AS $BODY$
BEGIN
    return query select j.*
        from job as j
        inner join resource_job as rj
            on j.id_job = rj.job_id
        where rj.resource_id = resourceid;
END;
$BODY$
  LANGUAGE plpgsql;