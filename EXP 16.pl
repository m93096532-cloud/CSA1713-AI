
% Database containing name and date of birth
person(ravi, '2004-05-12').
person(priya, '2003-08-21').
person(ajay, '2004-01-15').
person(divya, '2005-11-30').

% Query to display all records
show_all :-
    person(Name, DOB),
    write('Name: '),
    write(Name),
    write(', DOB: '),
    write(DOB),
    nl,
    fail.
show_all.
