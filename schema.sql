drop table if exists users;
create table users(
  username text primary key,
  email text not null,
  password text not null

);
insert into users values('admin','admin@gmail.com' ,'Admin123');
insert into users values('yvonne', 'yvonne@gmail.com','Yvonne1215');

