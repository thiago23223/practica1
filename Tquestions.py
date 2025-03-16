import random
import sys
# Preguntas para el juego
questions = [
        "¿Qué función se usa para obtener la longitud de una cadena en Python?",
        "¿Cuál de las siguientes opciones es un número entero en Python?",
        "¿Cómo se solicita entrada del usuario en Python?",
        "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
        "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
        ("size()", "len()", "length()", "count()"),
        ("3.14", "'42'", "10", "True"),
        ("input()", "scan()", "read()", "ask()"),
        (
            "// Esto es un comentario",
            "/* Esto es un comentario */",
            "-- Esto es un comentario",
            "# Esto es un comentario",
        ),
        ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
puntaje = 0
for _ in range(3):
        # Se selecciona una pregunta aleatoria
        question_index = random.randint(0, len(questions) - 1)
        # Se muestra la pregunta y las respuestas posibles
        print(questions[question_index])
        for i, answer in enumerate(answers[question_index]):
                print(f"{i + 1}. {answer}")
        # El usuario tiene 2 intentos para responder correctamente
        for intento in range(2):
                user_answer = input("Respuesta: ")
                if user_answer.isnumeric() and int(user_answer)-1 <= 4 and int(user_answer)-1 >= 0: #verifico si el valor ingresado es un entero y si esta en el rango de respuestas adecuado
                # Se verifica si la respuesta es correcta
                                user_answer = int(user_answer) - 1 #convierto el numero ingresado a integer
                                if user_answer == correct_answers_index[question_index]:
                                        print("¡Correcto!")
                                        puntaje = puntaje + 1
                                        break
                                else:
                                # Si el usuario no responde correctamente después de 2 intentos,
                                # se muestra la respuesta correcta
                                        print("Incorrecto. La respuesta correcta es:")
                                        print(answers[question_index][correct_answers_index[question_index]])
                                        puntaje = puntaje - 0.5
                else:
                                print("Respuesta no valida")
                                sys.exit(1) #finaliza el programa       
        # Se imprime un blanco al final de la pregunta
        print()
print(f"su puntaje final es :{puntaje}")
