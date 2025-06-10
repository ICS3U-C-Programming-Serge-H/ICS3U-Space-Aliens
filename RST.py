#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program is the Space Aliens program in python

import stage
import ugame
import constants


def menu_scene():
    # This function is the menu scene of the game.

    # Load image bank for the background from a BMP file.
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Create a list to hold text objects.
    text = []
    # Create the first text object for the studio name.
    # Set width, height, font (None for default), palette, and buffer (None for direct drawing).
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    # Move the text to a specific coordinate on the screen.
    text1.move(20, 10)
    # Set the actual text content.
    text1.text("Gugu Game Studios")
    # Add the text object to the list.
    text.append(text1)

    # Create the second text object for the "PRESS START" message.
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # Create the background grid using the loaded image bank, with dimensions 10x8 tiles.
    background = stage.Grid(image_bank_background, 10, 8)

    # Initialize the game stage with the display and set the frame rate to 60 FPS.
    game = stage.Stage(ugame.display, 60)
    # Set the layers for rendering: text objects on top of the background.
    game.layers = text + [background]
    # Render the initial block of layers to the screen.
    game.render_block()

    # Main loop for the menu scene.
    while True:
        # Get the current state of pressed buttons.
        keys = ugame.buttons.get_pressed()

        # Check if the START button is pressed.
        if keys & ugame.K_START != 0:
            # If START is pressed, transition to the game scene.
            game_scene()

        # Tick the game clock to maintain the frame rate.
        game.tick()


def game_scene():
    # This function is the main game scene.

    # Load image banks for the background and sprites.
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Initialize button states for debouncing (tracking presses, releases).
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Prepare sound for firing.
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()  # Stop any currently playing audio.
    sound.mute(False)  # Unmute the audio.

    # Create the background grid.
    background = stage.Grid(image_bank_background, 10, 8)

    # Create the player ship sprite.
    # Image bank, frame number (5), x-coordinate (75), y-coordinate (near bottom of screen).
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # Create the alien sprite.
    # Image bank, frame number (9), x-coordinate (centered horizontally), y-coordinate (near top).
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Initialize the game stage.
    game = stage.Stage(ugame.display, 60)
    # Set the layers for rendering: background first, then alien, then ship (foreground).
    game.layers = [background] + [alien] + [ship]
    # Render the initial block of layers.
    game.render_block()

    # Main loop for the game scene.
    while True:
        # Get the current state of pressed buttons.
        keys = ugame.buttons.get_pressed()

        # Handle A button press logic for firing.
        if keys & ugame.K_O != 0:  # Check if the A button (K_O) is currently held down.
            if a_button == constants.button_state["button_up"]:
                # If button was up and is now pressed, set state to "just_pressed".
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                # If button was just pressed and is still held, set state to "still_pressed".
                a_button = constants.button_state["button_still_pressed"]
        else:
            # If the A button is not currently held down.
            if a_button == constants.button_state["button_still_pressed"]:
                # If button was still pressed and is now released, set state to "released".
                a_button = constants.button_state["button_released"]
            else:
                # Otherwise, the button is fully "up".
                a_button = constants.button_state["button_up"]

        # B, Start, Select button handling (currently placeholders).
        if keys & ugame.K_X != 0:
            pass  # No action defined for B button.
        if keys & ugame.K_START != 0:
            print("Start")  # Debugging: prints "Start" to console.
        if keys & ugame.K_SELECT != 0:
            print("Select")  # Debugging: prints "Select" to console.

        # Move ship right with boundary check.
        if keys & ugame.K_RIGHT != 0:
            # Check if the ship is within the screen bounds to move right.
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)

        # Move ship left with boundary check.
        if keys & ugame.K_LEFT != 0:
            # Check if the ship is within the screen bounds to move left.
            if ship.x > 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)

        # Placeholder for vertical controls (currently unused).
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # Play shooting sound if A button was just pressed.
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw only the sprites to update their positions efficiently.
        game.render_sprites([ship] + [alien])
        # Tick the game clock to maintain the frame rate.
        game.tick()


if __name__ == "__main__":
    # Call the menu scene to start the game when the script is executed.
    menu_scene()
