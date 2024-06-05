


import sqlite3


connect = sqlite3.Connection("player.db")

c = connect.cursor()

with connect:
    c.execute("PRAGMA foreign_keys = ON")

def create_player_table() -> None:
    
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Player(
            player_name TEXT PRIMARY KEY)''')
        
def create_score_table() -> None:
    
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Score(
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            FOREIGN KEY (player_name) REFERENCES Player (player_name)
            ON DELETE CASCADE ON UPDATE CASCADE
        )''')

######################################################################


def insert_user_account(player_name: str) -> None:

    with connect:
        c.execute('''INSERT INTO Player (player_name)
                  VALUES (:player_name)''',
                {"player_name": player_name})


def insert_values(player_name: str,
                  score: int) -> None:
    with connect:
        c.execute('''INSERT INTO Score (player_name, score) 
                  VALUES (:player_name, :score)''', {"player_name": player_name,
                                                                "score": score})
        
###############################################################################        

def update_name(player_name: str,
                new_name: str) -> None:
    
    with connect:
        c.execute('''UPDATE Player
                  SET player_name = :new_name
                  WHERE player_name == :player_name''',
                  {"player_name": player_name,
                    "new_name": new_name})
        
def delete_player(player_name: str) -> None:
    
    with connect:
        c.execute('''DELETE FROM Player
                  WHERE player_name = :player_name''', {"player_name": player_name})

####################################################################################

def read_table(player_name: str) -> list:
    
    with connect:
        c.execute('''SELECT * FROM Score 
                  WHERE Score.player_name = :player_name
                  ORDER BY Score.score DESC
                  ''',
                  {"player_name": player_name})
        
        return c.fetchall()
    
def read_player_table() -> list:
    with connect:
        c.execute('''SELECT * FROM Player''')
        
    return  c.fetchall()


create_player_table()
create_score_table()


# insert_user_account("Mohammad")
# insert_user_account("Abravesh")

# insert_values("Amirali", 12)
# insert_values("Amirali", 15)
# insert_values("Mohammad", 30)
# insert_values("Abravesh", 80)

# read_table("Amirali")

# read_table("Abravesh")
# update_name("Abravesh", "Amirmahdi")
# read_table("Amirmahdi")

# delete_player("Amirmahdi")

# read_table("Amirmahdi")


