-- Data insertion
INSERT INTO employees
    (employee_id, last_name, first_name, infix, street, location, province, postal_code, birth_date, salary, parking_spot, gender, department_id, manager_id)
VALUES
    ('999666666', 'Bordoloi', 'Bijoy', '', 'Zuidelijke Rondweg 12', 'Eindhoven', 'NB', '6202 EK', '1977-11-10', 55000.00, 1, 'M', 1, NULL),
    ('999555555', 'Jochems', 'Suzan', '', 'Nuthseweg 17', 'Maastricht', 'LI', '9394 LR', '1981-06-20', 43000.00, 3, 'F', 3, '999666666'),
    ('999444444', 'Zuiderweg', 'Willem', '', 'Lindberghdreef 303', 'Oegstgeest', 'ZH', '2340 RV', '1985-08-12', 43000.00, 32, 'M', 7, '999666666'),
    ('999887777', 'Muiden', 'Martina', 'van der', 'Hoofdstraat 14', 'Maarssen', 'UT', '9394 LM', '1988-07-19', 25000.00, 402, 'F', 3, '999555555'),
    ('999222222', 'Amelsvoort', 'Henk', 'van', 'Zeestraat 14', 'Maastricht', 'LI', '9394 MK', '1979-03-29', 25000.00, 422, 'M', 3, '999555555'),
    ('999111111', 'Bock', 'Douglas', '', 'Monteverdidreef 2', 'Oegstgeest', 'ZH', '6312 CB', '1965-09-01', 30000.00, 542, 'M', 7, '999444444'),
    ('999333333', 'Joosten', 'Dennis', '', 'Eikenstraat 10', 'Groningen', 'GR', '6623 HK', '1982-09-15', 38000.00, 332, 'M', 7, '999444444'),
    ('999888888', 'Pregers', 'Shanya', '', 'Overtoomweg 44', 'Eindhoven', 'NB', '6202 MR', '1982-07-31', 25000.00, 296, 'F', 7, '999444444'),
    ('900000009', 'Johnson', 'Dan', 'Leo', 'Grotesteenweg 23', 'Berchem', 'BE', '2600 BE', '1992-10-09', 45000.00, 23, 'M', 7, '999666666'),
    ('123456789', 'Smith', 'John', 'J', '123 Main St', 'Toronto', 'ON', 'M1A 1A1', '1990-01-01', 20000.00, 40, 'M', 3, '999666666'),
    ('987654321', 'Johnson', 'Jane', 'J', '456 Elm St', 'Toronto', 'ON', 'M2A 2A2', '1995-01-01', 24000.00, 41, 'F', 7, '999555555'),
    ('111111111', 'Davis', 'David', 'D', '789 Oak St', 'Toronto', 'ON', 'M3A 3A3', '1992-01-01', 25000.00, 42, 'M', 3, '999666666'),
    ('222222222', 'Harris', 'Helen', 'H', '901 Maple St', 'Toronto', 'ON', 'M4A 4A4', '1998-01-01', 38000.00, 43, 'F', 3, '999555555'),
    ('333333333', 'Martin', 'Michael', 'M', '1111 Pine St', 'Toronto', 'ON', 'M5A 5A5', '1991-01-01', 29000.00, 44, 'M', 7, '999666666'),
    ('444444444', 'Taylor', 'Tina', 'T', '2222 Spruce St', 'Toronto', 'ON', 'M6A 6A6', '1996-01-01', 34000.00, 45, 'F', 7, '999666666'),
    ('555555555', 'Walker', 'William', 'W', '3333 Cedar St', 'Toronto', 'ON', 'M7A 7A7', '1993-01-01', 41000.00, 46, 'M', 3, '999666666'),
    ('666666666', 'Brown', 'Brenda', 'B', '4444 Willow St', 'Toronto', 'ON', 'M8A 8A8', '1994-01-01', 30000.00, 47, 'F', 3, '999666666');
