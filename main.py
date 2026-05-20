import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load("BG.png").convert()
bg_width = bg.get_width()
pygame.display.set_caption("Running Girl")
clock = pygame.time.Clock()

#MainGameLoop, using for:

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False







#Load all 20 running frames automatically
running_frames = [pygame.image.load(f"Run/Run({i}).png").convert_alpha() for i in range(1,21)]

#Animation state variables
current_frame = 0
animation_speed = 0.2  # Control how fast the frames change (lower = slower)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame += animation_speed
    if current_frame >= len(running_frames):
        current_frame = 0
        active_image = running_frames[int(current_frame)]
        screen.blit(active_image, (100, 400))

        clock.tick(60)  

# Load all 30 jumping frames automatically
jumping_frames = [pygame.image.load(f"Jump/Jump({i}).png").convert_alpha() for i in range(1,31)]

#Animation state variables
current_frame = 0
animation_speed = 0.2  # Control how fast the frames change (lower = slower)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame += animation_speed
    if current_frame >= len(running_frames):
        current_frame = 0
        active_image = running_frames[int(current_frame)]
        screen.blit(active_image, (100, 400))

        clock.tick(60) 

# Load all 16 idle frames automatically
Idle_frames = [pygame.image.load(f"Idle/Idle({i}).png").convert_alpha() for i in range (1,17)]

#Animation state variables
current_frame = 0
animation_speed = 0.2  # Control how fast the frames change (lower = slower)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame += animation_speed
    if current_frame >= len(running_frames):
        current_frame = 0
        active_image = running_frames[int(current_frame)]
        screen.blit(active_image, (100, 400))

        clock.tick(60) 

#Load all 30 dead frames automatically. Note the amount of picture sprites here.
Dead_frames = [pygame.image.load(f"Dead/Dead({i}).png").convert_alpha() for i in range (3,31)]

#Animation state variables
current_frame = 0
animation_speed = 0.2  # Control how fast the frames change (lower = slower)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame += animation_speed
    if current_frame >= len(running_frames):
        current_frame = 0
        active_image = running_frames[int(current_frame)]
        screen.blit(active_image, (100, 400))

        clock.tick(60) 

#Load all 20 walk frames automatically. Note the amount of picture sprites here.
Walk_frames = [pygame.image.load]

#Animation state variables
current_frame = 0
animation_speed = 0.2  # Control how fast the frames change (lower = slower)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_frame += animation_speed
    if current_frame >= len(running_frames):
        current_frame = 0
        active_image = running_frames[int(current_frame)]
        screen.blit(active_image, (100, 400))

        clock.tick(60) 


# Player setup
player_x = 100
player_y = 400
player_width = 20
player_height = 20
is_jumping = False
jump_velocity = 0
gravity = 0.5

# Animation
frame_index = 0
frame_counter = 0

# Obstacles
obstacles = []
obstacle_spawn_timer = 0

# Game state
running = True
game_over = False

# Main game loop
while running:
    clock.tick(60)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping and not game_over:
                is_jumping = True
                jump_velocity = -15
    
    # Spawn obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 60:
        obstacles.append(pygame.Rect(800, 450, 40, 40))
        obstacle_spawn_timer = 0
    
    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= 7
    
    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs.x > 0]
    
    # Jump physics
    if is_jumping:
        jump_velocity += gravity
        player_y += jump_velocity
        
        if player_y >= 400:
            player_y = 400
            is_jumping = False
    
    # Animation frame cycling
    frame_counter += 1
    if frame_counter >= 5:
        frame_index = (frame_index + 1) % len(running_frames)
        frame_counter = 0
    
    # Draw background
    screen.blit(background, (0, 0))
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
    
    # Draw player
    if game_over:
        current_frame = Dead_frames[frame_index % len(Dead_frames)]
    elif is_jumping:
        current_frame = jumping_frames[frame_index % len(jumping_frames)]
    else:
        current_frame = running_frames[frame_index]
    
    screen.blit(current_frame, (player_x, player_y))
    
    pygame.display.update()

pygame.quit()
