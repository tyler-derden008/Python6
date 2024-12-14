#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    routes = []
    n = int(input("Введите количество маршрутов: "))
    for i in range(n):
        start_point = input(f"Введите название начального пункта маршрута {i+1}: ")
        end_point = input(f"Введите название конечного пункта маршрута {i+1}: ")
        route_number = int(input(f"Введите номер маршрута {i+1}: "))
        route = {
            "start_point": start_point,
            "end_point": end_point,
            "route_number": route_number
        }
        routes.append(route)
    routes.sort(key=lambda x: x["route_number"])
    search_point = input("Введите название пункта для поиска маршрутов: ")
    found_routes = [route for route in routes if route["start_point"] == search_point or route["end_point"] == search_point]
    if found_routes:
        print("Найденные маршруты:")
        for route in found_routes:
            print(f"Маршрут №{route['route_number']}: {route['start_point']} -> {route['end_point']}")
    else:
        print("Маршруты с указанным пунктом не найдены.")
if __name__ == "__main__":
    main()
