import pygame

SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
RTRIANGLE = 'RTRIANGLE'
ETRIANGLE = 'ETRIANGLE'
RHOMBUS = 'RHOMBUS'
ERASER = 'ERASER'

dis_width = 640
dis_height = 480
main_screen_size = (dis_width, dis_height)
elements_to_draw = []

#bars
icon_top_bar_height = 50
icon_top_bar_width = 50
#rectangle
icon_rectangle_start_x = 0
icon_rectangle_end_x = 50
#circle
icon_circle_start_x = 50
icon_circle_end_x = 100
#rtriangle
icon_rtriangle_start_x = 100
icon_rtriangle_end_x = 150
#etrinagle
icon_etriangle_start_x = 150
icon_etriangle_end_x = 200
#rhombus
icon_rhombus_start_x = 200
icon_rhombus_end_x = 250
#eraser
icon_eraser_start_x = 250
icon_eraser_end_x = 300

#colors
#red
icon_red_color_start_y = 50
icon_red_color_end_y = 100
#blue
icon_blue_color_start_y = 100
icon_blue_color_end_y = 150
#icons
icon_color_shape_width = 40
icon_color_shape_height = 30

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)


def draw_all_shapes(screen):
  for element in elements_to_draw:
    if element['shape'] == SQUARE:
      pygame.draw.rect(screen, element['color'],[element['x'], element['y'], 50, 50])
    elif element['shape'] == CIRCLE:
      pygame.draw.circle(screen, element['color'],(element['x'], element['y']), element['radius'])
    elif element['shape'] == RTRIANGLE:
      pygame.draw.polygon(screen, element['color'],(element['x'], element['y'], element['z']))
    elif element['shape'] == ETRIANGLE:
      pygame.draw.polygon(screen, element['color'],(element['x'], element['y'], element['z']))
    elif element['shape'] == RHOMBUS:
      pygame.draw.polygon(screen, element['color'],(element['x'], element['y'], element['z'], element ['t']))
    elif element['shape'] == ERASER:
     pygame.draw.rect(screen, white,[element['x'], element['y'], 50, 50])



def add_element_rectangle(x, y, color):
  elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})


def add_element_circle(x, y, color, radius):
  elements_to_draw.append({
      'shape': CIRCLE,
      'x': x,
      'y': y,
      'color': color,
      'radius': radius
  })


def add_element_rtriangle(x, y, color):
  elements_to_draw.append({
      'shape': RTRIANGLE,
      'x': (x,y + 50),
      'y': (x + 50 ,y + 50),
      'z': (x, y),
      'color': color
  })

def add_element_etriangle(x, y, color):
  elements_to_draw.append({
      'shape': ETRIANGLE,
      'x': (x,y),
      'y': (x + 50 ,y + 50),
      'z': (x - 50, y + 50),
      'color': color
  })

def add_element_rhombus(x, y, color):
  elements_to_draw.append({
      'shape': RHOMBUS,
      'x': (x,y),
      'y': (x + 50, y + 25),
      'z': (x, y + 50),
      't': (x - 50, y + 25),
      'color': color
  })

def add_element_erase(x, y):
  elements_to_draw.append({'shape': ERASER, 'x': x, 'y': y})


