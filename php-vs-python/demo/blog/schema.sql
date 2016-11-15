drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username string not null,
    password text not null
    );

drop table if exists articles;
create table articles (
    id integer primary key autoincrement,
    title string not null,
    content text not null
    );

drop table if exists comments;
create table comments (
    id integer primary key autoincrement,
    content text not null,
    article_id integer not null,
    user_id integer not null
    );
