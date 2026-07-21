# Write your MySQL query statement below
SELECT lastname,firstname,city,state FROM Address RIGHT JOIN Person ON Address.personid = Person.personid;