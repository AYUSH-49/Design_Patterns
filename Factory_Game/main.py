from Character import Character
# type: ignore

                                  

                                              

#def create_player(player_val):
  #  if player_val == 'knight':
   #     KnightFactory().create_player().attack()



if __name__ == '__main__':
    Player_Type = input("Enter player type (knight/archer/mage): ").strip().lower()
    Player= Character(Player_Type).create_player()
    