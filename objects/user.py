import sys

sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')

from extra.database import insert_user_account, delete_player, update_name, read_table, insert_values, read_player_table

class UserList:

    def __init__(self) -> None:
        self.list = ["PLAYER"]
        self.current_value = 1
        self.user_account_dictionary = {}
        
        
    def insert_user(self,
                    user_name: str) -> None:
        if user_name not in self.list:
            self.list.append(user_name)
            insert_user_account(user_name)
        else:
            pass #TODO - display a Error window, which shows that the entered name is duplicate and must be unique.
              
              
    def delete_user(self,
                    user_name: str) -> None:
        if user_name in self.list:
            self.list.remove(user_name)
            delete_player(user_name)
        else:
            pass #TODO - display a Error window, which shows that the player is not exist
    
    
    def change_user_name(self,
                         new_user_name: str) -> None:
        if new_user_name not in self.list:
            update_name(self.get_current_value(), new_user_name)
            self.user_account_dictionary[self.current_value] = new_user_name
        else:
            pass #TODO - display a error window, which show that the player is already exist
    
    
    def update_user_preset(self) -> None:
        self.user_account_dictionary = {index : user_name for index ,user_name in enumerate(self.list, 1)}
        
    def update_list(self) -> None:
        player_names = read_player_table()
        self.list = [value[0] for value in player_names]
        
        
    def get_current_value(self) -> str:
        return self.user_account_dictionary[self.current_value]
    
    
    def next_user(self) -> None:
        if self.current_value < len(self.user_account_dictionary):
            self.current_value += 1
            
    def perv_user(self) -> None:
        if self.current_value > 1:
            self.current_value -= 1
            
    def show_current_user_leaderboard(self,
                                      user_name: str) -> None:
        if user_name in self.list:
            read_table(user_name)
        else:
            pass #TODO - display a error message which indicates that the player is not exist.
        
    def insert_name_score(self, player_name, score) -> None:
        if player_name in self.list:
            insert_values(player_name, score)
        else:
            pass
        
    def read_db(self) -> None:
        self.list = read_player_table()
    
user_list = UserList()

user_list.update_user_preset()
