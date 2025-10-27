class Animals:
    def __init__(self,color,size):
       self.color = color
       self.size = size

dianasor_obj=Animals('gray','very big')
mouse_obj=Animals('black','small')


print(f'dog color: {dianasor_obj.color}, size: {dianasor_obj.size}')
print(f'dog color: {mouse_obj.color}, size: {mouse_obj.size}')