https://www.testdome.com/d/sql-interview-questions/17

--1
select count(*) from students where firstName = 'John';


--2
update enrollments set year = 2015 where id between 20 and 100;


--3
select distinct name from dogs
union
select distinct name from cats;

--4
with s_grouped as (
  select userId, avg(duration) as avg, count(id) as count
  from sessions
  group by userId
)
select userId, avg from s_grouped
where count > 1;


--5
with sellers4 as (
  select * from sellers
  where rating > 4
)
select items.name, sellers4.name
from items
join sellers4
on items.sellerId = sellers4.id;


--6
with managers as (
  select distinct managerId as id from employees
)
select name from employees
left join managers on employees.id = managers.id
where managers.id is null


--7
CREATE TABLE users_roles (
  userId INTEGER not null references users(id),
  roleId INTEGER not null references roles(id),
  unique (userId,roleId)
);