from client.factory import KnightFactory # type: ignore





def create_player(player_val):
    if player_val == 'knight':
        KnightFactory().create_player().attack()



if __name__ == '__main__':
    create_player('Knight')