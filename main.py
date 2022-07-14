create table if not exists Genres (
    id serial primary key,
    name varchar(80) not null
);

create table if not exists Artist (
    id serial primary key,
    name varchar(80) not null
);

create table if not exists Album (
    id serial primary key,
    name varchar(80) not null,
    data_relaise date not null
);

create table if not exists Track (
    id serial primary key,
    name varchar(80) not null,
    duration time not null,
    album_id integer not null references album(id)
);

create table if not exists Compliation (
    id serial primary key,
    name varchar(80) not null,
    data_relaise date not null
);

create table if not exists Compliation_track (
    compliation_id integer references compliation(id),
    track_id integer references track(id),
    constraint pk primary key (compliation_id, track_id)
);

create table if not exists Genres_artist (
    genres_id integer references Genres(id),
    artist_id integer references Artist(id),
    constraint ak primary key (genres_id, artist_id)
);

create table if not exists Album_artist (
    album_id integer references Album(id),
    artist_id integer references Artist(id),
    constraint bk primary key (album_id, artist_id)
);