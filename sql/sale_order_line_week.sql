CREATE OR REPLACE FUNCTION public.set_sale_order_line_dlvy_year_week()
  RETURNS trigger AS
$BODY$
BEGIN
  IF NEW.dlvy_date is not null THEN
     NEW.dlvy_week = cast(extract(year from NEW.dlvy_date) as char(4)) || '-' || right('0' || cast(extract(week from NEW.dlvy_date) as char(2)),2) ;
  END IF;
  RETURN NEW;
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.set_sale_order_line_dlvy_year_week()
  OWNER TO odoo;


CREATE TRIGGER sale_order_line_insert_update_dlvy_week
  BEFORE INSERT OR UPDATE
  ON public.sale_order_line
  FOR EACH ROW
  EXECUTE PROCEDURE public.set_sale_order_line_dlvy_year_week();