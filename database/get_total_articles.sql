CREATE OR REPLACE FUNCTION get_total_articles()
  RETURNS int AS
$$
BEGIN
  RETURN (

  SELECT COUNT(*) 
  FROM articles);
END; $$

LANGUAGE plpgsql;
