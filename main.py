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
    print("Hello, students!")
    print("Fetching Colombian typical dishes...")

    try:
        num = int(input("Enter the dish ID number: "))
        info = dish_fetch(num)
        if info:
            print("Dish Information:")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Dish not found.")
    except ValueError:
        print("Please enter a valid number.")
    print("Hello, students!")
    print("Fetching Colombian typical dishes...")

    try:
        num = int(input("Enter the dish ID number: "))
        info = dish_fetch(num)
        if info:
            print("Dish Information:")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Dish not found.")
    except ValueError:
        print("Please enter a valid number.")

def main():
  print("Hello learners!")

if __name__=="__main__":
  main()