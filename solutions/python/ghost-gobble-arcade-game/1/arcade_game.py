
def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without       his power pellet."""
    if power_pellet_active == False and touching_ghost == True:
        return True
    else:
        return False



def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    """
    if has_eaten_all_dots and power_pellet_active and touching_ghost :
        return True
    elif has_eaten_all_dots and touching_ghost == False:
        return True
    else:
        return False
