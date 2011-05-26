delete from users;
insert into users (username, email, password, role) values ('admin', 'anders@alphabits.dk', 'lol000', 'admin');
insert into users (username, email, password, role) values ('david', 'da@jello.dk', 'lol000', 'member');

delete from questions;
insert into questions ('id', 'title', 'template', 'languages_allowed') values ('php-prettify', 'PHP Prettify', 'quiz/php-prettify.html', 'php,normal-text');
insert into questions ('id', 'title', 'template', 'languages_allowed') values ('calling-a-webservice', 'Calling a webservice', 'quiz/calling-a-webservice.html', 'php,python,bash,normal-text');

delete from answers;
