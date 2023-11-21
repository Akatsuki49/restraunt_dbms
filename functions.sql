USE restaurant_db;
DROP PROCEDURE IF EXISTS update_inventory_procedure;

DELIMITER $$

CREATE PROCEDURE update_inventory_procedure(IN f_id INT, IN q INT)
BEGIN
    DECLARE ingr_id_var INT;
    DECLARE ingr_qty_var INT;
    
    -- Cursor to fetch ingredients and their quantities used in the food item
    DECLARE ingr_cursor CURSOR FOR
        SELECT ingr_id, quantity
        FROM recepie
        WHERE recepie.f_id = f_id;

    -- Declare continue handler for cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET @done = 1;

    OPEN ingr_cursor;
    
    ingr_loop: LOOP
        FETCH ingr_cursor INTO ingr_id_var, ingr_qty_var;
        IF @done = 1 THEN
            LEAVE ingr_loop;
        END IF;

        -- Update the inventory for each ingredient
        UPDATE ingredients 
        SET avail_quantity = avail_quantity - (ingr_qty_var * q)
        WHERE ingr_id = ingr_id_var;
    END LOOP;

    CLOSE ingr_cursor;
    SET @done = 0; -- Reset @done variable
END;
$$

DELIMITER ;

