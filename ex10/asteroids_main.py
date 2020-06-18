from screen import Screen
from ship import Ship
import sys
import random
import math
from asteroid import Asteroid
from point import Point
from torpedo import Torpedo
from speed_2d import Speed2D

TORPEDO_LIFE_TIME = 200
DEFAULT_ASTEROIDS_NUM = 5
MOVE_RIGHT=-1
MOVE_LEFT=1

class GameRunner:
    """
    The following represents a gameRunner object,
    which has a screen,
    list of sprites,
    list of torpedos,
    list of astroids,
    a ship,
    and screen constants limits.
    """
    def __init__(self, asteroids_amount):
        """
        The following makes a new GameRunner -
        it creates the astroids according to amount,
        sets a new astroids list,
        creates a new screen member,
        sets the limits of the screen,
        creates scores member,
        sets a new list of torpedos.

        :param asteroids_amount: Amount of astroid that should be in the game.
        """
        self.__screen = Screen()
        self.__asteroids = []
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__asteroids_amount=asteroids_amount
        self._ship=Ship(self.random_point(),Speed2D(0,0),0)
        self.add_asteroids()
        self._torpedos=[]
        self._score=0

    def update_score(self,size):
        """
        The following add scores to the
        scores counter, in addition, it
        set's screen scores bar,
        to show the current score.
        :param size: Size of the astroid
        which have destroyed
        :return:None
        """
        size_to_score={1:100,2:50,3:20}
        if size in size_to_score:
            self._score+=size_to_score[size]
            self.__screen.set_score(self._score)

    def deg_to_radians(self,deg):
        """
        The following converts
        degrees to radians.
        :param deg: a given degree
        :return: deg in radians
        """
        return math.radians(deg)

    def add_asteroids(self):
        """
        The following adds astorid
        to the current game,
        it adds the amount of astroid
        which was given in the constructor
        :return: None
        """
        for i in range(self.__asteroids_amount):
            asteroid_point = self.random_point()
            speed = Speed2D(random.randint(1,4),random.randint(1,4))
            new_asteroid = Asteroid(asteroid_point, speed, 3)
            while new_asteroid.has_intersection(self._ship):
                asteroid_point = self.random_point()
                speed = random.randint(1,4)
                new_asteroid = Asteroid(asteroid_point, speed, 3)
            self.__asteroids.append(new_asteroid)
            self.__screen.register_asteroid(new_asteroid, 3)
            self.__screen.draw_asteroid(new_asteroid
            , asteroid_point.get_x(), asteroid_point.get_y())

    def accelerate_ship(self,ship):
        """
        The following accelerates ship's speed by the formula
        new Speed= old speed+math.cos( ship's heading)
         (in both axis's X && Y)
        :param ship: Game's ship
        :return: None
        """
        new_speed_x=ship.get_speed().get_x_speed()\
                    +math.cos(self.deg_to_radians(ship.get_direction()))
        new_speed_y=float(ship.get_speed().get_y_speed())\
            +float(math.sin(self.deg_to_radians(ship.get_direction())))
        ship.set_speed(Speed2D(new_speed_y,new_speed_x))

    def astroid_intersection(self):
        """
        The following loops through each astroid in the game,
        and check intersection of it with 1. the ship , 2. torpedos.
        :return: Nobe
        """
        hit_asteroid=None
        hit_torpedo=None
        for key, asteroid in enumerate(self.__asteroids):
            if asteroid.has_intersection(self._ship):
                self._ship.decrease_ship_health()
                self.__screen.show_message\
                ('Asteroid hit!', 'You got hit by an asteroid,'
                    'your life is decreased by 1.')
                hit_asteroid=key
                if self._ship.get_life()>=0:
                    self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                break

            else:
                for torpedo_ind,torpedo in enumerate(self._torpedos):
                    torpedo=torpedo[0]
                    if asteroid.has_intersection(torpedo):
                        hit_torpedo=torpedo_ind
                        hit_asteroid=key
                        ## Make it double
                        self.__screen.unregister_asteroid(asteroid)
                        self.__screen.unregister_torpedo(torpedo)
                        break
                if hit_torpedo:
                    break
        if hit_torpedo is not None:
            ##update score
            self.update_score(self.__asteroids[hit_asteroid].get_size())
            ##divide astoid in correlation with it's size
            self.divide_asteroid\
            (self.__asteroids[hit_asteroid],self._torpedos[hit_torpedo][0])
            del self._torpedos[hit_torpedo]
        if hit_asteroid is not None:
            del self.__asteroids[hit_asteroid]


    def run(self):
        """
        The following run's the do loop,
        and calls screen's start screen
        :return: None
        """
        self._do_loop()
        self.__screen.start_screen()
    def _do_loop(self):
        """
        The following runs the game loop,
        update's screen, and runs the timer.
        :return: None
        """
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)
    def random_point(self):
        """
        The following generates random point in
        the game's screen
        :return: New random point
        """
        return Point(random.randint(self.__screen_min_y,self.__screen_max_y),
                     random.randint(self.__screen_min_x,self.__screen_max_x))

    def update_torpedos(self):
        """
        The following takes care of
        removing torpedos which their "life" was over,
        when "life" is the amount of times that they had been
        drawn on the screen - in our case it's 200
        :return: None
        """
        temp_torpedos=self._torpedos[:]
        for torpedo in temp_torpedos:
            if torpedo[1]== TORPEDO_LIFE_TIME:
                self._torpedos.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo[0])

    def add_torpedo(self):
        """
        The following adds a new torpedo into the game,
        in the position of the ship,
        in a constant speed - determined by the speed of
        the sheep.
        :return: None
        """
        starting_point = self._ship.get_position()
        torp_direction = self._ship.get_direction()
        torp_speed_x = self._ship.get_speed().get_x_speed() \
        + 2*math.cos(self.deg_to_radians(torp_direction))
        torp_speed_y = self._ship.get_speed().get_y_speed() \
        + 2*math.sin(self.deg_to_radians(torp_direction))
        new_torpedo = Torpedo(starting_point
        , Speed2D(torp_speed_y,torp_speed_x), torp_direction)
        self.__screen.register_torpedo(new_torpedo)
        self.__screen.draw_torpedo(new_torpedo,starting_point.get_x()
                        ,starting_point.get_y(), torp_direction)
        self._torpedos.append([new_torpedo,0])


    def _game_loop(self):
        """
        The following is the main loop of the game,
        in here we determine all relevant keyboard and turn on their reaction
        if needed, in addition, we move each and every sprite , in order to draw
        it in it's new location,
        in addition, we update torpedos list - case their life time has been over,
        in addition, we call astroid_intersectoin,
        which is checking itersections of the astroids with all the relevant objects,
        and treat it accordingly.
        :return:
        """
        self.check_if_ended()
        self.__screen.draw_ship(self._ship.get_position().get_x(),
             self._ship.get_position().get_y(),self._ship.get_direction())
        self.move_sprite(self._ship)
        for torpedo_lst in self._torpedos:
            torpedo=torpedo_lst[0]
            self.move_sprite(torpedo)
            self.__screen.draw_torpedo(torpedo
             ,torpedo.get_position().get_x()
        ,torpedo.get_position().get_y(),torpedo.get_direction())
            torpedo_lst[1]+=1
        for astroid in self.__asteroids:
            self.move_sprite(astroid)
            self.__screen.draw_asteroid(
        astroid,astroid.get_position().get_x(),astroid.get_position().get_y())
        if (self.__screen.is_left_pressed()):
            self._ship.change_direction(MOVE_LEFT)
        elif(self.__screen.is_right_pressed()):
            self._ship.change_direction(MOVE_RIGHT)
        elif(self.__screen.is_up_pressed()):
            self.accelerate_ship(self._ship)
        elif(self.__screen.is_space_pressed()):
            if len(self._torpedos)<10:
                self.add_torpedo()
        self.astroid_intersection()
        self.update_torpedos()

    def check_if_ended(self):
        """
        The following check whether the player
        1.  lost. - No more life
        2. won - No more astroids
        3. wants to quit - he pressed on "q"
        and acts accordingly.
        4. the player pressed on 't' -
        if that's the case, we should "teleport" the ship.
        :return: None
        """
        ##no more astroids
        if len(self.__asteroids) == 0:
            self.__screen.show_message\
        ('You won', 'You took all the astroid down! well done foke')
            self.__screen.end_game()
            sys.exit(1)
        #no more life, quit
        if self._ship.get_life() ==0:
            self.__screen.show_message\
        ('Game ended', 'You Lost! You have no life')
            self.__screen.end_game()
            sys.exit(1)
        # the player pressed "q"
        if self.__screen.should_end():
            self.__screen.show_message('Good question', 'Are you sure?')
            self.__screen.end_game()
            sys.exit(1)
        # The player pressed "t"
        if self.__screen.is_teleport_pressed():
            for astroid in self.__asteroids:
                new_location=self.random_point()
                self._ship.set_position(new_location)
                while(astroid.has_intersection(self._ship)):
                    new_location=self.random_point()
                    self._ship.set_position(new_location)


    def divide_asteroid(self,asteroid,torpedo):
        """
        The following is responsible for dividing an astroid
        into 2 astroid, it Generates 2 new astroid in a
        special speed, in addition, if it was called with
        astroid with size 1 - it's returning,
        nothing to divide.
        :param asteroid: a given astroid
        :param torpedo: The torpedo that hitted the astroid
        :return: None
        """
        if asteroid.get_size()==1:
            return
        new_x=asteroid.get_position().get_x()
        new_size=asteroid.get_size()-1
        new_y=asteroid.get_position().get_y()
        divide_factor=math.sqrt(asteroid.get_speed().get_x_speed()**2+
                                asteroid.get_speed().get_y_speed()**2)
        new_speed_x=(torpedo.get_speed().get_x_speed()
                    +asteroid.get_speed().get_x_speed())/divide_factor
        new_speed_y=(torpedo.get_speed().get_y_speed()
                     +asteroid.get_speed().get_y_speed())/divide_factor
        asteroid_one=Asteroid(asteroid.get_position()
                              ,Speed2D(new_speed_y,new_speed_x),new_size)
        asteroid_two=Asteroid(asteroid.get_position()
                 ,Speed2D(-1*new_speed_y,-1*new_speed_x),new_size)
        self.__screen.register_asteroid(asteroid_one,new_size)
        self.__screen.register_asteroid(asteroid_two,new_size)
        self.__asteroids.append(asteroid_one)
        self.__asteroids.append(asteroid_two)

    def move_sprite(self, sprite):
        """
        The following takes a sprite - e.g an object which can be drawn,
        and move's it according to it's speed - ship, astroid,
         torpedo and etc.
        :param sprite: An object that has a speed and can change it's position
        :return: None
        """
        delta_y=self.__screen_max_y-self.__screen_min_y
        delta_x=self.__screen_max_x-self.__screen_min_x
        new_y_cor=(sprite.get_speed().get_y_speed()
        +sprite.get_position().get_y()
        -self.__screen_min_y)%delta_y+self.__screen_min_y
        new_x_cor=(sprite.get_speed().get_x_speed()
                       +sprite.get_position().get_x()
        -self.__screen_min_x)%delta_x+self.__screen_min_x
        sprite.set_position(Point(new_y_cor,new_x_cor))

def main(amount):
    """
    The following takes amount of astroid,
    creates a game runner, and runs the game
    :param amount: Amounnt of astroids
    :return: None
    """
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    # in case we got ASTROID_AMOUNT param
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
