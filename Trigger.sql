use restaurant_db;

DELIMITER $$

CREATE TRIGGER bill_insert_trigger
AFTER INSERT ON bill
FOR EACH ROW
BEGIN
    UPDATE tables
    SET reserved = 1
    WHERE table_no = NEW.table_no;
END;
$$

DELIMITER ;
