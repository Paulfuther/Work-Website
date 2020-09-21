-- SQLite
select firstname, lastname, whmis.startdate from employee
inner join whmis on employee_id = Employee.id