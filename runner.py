import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('gfx/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('gfx/player/player_walk_2.png').convert_alpha()
        player_walk_3 = pygame.image.load('gfx/player/player_walk_3.png').convert_alpha()
        player_walk_4 = pygame.image.load('gfx/player/player_walk_4.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
        self.player_index = 0
        self.player_jump = pygame.image.load('gfx/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('sfx/jump.mp3')
        self.jump_sound.set_volume(0.1)

        self.mask = pygame.mask.from_surface(self.image)

        # Cooldown management
        self.last_jump_time = 0  # Time of the last jump

    def player_input(self, condition):
        current_time = pygame.time.get_ticks()  # Get the current time
        if self.rect.bottom >= 300 and (condition == 'jump') and (current_time - self.last_jump_time >= 750):
            self.gravity = -12
            self.jump_sound.play()
            self.last_jump_time = current_time  # Update the last jump time

    def apply_gravity(self):
        self.gravity += 0.4
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.15
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, condition=None):
        if condition:
            self.player_input(condition)
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('gfx/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('gfx/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('gfx/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('gfx/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, '#fefefe')
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False, pygame.sprite.collide_mask):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Gesture Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('sfx/ap_sad.xm')
bg_music.play(loops=-1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('gfx/Sky.png').convert()
ground_surface = pygame.image.load('gfx/ground.png').convert()
title_bg = pygame.image.load('gfx/title_bg.png').convert_alpha()

player_stand = pygame.image.load('gfx/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale_by(player_stand, 5)
player_stand_rect = player_stand.get_rect(midbottom=(150, 380))

title = pygame.image.load('gfx/title.png').convert_alpha()
title_rect = title.get_rect(center=(400, 100))

game_message = test_font.render('Make a closed fist with your right hand.', False, '#fefefe')
game_message_rect = game_message.get_rect(center=(400, 260))

controls_message = test_font.render('Open hand to jump. Closed fist to stay on ground.', False, '#fefefe')
controls_message_rect = controls_message.get_rect(center=(400, 360))

quit_text = test_font.render('[SPACEBAR] to run! [Q] to quit.', False, '#fefefe')
quit_rect = quit_text.get_rect(center=(400, 320))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            exit()

        if game_active and event.type == obstacle_timer:
            obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

        else:
            if not game_active:
                with open('hand_detection_result.txt', 'r') as f:
                    result = f.readline().strip()
                if result == 'jump':
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

    # Gesture detection logic
    if game_active:
        with open('hand_detection_result.txt', 'r') as f:
            result = f.readline().strip()
        if result == 'jump':
            # Now we pass the condition directly to the update method
            player.sprite.update('jump')

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        screen.blit(controls_message, controls_message_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        screen.blit(title_bg, (0, 0))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title, title_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            score_message = test_font.render(f'Your Score: {score}', False, '#fefefe')
            score_message_rect = score_message.get_rect(center=(400, 260))
            screen.blit(score_message, score_message_rect)

        screen.blit(quit_text, quit_rect)

    pygame.display.update()
    clock.tick(60)
