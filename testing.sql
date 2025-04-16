use brainflex;

#admin
#insert new student data
SELECT * FROM Students
#insert
#NUID: 581298319
#First and last name : "Bob Smith"
ORDER BY user_id DESC;

#delete student data
SELECT * FROM Students
#delete
#where user_id = 42
ORDER BY user_id DESC;

#advisor
# create a new request to an admin
SELECT * FROM Requests
#request_id: 41
#description: "Database was not found on local machine"
#sent by: nothing
#type_id: 6
ORDER BY request_id DESC;
