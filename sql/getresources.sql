CREATE OR REPLACE FUNCTION getresources(outeruserid bigint)
 RETURNS setof resource
AS $BODY$
BEGIN
    return query select r."alias", r."domain"
        from resource as r
        inner join user_resource as ur
            on r.id_resource = ur.resource_id
        where ur.user_id = (select * from getuserid(outeruserid));
END;
$BODY$
  LANGUAGE plpgsql;