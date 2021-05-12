drop table employee;, tr_instance, grading_type, education_type, process, grading


create table employee (
id INTEGER,
employee_name VARCHAR(50),
direct_supervisor INTEGER,
department_head INTEGER,
available_reimbursement NUMERIC(20,2) DEFAULT 1000.00,
title VARCHAR(50)
);
insert into employee 
(id, employee_name, direct_supervisor, department_head, available_reimbursement, title)
VALUES 
(1 , 'Adam', 2, 2, DEFAULT, 'Benefits Coordinator'),
(2, 'Betty', 0, 0, DEFAULT, 'Accounting Head' ),
(3, 'Chris', 0, 0, DEFAULT, 'Human Resources Head'),
(4, 'Doug', 0, 0, DEFAULT, 'Operations Head'),
(5, 'Edward', 0, 4, DEFAULT, 'Operations Supervisor'),
(6, 'Fred', 0, 2, DEFAULT, 'Accounting Supervisor'),
(7, 'Georgia', 5, 4, DEFAULT, 'Operations Employee'),
(8, 'Henry', 6, 2, DEFAULT, 'Accounting Employee'),
(9, 'Issac', 0, 3, DEFAULT, 'Human Resources Supervisor'),
(10, 'Jesse', 9, 3, DEFAULT, 'Human Resources Employee'),
(11, 'Kyle', 9, 3, DEFAULT, 'Human Resources Employee'),
(12, 'Lee', 6, 2, DEFAULT, 'Accounting Employee'),
(13, 'Matthew', 5, 4, DEFAULT, 'Operations Employee');



select * from employee;
select employee_name, title from employee


insert into tr_instance (date_current, training_location, description, full_cost, work_justification, start_date, days_long, education_type_id, employee_id)
values
('2021-05-02')










create table tr_instance(
id SERIAL primary key,
date_current DATE,
training_location VARCHAR(50),
description VARCHAR,
full_cost NUMERIC(20,2), 
work_justification VARCHAR,
start_date DATE,
days_long INTEGER,
education_type_id INTEGER,
employee_id INTEGER
);
select * from tr_instance; 
create table grading_type(    
id SERIAL primary key,
graded Boolean,
score INTEGER DEFAULT 70,
tr_instance_id integer
);


select * from grading_type ; 


create table education_type(
id Integer, 
type_name VARCHAR(50),
percentage INTEGER
);
insert into education_type values 
(1, 'university course', 80),
(2, 'seminars', 60),
(3, 'certification preparation class', 75),
(4, 'certification', 100),
(5, 'technical training', 90),
(6, 'other', 30);
select * from education_type;


drop table process
create table process( 
id SERIAL primary key,
process_name VARCHAR(50),
step INTEGER,
begin_date VARCHAR(15),
completed VARCHAR(10),
tr_instance_id INTEGER
);
select * from process; 



create table grading(    
id SERIAL primary key,
status VARCHAR(50),
grade_final INTEGER,
verification_person INTEGER,
tr_instance_id integer
);
select * from grading; 




create table uploaded_files( 
id SERIAL primary key,
file_type VARCHAR(50),
file_name text, 
binary_data bytea,
tr_instance_id INTEGER
);
select * from uploaded_files; 
