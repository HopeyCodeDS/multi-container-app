-- create_table.sql

-- Table creation
CREATE TABLE employees (
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
    manager_id    CHAR(9),
    CONSTRAINT pk_employees PRIMARY KEY (employee_id)
);
