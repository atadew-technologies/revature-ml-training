create table todo
(
    _id         bigint auto_increment
        primary key,
    uuid        varchar(100)                       not null,
    name        varchar(100)                       not null,
    createdDate datetime default CURRENT_TIMESTAMP null,
    updatedDate datetime                           null
);

create table todo_items
(
    _id      bigint auto_increment
        primary key,
    taskName varchar(100)                                    not null,
    status   enum ('COMPLETED', 'PENDING') default 'PENDING' not null
);

