#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program is the Space Aliens program in python


import stage
import ugame
import constants


def game_scene():

    # this function is the main game game_scene



    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")



    # buttons that you wanna keep state information on

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]



    # get sound ready

    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    background = stage.Grid(image_bank_background, 10, 8)



    ship = stage.Sprite(

        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)

    )



    alien = stage.Sprite(

        image_bank_sprites, 9,

        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),

        16

    )



    game = stage.Stage(ugame.display, 60)

    game.layers = [ship] + [alien] + [background]

    game.render_block()



    # repeat forever, game loop

    while True:

        keys = ugame.buttons.get_pressed()



        # A button to fire

        if keys & ugame.K_O != 0:

            if a_button == constants.button_state["button_up"]:

                a_button = constants.button_state["button_just_pressed"]

            elif a_button == constants.button_state["button_just_pressed"]:

                a_button = constants.button_state["button_still_pressed"]

        else:

            if a_button == constants.button_state["button_still_pressed"]:

                a_button = constants.button_state["button_released"]

            else:

                a_button = constants.button_state["button_up"]



        # B button

        if keys & ugame.K_X != 0:

            pass

        if keys & ugame.K_START != 0:

            print("Start")

        if keys & ugame.K_SELECT != 0:

            print("Select")



        # Fixed LEFT/RIGHT movement (no teleporting)

        if keys & ugame.K_RIGHT != 0:

            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):

                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)



        if keys & ugame.K_LEFT != 0:

            if ship.x > 0:

                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)



        if keys & ugame.K_UP != 0:

            pass

        if keys & ugame.K_DOWN != 0:

            pass



        # update game logic

        if a_button == constants.button_state["button_just_pressed"]:

            sound.play(pew_sound)



        # redraw Sprites

        game.render_block()

        game.tick()





if __name__ == "__main__":

    game_scene()