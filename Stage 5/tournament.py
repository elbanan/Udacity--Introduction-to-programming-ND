### Tournament python data file by Mohamed Elbanan 3/22/2016

#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach




def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament") #Connects to database





def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute ("delete from matches;")      #deletes all previously recorded matches
    c.execute ("ALTER SEQUENCE matches_matchid_seq RESTART WITH 1;")        #resets the primary key to begin again with 1
    db.commit()
    db.close()





def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute ("delete from players;")      #deletes all previously registered players
    c.execute ("ALTER SEQUENCE players_playerid_seq RESTART WITH 1;")       #resets the primary key to begin again with 1
    db.commit()
    db.close()





def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute ("select count(*) from players")      #counts number of players in players table
    db.commit()
    count= c.fetchone()[0]     #retruns count
    count = int(count)         #converts outpout from long to integer
    db.close()
    return count






def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    name=bleach.clean(name)     #ensure values entered are clean
    db = connect()
    c = db.cursor()
    c.execute ("insert into players (name) values(%s)",(name,))     #inserts player name into players table
    db.commit()
    db.close()
    return 'Congratulation! Player '+str(name)+' has been registered into tournament DB'        #Confirmation message of player registeration.




def showPlayers():
    db = connect()
    c = db.cursor()
    c.execute ("select * from players")
    playerslist = c.fetchall ()
    db.commit()
    db.close()
    x = 0
    while x < len(playerslist):
        print playerslist[x]
        x=x+1





def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute ("insert into matches (winner, loser) values ({0},{1})".format(winner,loser))     #inserts match report into database.
    db.commit()
    db.close()







def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute ("select * from standings;")
    output = c.fetchall ()
    db.commit()
    db.close()
    return output






def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Return:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standing = playerStandings()                                                     #selects current standing from database
    wins = [(i[2]) for i in standing]                                                #gets numbers of winnings acheived in between players
    wins = list(set(wins))                                                           #creates a list of number of winnings achieved
    pairs = []
    for x in wins:
        p = ((player[0],player[1]) for player in standing if player [2]== x)         #selects player id and player name per each win record
        p = zip(*[iter(p)]*2)                                                        #combines them into pairs
        x = x+1
        pairs = pairs + p                                                            #appends all pairs of all win records in one list
    output = [(pair[0]+pair[1]) for pair in pairs]                                   #combines id and name of players in each pair into a single tuple
    return output






