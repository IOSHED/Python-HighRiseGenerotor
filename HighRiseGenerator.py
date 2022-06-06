from ClassHighRise import BuildResidentialBuilding, BuildingShop, BuildingFabrik,\
                           BildVoids, BildGrass, PrintFront, Build
import random


def Designer(my_class, height: list, width: list) -> \
        BuildResidentialBuilding or BuildingShop or BuildingFabrik:
    """Создание экземпляра для всех классов"""

    objects = my_class(random.randrange(height[0], height[1], height[2]),
                       random.randrange(width[0], width[1], width[2]))
    objects.math_front()
    if my_class == BuildingShop or my_class == BuildingFabrik:
        objects.math_front_gradiente()
    objects.math_windows()
    if my_class == BuildingFabrik:
        objects.math_pipes()
    objects.addendum()
    return objects


if __name__ == '__main__':
    Build.global_night(night=True)  # регулировка ночи
    max_height = 20  # регулировка максимальной высоты

    for home in range(0, 5):  # количество рандомных домов
        my_random = random.randint(0, 2)
        print(home)
        if my_random == 0:
            home = Designer(BuildResidentialBuilding, [9, 19, 2], [9, 19, 2])   # регулировка высоты и ширины дома
        elif my_random == 1:
            office = Designer(BuildingShop, [9, 19, 2], [9, 19, 2])    # регулировка высоты и ширины оффиса
        elif my_random == 2:
            fabrik = Designer(BuildingFabrik, [3, 6, 2], [9, 19, 2])    # регулировка высоты и ширины фабрики

    BildVoids.bild_voids()  # создание правого пустого края
    BildGrass.bild_grass()  # создание травки
    PrintFront.print_front()  # визуализация
