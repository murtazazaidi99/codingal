class CAR:
    def __init__(model,color,name,brand):
        self.model=model
        self.color=color
        self.name=name
        self.brand=brand

landcruser_obj= CAR('2025','black','landcruser','toyota')
crown_obj= CAR('2000','gray','crown','crown')
civic_obj= CAR('2024','white','civic','honda')

print(f'landcruser model: {landcruser_obj.model}, color: {landcruser_obj.color},name: {landcruser_obj.size}brand: {landcruser_obj.size}')
print(f'crown model: {crown_obj.model}, color: {crown_obj.color},name: {crown_obj.size}brand: {crown_obj.size}')
print(f'civic model: {civic_obj.model}, color: {civic_obj.color},name: {civic_obj.size}brand: {civic_obj.size}')
