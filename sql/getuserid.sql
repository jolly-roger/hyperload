CREATE OR REPLACE FUNCTION getuserid(facebookuserid bigint) returns bigint AS
$BODY$
declare
    local_id_user bigint;
BEGIN
    if not (case when (select true from "user" where facebook_user_id = facebookuserid limit 1) then true else false end) then
        insert into "user"(facebook_user_id) values(facebookuserid);
    end if;
    
    select into local_id_user id_user from "user" where facebook_user_id = facebookuserid limit 1;
    
    return local_id_user;
END;
$BODY$
  LANGUAGE plpgsql;