-- Tournament sql by Mohamed Elbanan 3/22/2016


-- deletes older versions of the databse before running the project for the first time
drop database if exists tournament ;



-- creates the database
create database tournament ;



--connects to the database
 \c tournament



-- creates tournament players table
create table players (name text, playerid serial primary key);




-- creates tournament matches table
create table matches (winner integer references players(playerid), loser integer references players(playerid), matchid serial primary key) ;




-- creates view to show wins per player
create view wins as
select name, playerid, cast(count(winner) as integer) as wins
    from  (select * from players left join matches on players.playerid = matches.winner) as winstable
    group by name , playerid
    order by playerid;




-- creates view to show matches played per player
create view matches_played as
select name,playerid, cast(count(matchid) as integer) as matchesplayed
    from (select * from players left join matches on players.playerid = matches.winner or players.playerid = matches.loser) as matchestable
    group by name, playerid
    order by playerid ;




-- creates view to show current standing of each player including wins and total matches played
create view standings as
    select  matches_played.playerid, matches_played.name, wins, matchesplayed
    from matches_played left join wins
    on matches_played.playerid = wins.playerid
    group by matches_played.name, matches_played.playerid, wins, matchesplayed
    order by playerid ;



