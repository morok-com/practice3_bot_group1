# # напишите здесь функцию print_shopping_list(),
# # подобрав уникальные названия продуктов и сложив значения
# def print_shopping_list(pizza, salad):
#     key_pizza = set(pizza)
#     key_salad = set(salad)
#     union_key = key_pizza.union(key_salad)
#     #print(union_key)
#     count = 0
#
#     for pozition in union_key:
#         for pozition_pizza, name_pizza in pizza.items():
#             for pozition_salad, name_salad in salad.items():
#                 if pozition_pizza == pozition_salad == pozition:
#                     count = name_pizza + name_salad
#                     print(pozition, count)
#
#                 # else:
#                 #     print(pozition_pizza, name_pizza)
#                 #     #print(pozition_salad, name_salad)
#
#
#
#         # for pozition_salad, name_salad in salad.items():
#         #     if pozition_salad == pozition:
#         #         count += name_salad
#         #         print(pozition, name_salad)
#
#         # def is_anyone_in(collection, city):
#         #     if city in collection.values():  # если есть среди значений словаря collection
#         #         print(city)
#         #         for key, name in collection.items():  # переберите все ключи словаря
#         #             if name == city:  # если соответствующее ключу значение равно city
#         #                 print('В городе ' + city + ' живёт ' + key + '.')
#         #     else:
#         #         print('Пока никого.')
#
# # print(pizza.intersection(salad))
#
# pizza = {'мука, кг': 1,
#          'помидоры, кг': 1.5,
#          'шампиньоны, кг': 1.5,
#          'сыр, кг': 0.8,
#          'оливковое масло, л': 0.1,
#          'дрожжи, г': 50}
# salad = {'огурцы, кг': 1,
#          'перцы, кг': 1,
#          'помидоры, кг': 1.5,
#          'оливковое масло, л': 0.1,
#          'листья салата, кг': 0.4}
#
# print_shopping_list(pizza, salad)


# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения
def print_shopping_list(pizza, salad):

    sort_food = set(pizza)
    sort_food = sort_food.union(salad)

    for food in sort_food:
        weight = 0
        if food in pizza.keys():
            weight += pizza[food]
        if food in salad.keys():
            weight += salad[food]
        print(food,': ', weight, sep='')

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)