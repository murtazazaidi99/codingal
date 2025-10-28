class Robot:
    def __init__(self,color,size,parts):
       self.color = color
       self.size = size
       self.parts= parts

karel_obj=Robot('gray','very big','six')
chidi_obj=Robot('black','small','ninteen')


print(f'karel color: {karel_obj.color}, size: {karel_obj.size}, parts:{karel_obj.parts}')
print(f'chidi color: {chidi_obj.color}, size: {chidi_obj.size},parts:{chidi_obj.parts}')
