from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

app = Ursina()
from UI import *

move = False
window.show_ursina_splash = True
window.borderless = False
window.exit_button.enabled = False
change_position = (False,None)
selected = None
ogColor = None
movepoint = Vec3(0,0,0)
og_handler_position = Vec3(0,0,0)
        
def input(key):
    global selected,ogColor,move,change_position,og_handler_position,movepoint
    #selection
    if key == Keys.left_mouse_down:
        for entity in entityGroup:
            if entity.ID == 'Active':
                if entity == mouse.hovered_entity:
                    if not selected:
                        selected = entity
                        ogColor = entity.color
                        entity.color = color.yellow
                        properties.show_properties(selected)
                        break
                elif mouse.hovered_entity in uiGroup:
                    break
                else:
                    if selected:
                        selected.color=ogColor
                        properties.hide_properties()
                        selected = None
                        break
    #moving
    if key == Keys.left_mouse_down and change_position[0] == False:
        if mouse.hovered_entity == move_tool.x:
            change_position = (True,'x')
            og_handler_position = move_tool.handler.position
        if mouse.hovered_entity == move_tool.y:
            change_position = (True,'y')
            og_handler_position = move_tool.handler.position
        if mouse.hovered_entity == move_tool.z:
            change_position = (True,'z')
            og_handler_position = move_tool.handler.position
        movepoint = move_tool.handler.position
    elif key == Keys.left_mouse_down and change_position[0] == True:
        change_position = (False,None)
        movepoint = Vec3(0,0,0)
    if key == Keys.right_mouse_down and change_position[0] == True:
        change_position = (False,None)
        move_tool.handler.position = og_handler_position
        movepoint = Vec3(0,0,0)
    if key == 'm':
        if selected:
            if move == True:
                move = False
                move_tool.handler.parent = None
                change_position = (False,None)
                move_tool.handler.enabled = False
            else:
                move_tool.handler.parent = selected
                move = True
                move_tool.handler.enabled = True

def update():
    global movepoint
    properties.update()
    if selected:
        if change_position[0]:
            print(movepoint)
            if change_position[1] == 'x':
                selected.x = movepoint.x + mouse.x*10 
            if change_position[1] == 'y':
                selected.y = movepoint.y + mouse.x*10
            if change_position[1] == 'z':
                selected.z = movepoint.z + mouse.x*10 

EditorCamera()
app.run()
