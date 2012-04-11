CREATE OR REPLACE FUNCTION getresource(resourceid bigint)
 RETURNS setof resource
AS $BODY$
BEGIN
    return query select r.*
        from resource as r
        where t.id_resource = resourceid;
END;
$BODY$
  LANGUAGE plpgsql;