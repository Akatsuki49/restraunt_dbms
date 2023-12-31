use restaurant_db;
CREATE TABLE chef (emp_id int, emp_name varchar(20),age int, head_id int, PRIMARY KEY(emp_id));

ALTER TABLE chef ADD FOREIGN KEY (head_id) REFERENCES chef(emp_id);

CREATE TABLE waiter (w_id int, w_name varchar(20), age int, PRIMARY KEY(w_id));

CREATE TABLE tables(table_no int, capacity int, reserved bool, w_id int, PRIMARY KEY(table_no), FOREIGN KEY(w_id) REFERENCES waiter(w_id));

CREATE TABLE food_items (f_id int,f_name varchar(30), price int, category varchar(20), cuisine varchar(20), prep_time int, PRIMARY KEY(f_id));

CREATE TABLE ingredients(ingr_id int, ingr_name varchar(20), avail_quantity int, expr_date date, PRIMARY KEY(ingr_id)); 

CREATE TABLE bill(table_no int, f_id int, quantity int, PRIMARY KEY(f_id, table_no), FOREIGN KEY(table_no) references tables(table_no), FOREIGN KEY(f_id) references food_items(f_id));

CREATE TABLE recepie(f_id int, ingr_id int, quantity int, PRIMARY KEY(f_id,ingr_id),FOREIGN KEY(f_id) references food_items(f_id), FOREIGN KEY(ingr_id) references ingredients(ingr_id));

CREATE TABLE chef_preps_food(emp_id int, f_id int, PRIMARY KEY(emp_id,f_id),FOREIGN KEY(emp_id) references chef(emp_id), FOREIGN KEY(f_id) references food_items(f_id));