CREATE DATABASE college;
USE college; 
create table student(rollno int primary key, name varchar(50));
insert into student (rollno,name)values(101,"Karan"),(102,"Arjun");
insert into student values(103,"Ram");
insert into student (rollno,name) values(104,"Nikhil"),(105,"Shubham");
select * from student;
create table temp1(id int unique);
insert into temp1 values(101);
create table emp(id int,salary INT default 25000);
insert into emp(id)values (101);
select * from emp;
create table student1(rollno int primary key,name varchar(30),marks int not null,grade varchar(10),city varchar(20));
insert into student1(rollno,name,marks,grade,city) values
(101,"Anil",78,"C","Pune"),
(102,"Bhumika",93,"A","Mumbai"),
(103, "chetan", 85, "B", "Mumbai"),
(104, "dhruv", 96, "A", "Delhi"),
(105, "emanuel", 12, "F", "Delhi"),
(106, "farah", 82, "B", "Delhi");
select * from student1 where marks>80;
select * from student1 where city="Mumbai";
select * from student1 where marks between 80 and 90;
select * from student1 where city in("Mumbai","Delhi");
select * from student1;
select * from student1 where marks >75 limit 3;
select * from student1 order by marks desc limit 3;
select city,count(rollno) from student1 group by city;
select count(name),city from student1 group by city having max(marks)>75;
update student1 set grade="O" where grade="A";
delete from student1 where marks<33;
update student1 set marks=12 where rollno=105;

create table dept(id int primary key, name varchar(30));
insert into dept values(101,"English"),(102,"IT");
create table teacher(id int primary key,name varchar(30),dept_id int,foreign key(dept_id) references dept(id) on update cascade on delete cascade);
insert into teacher values (101,"Adam",101),(102,"Eve",102);
select * from teacher,dept;
alter table student1 add Current_age INT not null default 18;
select * from student1;
ALTER TABLE student1
DROP COLUMN age;
alter table student1 rename to student;
CREATE TABLE student1 (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
INSERT INTO student1 (id, name)
VALUES
(101, 'adas'),
(102, 'bob'),
(103, 'casey');

CREATE TABLE course (
    id INT,
    course VARCHAR(50)
);
INSERT INTO course (id, course)
VALUES
(102, 'english'),
(105, 'math'),
(103, 'science'),
(107, 'computer science');
select * 
from student1 as A
inner join course as B
on A.id=B.id;

select * 
from student1 as s
left join course as c
on s.id=c.id;

select * 
from student1 as s
right join course as c
on s.id=c.id;


select * 
from student1 as s
left join course as c
on s.id=c.id
UNION
select * 
from student1 as s
right join course as c
on s.id=c.id;




 