def draw_main_icons(screen):
  # tabs
  pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, 40))
  pygame.draw.rect(screen, right_tab_color, (dis_width - 80, 0, 80, dis_height))
  #rectangle
  pygame.draw.rect(screen, white, (icon_rectangle_start_x + 5, 5, 40, 30))
  pygame.draw.rect(screen, purple, (icon_rectangle_start_x + 10, 10, 30, 20))
  #circle
  pygame.draw.rect(screen, white, (icon_circle_start_x + 5, 5, 40, 30))
  pygame.draw.circle(screen, purple, (icon_circle_start_x + 25, 20), 10)
  #rtriangle
  pygame.draw.rect(screen, white, (icon_rtriangle_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, purple, ((icon_rtriangle_start_x + 5, 35), (icon_rtriangle_end_x - 5, 35), (icon_rtriangle_start_x + 5, 5)))
  #etriangle
  pygame.draw.rect(screen, white, (icon_etriangle_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, purple, ((icon_etriangle_start_x + 5, 35), (icon_etriangle_end_x - 5, 35), (icon_etriangle_start_x + 25, 5)))
  #rhombus
  pygame.draw.rect(screen, white, (icon_rhombus_start_x + 5, 5, 40, 30))
  pygame.draw.polygon(screen, purple, ((icon_rhombus_start_x + 25, 5), (icon_rhombus_start_x + 5, 20), (icon_rhombus_start_x + 25, 35), (icon_rhombus_end_x -  5, 20)))
  #eraser
  pygame.draw.rect(screen, white, (icon_eraser_start_x + 5, 5, 40, 30))

  # colors
  pygame.draw.rect(screen, red,(dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
  pygame.draw.rect(screen, blue,(dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))


def main():
  pygame.init()
  screen = pygame.display.set_mode(main_screen_size)
  clock = pygame.time.Clock()

  x = 0
  y = 0
  mode = 'blue'
  points = []
  is_rectangle_drawer = False
  is_circle_drawer = False
  is_rtriangle_drawer = False
  is_etriangle_drawer = False
  is_rhombus_drawer = False
  is_eraser = False

  color = black

  position = (0, 0)

  while True:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w and ctrl_held:
          return
        if event.key == pygame.K_F4 and alt_held:
          return
        if event.key == pygame.K_ESCAPE:
          return

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if position[0] <= icon_rectangle_end_x and position[0] > 0 and position[1] < icon_top_bar_height:
            is_rectangle_drawer = not is_rectangle_drawer
            is_circle_drawer = False
            is_rtriangle_drawer = False
            is_etriangle_drawer = False
            is_rhombus_drawer = False
            is_eraser = False
            print('is_rectangle_drawer = True')
          elif position[0] <= icon_circle_end_x and position[0] > icon_circle_start_x and position[1] < icon_top_bar_height:
            is_circle_drawer = not is_circle_drawer
            is_rectangle_drawer = False
            is_rtriangle_drawer = False
            is_etriangle_drawer = False
            is_rhombus_drawer = False
            is_eraser = False
            print('is_circle_drawer = True')
          elif position[0] <= icon_rtriangle_end_x and position[0] > icon_rtriangle_start_x and position[1] < icon_top_bar_height:
            is_rtriangle_drawer = not is_rtriangle_drawer
            is_rectangle_drawer = False
            is_circle_drawer = False
            is_etriangle_drawer = False
            is_rhombus_drawer = False
            is_eraser = False
            print('is_rtriangle_drawer = True')
          elif position[0] <= icon_etriangle_end_x and position[0] > icon_etriangle_start_x and position[1] < icon_top_bar_height:
            is_etriangle_drawer = not is_etriangle_drawer
            is_rectangle_drawer = False
            is_circle_drawer = False
            is_rtriangle_drawer = False
            is_rhombus_drawer = False
            is_eraser = False
            print('is_etriangle_drawer = True')
          elif position[0] <= icon_rhombus_end_x and position[0] > icon_rhombus_start_x and position[1] < icon_top_bar_height:
            is_rhombus_drawer = not is_rhombus_drawer
            is_rectangle_drawer = False
            is_rtriangle_drawer = False
            is_etriangle_drawer = False
            is_circle_drawer = False
            is_eraser = False
            print('is_rhombus_drawer = True')
          elif position[0] <= icon_eraser_end_x and position[0] > icon_eraser_start_x and position[1] < icon_top_bar_height:
            is_eraser = not is_eraser
            is_rectangle_drawer = False
            is_rtriangle_drawer = False
            is_etriangle_drawer = False
            is_circle_drawer = False
            is_rhombus_drawer = False
            print('is_eraser = True')
          elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_red_color_start_y and position[1] < icon_red_color_end_y:
            color = red
            print('color = red')
          elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_blue_color_start_y and position[1] < icon_blue_color_end_y:
            color = blue
            print('color = blue')
          elif is_rectangle_drawer:
            add_element_rectangle(position[0], position[1], color)
          elif is_circle_drawer:
            add_element_circle(position[0], position[1], color, 20)
          elif is_rtriangle_drawer:
            add_element_rtriangle(position[0], position[1], color)
          elif is_etriangle_drawer:
            add_element_etriangle(position[0], position[1], color)
          elif is_rhombus_drawer:
            add_element_rhombus(position[0], position[1], color)
          elif is_eraser:
            add_element_erase(position[0], position[1])

      if event.type == pygame.MOUSEMOTION:
        position = event.pos
        print(position)
        

    screen.fill((255, 255, 255))

    draw_all_shapes(screen)
    draw_main_icons(screen)

    pygame.display.flip()

    clock.tick(60)

main()