from ClassHighRise import *
import random
import time


class App:
    @staticmethod
    def designer(my_class, height: list, width: list) -> \
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

    @staticmethod
    def run():
        Build.global_night(night=True)  # регулировка ночи
        for home in range(0, 100):  # количество рандомных домов
            my_random = random.randint(0, 2)
            print(f'сгенерированное здание {home + 1}', end=(' - \n' if (1 + home) % 5 == 0 else ' - '))
            if my_random == 0:
                App.designer(BuildResidentialBuilding, [9, 19, 2], [9, 19, 2])
            elif my_random == 1:
                App.designer(BuildingShop, [9, 19, 2], [9, 19, 2])  # регулировка высоты и ширины оффиса
            elif my_random == 2:
                App.designer(BuildingFabrik, [3, 6, 2], [9, 19, 2])  # регулировка высоты и ширины фабрики

        BildVoids.bild_voids()  # создание правого пустого края
        BildGrass.bild_grass()  # создание травки

        print("\n \n --- %s секунд ---" % (time.time() - start_time))
        print(f"--- {(time.time() - start_time) / home} на здание ---")

        PrintFront.print_front()  # визуализация


if __name__ == '__main__':
    start_time = time.time()
    App.run()
