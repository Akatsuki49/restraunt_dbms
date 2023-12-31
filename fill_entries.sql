use restaurant_db;
INSERT INTO chef VALUES
(1001,"Martin",32,NULL),
(1002,"Suresh",41,NULL),
(1003,"Irfan",38,NULL),
(2001,"Rohit",21,1001),
(2012, "Kiran",18,1001),
(2391, "Arif", 21, 1002),
(2023,"Shubham", 23,1003);



INSERT INTO waiter VALUES
(201,"Suresh",21),
(242,"Jimin", 27),
(311,"Josh",19),
(266,"Suman",24);

INSERT INTO tables VALUES
(1,4,false,201),
(2,4,false,242),
(3,2,true,311),
(4,6,true,266),
(5,4,false,311);

INSERT INTO food_items VALUES
(1321,"kadai paneer", 160, "main","Indian", 15),
(3223,"Al-faham", 300, "main", "Arabian",10),
(7213, "shawarma", 80,"starter", "Arabian", 10),
(2212,"chilli noodles", 130,"starter","Chinese", 15);

INSERT INTO ingredients VALUES
(1121,"paneer",33,"2022-12-01"),
(4211,"Chicken",10,"2022-11-15"),
(3002,"Wheat",20,"2023-01-10"),
(8890,"tomatoes",50,"2022-11-16"),
(3313,"Noodles",20,"2023-03-01");

INSERT INTO recepie VALUES
(1321,1121,1), (1321,8890,3),
(3223,4211,1),
(7213,4211,0.5),(7213,3002,0.5),
(2212,3313,1),(2212,8890,2);

INSERT INTO chef_preps_food VALUES
(1001,1321),(2001,1321),
(1001,2212),(2012,2212),
(1002,3223),(2391,3223),
(1003,7213),(2023,7213);


INSERT INTO bill VALUES
(1,1321,2),(1,2212,1),
(2,7213,4),(2,3223,2),(2,1321,1),
(3,2212,2),
(4,1321,4),(4,2212,2),
(5,7213,4);
