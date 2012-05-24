CREATE OR REPLACE FUNCTION getjob(jobid bigint)
 RETURNS setof job
AS $BODY$
BEGIN
    return query select j.*
        from job as j
        where j.id_job = jobid;
END;
$BODY$
  LANGUAGE plpgsql;