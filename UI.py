from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

if __name__ == "__main__":
    app = Ursina()
    EditorCamera()

grid = Entity(model=Grid(1000,1000),rotation_x=90,scale=1000,color=	rgb(220,220,220,10))
y_axis = Entity(model=Mesh(vertices=[Vec3(0,1000,0),Vec3(0,-1000,0)],mode='line',thickness=1),color=rgb(220,0,0,100))
x_axis = Entity(model=Mesh(vertices=[Vec3(1000,0,0),Vec3(-1000,0,0)],mode='line',thickness=1),color=rgb(0,220,0,100))
z_axis = Entity(model=Mesh(vertices=[Vec3(0,0,1000),Vec3(0,0,-1000)],mode='line',thickness=1),color=rgb(0,0,220,100))

uiGroup = []
entityGroup = []
showing = False

class Move:
    def __init__(self):
        visible = False
        self.handler = Entity(enabled=False)
        self.x = Entity(model='arrow',x=0.5,color=color.green,parent=self.handler,collider='box',ID="UI")
        self.y = Entity(model='arrow',y=0.5,color=color.red,rotation_z=-90,parent=self.handler,collider='box',ID="UI")
        self.z = Entity(model='arrow',z=-0.5,color=color.blue,rotation_y=90,parent=self.handler,collider='box',ID="UI")
        uiGroup.append(self.x)
        uiGroup.append(self.y)
        uiGroup.append(self.z)

class Properties:
    def __init__(self):
        self.showing = False
        self.position_ = Button(model='quad',text='position',color=color.gray,parent=properties_bar,scale=(1,0.03),y=0.475,ID='UI',name="property_scale",visible=False)
        self.position_.text_entity.position=(-0.3,-0.02)
        uiGroup.append(self.position_)
        self.selected = None
    def show_properties(self,selected):
        self.selected = selected
        self.position_.visible = True
    def hide_properties(self):
        self.selected = None
        self.position_.visible = False
    def update(self):
        if self.selected is not None:
            self.position_.text = f"Position : x:{round(self.selected.x)} y:{round(self.selected.y)} z:{round(self.selected.z)}"

def makeEntity(model,menu=None):
    entity = Entity(model=model,collider='box',ID="Active")
    entityGroup.append(entity)
    if menu != None:
        destroy(menu)

def addEntityMenu():
    pannel = WindowPanel(title='Add Object',content=(
        Button(text='cube', color=color.azure),
        Button(text='quad', color=color.azure),
        Button(text='sphere', color=color.azure)
                    ))
    for button in pannel.content:
        button.on_click = Func(makeEntity,button.text,pannel)

properties_bar = Entity(name='properties_bar',
                        model='quad',
                        parent=camera.ui,
                        scale=(0.7,1),
                        position=window.right,
                        color=color.black,
                        collider='box',
                        ID='UI')

uiGroup.append(properties_bar)

properties = Properties()

move_tool = Move()

menu = DropdownMenu('menu', buttons=(DropdownMenuButton(text='add',on_click=addEntityMenu),),ID='UI',name='menu_wiged')
uiGroup.append(menu)

if __name__ == "__main__":
    app.run()