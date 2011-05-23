delete from users;
insert into users (username, email, password, role) values ('admin', 'anders@alphabits.dk', 'lol000', 'admin');
insert into users (username, email, password, role) values ('david', 'da@jello.dk', 'lol000', 'member');

delete from questions;
insert into questions ('id', 'title', 'template', 'status') values ('php-prettify', 'PHP Prettify', 'quiz/php-prettify.html', 'closed');

delete from answers;
