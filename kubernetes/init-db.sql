CREATE DATABASE Enterprise;

       \c Enterprise

       CREATE TABLE IF NOT EXISTS employees (
        employee_id   CHAR(9)      NOT NULL,
        last_name     VARCHAR(25)  NOT NULL,
        first_name    VARCHAR(25)  NOT NULL,
        infix         VARCHAR(25),
        street        VARCHAR(50),
        location      VARCHAR(25),
        province      CHAR(2),
        postal_code   VARCHAR(7),
        birth_date    DATE,
        salary        NUMERIC(7, 2),
        parking_spot  NUMERIC(4),
        gender        CHAR,
        department_id NUMERIC(2),
        manager_id    CHAR(9)
    );



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
        ('666666666', 'Brown', 'Brenda', 'B', '4444 Willow St', 'Toronto', 'ON', 'M8A 8A8', '1994-01-01', 30000.00, 47, 'F', 3, '999666666');