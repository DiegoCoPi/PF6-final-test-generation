import json
import requests

# Fetch dish by number from API
def dish_fetch(num):
    URL = "https://api-colombia.com/api/v1/TypicalDish"
    response = requests.get(URL)
    dishes = json.loads(response.content)

    # Find dish with matching id
    for dish in dishes:
        if dish.get('id') == num:
            return {
                "id": dish.get('id'),
                "name": dish.get('name'),
                "description": dish.get('description'),
                "region": dish.get('region')
            }
    return {}

def main():
    print("Estudiantes, ¡bienvenidos a Colombia!")
    print("Escojan el plato típico que deseen.\n")

    try:
        num = int(input("Ingrese el número del plato: "))
        info = dish_fetch(num)
        if info:
            print("\nInformación del plato:")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Plato no encontrado.")
    except ValueError:
        print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
