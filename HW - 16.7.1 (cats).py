class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")
        
#         2 часть

from cat import Cat

cats = [
    {
     "name": "Сэм",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Мурка",
     "gender": "девочка",
     "age": 1,
    },
{
     "name": "Пушок",
     "gender": "мальчик",
     "age": 3,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)
