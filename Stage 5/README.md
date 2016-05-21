##**Udacity IPND - Stage 5 - Backend porgramming pathway graduation project**

This is the tournament application created by Mohamed Elbanan (Last version on 3/22/2016).

The application's purpose is to create a single swiss tournament from registered players and matches.

This file will help users to understand how to use the application.

This application uses a database called "Tournament" including 2 tables "player" and "matches".

All sql commands required to build database, tables and view are included in tournament.sql file.

Run psql in your terminal and import tournament.sql using command: \i tournament.sql

Now all data structure have been created.

The following are definitions of the variable python functions that are built specifically for this tournament.

**registerPlayer(name)** : registers a new player with name in between brackets

**showPlayers()** : shows a list of all registered players and their unique IDs.

**countPlayers()** : returns the number of players currently registered in the database.

**deletePlayers()** : deletes all players in tournament database.

**reportMatch(winner, loser)** : records the result of a match between 2 players. Note that winner and loser refer to players unique id.

**deleteMatches()**: deletes all matches recorded in the tournament.

**playerStandings()** : returns the current standing of each player in terms of wins and matches played.

**swissPairings()**: returns pairs of players for next round of matches based on number of wins and matches played.

