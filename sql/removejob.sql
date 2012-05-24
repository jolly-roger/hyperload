CREATE OR REPLACE FUNCTION removejob(jobid bigint)
 RETURNS boolean
AS $BODY$
BEGIN
    update job set is_removed = true where id_job = jobid;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;