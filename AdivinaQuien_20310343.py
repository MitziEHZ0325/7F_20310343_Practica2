# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:50:02 2023

@author: Home
"""
class Actress:
    def __init__(self, name, hair_color, eye_color, has_children, nationality, is_married, age, has_marvel_dc_movie, has_oscar):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.has_children = has_children
        self.nationality = nationality
        self.is_married = is_married
        self.age = age
        self.has_marvel_dc_movie = has_marvel_dc_movie
        self.has_oscar = has_oscar

def load_actresses(filename):
    actresses = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 9:  # Actualiza el número de atributos
                    name, hair_color, eye_color, has_children, nationality, is_married, age, has_marvel_dc_movie, has_oscar = data
                    actresses.append(Actress(name.strip(), hair_color.strip(), eye_color.strip(), has_children.strip(), nationality.strip(), is_married.strip(), age.strip(), has_marvel_dc_movie.strip(), has_oscar.strip()))
    except FileNotFoundError:
        pass
    return actresses

def save_actresses(filename, actresses):
    with open(filename, 'w') as file:
        for actress in actresses:
            file.write(f"{actress.name},{actress.hair_color},{actress.eye_color},{actress.has_children},{actress.nationality},{actress.is_married},{actress.age},{actress.has_marvel_dc_movie},{actress.has_oscar}\n")

def guess_actress(user_input, actresses):
    for actress in actresses:
        if (
            (actress.hair_color == user_input["hair_color"] or user_input["hair_color"] == "Cualquier") and
            (actress.eye_color == user_input["eye_color"] or user_input["eye_color"] == "Cualquier") and
            (actress.has_children == user_input["has_children"] or user_input["has_children"] == "Cualquier") and
            (actress.nationality == user_input["nationality"] or user_input["nationality"] == "Cualquier") and
            (actress.is_married == user_input["is_married"] or user_input["is_married"] == "Cualquier") and
            (user_input["age"] == "No" or (user_input["age"] == "Si" and int(actress.age) > 35)) and
            (user_input["has_marvel_dc_movie"] == "No" or (user_input["has_marvel_dc_movie"] == "Si" and actress.has_marvel_dc_movie == "Si")) and
            (actress.has_oscar == user_input["has_oscar"])
        ):
            return actress
    return None

def main():
    actresses = load_actresses('actresses.txt')

    print("Bienvenido al juego Adivina la Actriz - Actrices de Hollywood")
    play_again = True

    while play_again:
        print("Piensa en una actriz y responde las siguientes preguntas.")
        
        hair_color = input("¿Cuál es el color de cabello de la actriz? (Rubio/Castaño/Pelirrojo/Cualquier): ").strip()
        eye_color = input("¿Cuál es el color de ojos de la actriz? (Azules/Marrones/Verdes/Cualquier): ").strip()
        has_children = input("¿Tiene la actriz hijos? (Si/No/Cualquier): ").strip()
        nationality = input("¿Cuál es la nacionalidad de la actriz? (Estadounidense/Australiana/Cualquier): ").strip()
        is_married = input("¿Está casada actualmente? (Si/No/Cualquier): ").strip()
        age = input("¿Tiene la actriz más de 35 años? (Si/No): ").strip()
        has_marvel_dc_movie = input("¿Ha estado la actriz en alguna película de Marvel o DC? (Si/No): ").strip()
        has_oscar = input("¿Tu actriz ha ganado un Oscar? (Si/No): ").strip()

        user_input = {
            "hair_color": hair_color,
            "eye_color": eye_color,
            "has_children": has_children,
            "nationality": nationality,
            "is_married": is_married,
            "age": age,
            "has_marvel_dc_movie": has_marvel_dc_movie,
            "has_oscar": has_oscar,
        }

        guessed_actress = guess_actress(user_input, actresses)

        if guessed_actress:
            print(f"¡Adiviné! La actriz que pensaste es {guessed_actress.name}.")
        else:
            print("No pude adivinarla.")
            new_name = input("Por favor, ingresa el nombre de la actriz que pensaste: ")
            new_hair_color = input("¿Cuál es el color de cabello de la actriz? (Rubio/Castaño/Pelirrojo/Cualquier): ")
            new_eye_color = input("¿Cuál es el color de ojos de la actriz? (Azules/Marrones/Verdes/Cualquier): ")
            new_has_children = input("¿Tiene la actriz hijos? (Si/No): ")
            new_nationality = input("¿Cuál es la nacionalidad de la actriz? (Estadounidense/Australiana7Cualquiera): ").strip()
            new_is_married = input("¿Está casada actualmente? (Si/No): ")
            new_age = input("¿Tiene la actriz más de 35 años? (Si/No): ").strip()
            new_has_marvel_dc_movie = input("¿Ha estado la actriz en alguna película de Marvel o DC? (Si/No): ").strip()
            new_has_oscar = input("¿Tu actriz ha ganado un Oscar? (Si/No): ").strip()
            new_actress = Actress(new_name, new_hair_color, new_eye_color, new_has_children, new_nationality, new_is_married, new_age, new_has_marvel_dc_movie, new_has_oscar)
            actresses.append(new_actress)
            save_actresses('actresses.txt', actresses)
            print(f"Nueva actriz agregada: {new_name}")

        play_again_input = input("¿Deseas jugar de nuevo? (Si/No): ").strip().lower()
        play_again = play_again_input == 'si' or play_again_input == 'si'

if __name__ == "__main__":
    main()
