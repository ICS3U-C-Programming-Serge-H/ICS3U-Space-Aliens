#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program is the Space Aliens program in python
import stage
import ugame


def game_scene():
    # this function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # sets the backround to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    background = stage.Grid(image_bank_background, 10, 8)
    # sets the backround to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    # Sets the 77 tiles to the right and 66 tiles down.

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [ship] + [background]
    # render the backround and initial location of sprite list
    # most likely you will only render backround once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)

       
        # update game logic
       
        # redraw Sprites
        game.render_sprites([ship])
        # makes sure the ship is always on screen
        game.tick()
        # This makes sure the ship renders at 60 Hz per frames


if __name__ == "__main__":
    game_scene()
