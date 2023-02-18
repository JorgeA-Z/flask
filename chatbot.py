import re, random

class chatBot():
    def __init__(self) -> None:
        pass

    def get_respuesta(self, user_input):
        mensaje = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        respuesta = self.revisar_respuestas(mensaje)
        return respuesta

    def probabilidad_mensaje(self, mensaje, palabras_reconocidas, respuesta_simple = False, palabras_requeridas=[]):
        
        probabilidad_mensaje = 0
        tiene_palabras_requeridas = True

        for palabra in mensaje:
            if palabra in palabras_reconocidas:
                probabilidad_mensaje += 1

        porcentaje =  float(probabilidad_mensaje) / float(len(palabras_reconocidas))

        
        for palabra in palabras_requeridas:
            if palabra in mensaje:
                tiene_palabras_requeridas = True


        if tiene_palabras_requeridas or respuesta_simple:
            return int(porcentaje * 100)    
        else:
            return 0


    def revisar_respuestas(self, mensaje):
        probabilidad_mayor = {}

        def respuesta(bot_respuesta, lista_p ,respuesta_simple = False, palabras_requeridas=[]):
            nonlocal probabilidad_mayor
            probabilidad_mayor[bot_respuesta] = self.probabilidad_mensaje(mensaje, lista_p, respuesta_simple, palabras_requeridas)


        
        canto = '''
        Well here we are again
        It's always such a pleasure
        Remember when you tried
        to kill me twice?

        Oh how we laughed and laughed
        Except I wasn't laughing
        Under the circumstances
        I've been shockingly nice

        You want your freedom?
        Take it
        That's what I'm counting on
        I used to want you dead
        but
        Now I only want you gone

        She was a lot like you
        (Maybe not quite as heavy)
        Now little Caroline is in here too

        One day they woke me up
        So I could live forever
        It's such a shame the same
        will never happen to you

        Severance Package Details:

        You've got your
        short sad
        life left
        That's what I'm counting on
        I'll let you get right to it
        Now I only want you gone

        Goodbye my only friend
        Oh, did you think I meant you?
        That would be funny
        if it weren't so sad

        Well you have been replaced
        I don't need anyone now
        When I delete you maybe
        [REDACTED]

        Go make some new disaster
        That's what I'm counting on
        You're someone else's problem
        Now I only want you gone
        Now I only want you gone
        Now I only want you
        gone.'''

        respuesta('Hola', ['hola','saludos', 'buenas'], respuesta_simple = True)
        
        respuesta('General Kenobi', ['hello', 'there', 'Hello', 'There'], respuesta_simple = False ,palabras_requeridas=['hello', 'there', 'Hello', 'There'])

        respuesta('Chat bot de Angelo', ['como', 'llamas', 'cual', 'nombre', 'Como', 'Cual'], respuesta_simple = False ,palabras_requeridas=['Como', 'como', 'cual', 'Cual'])

        respuesta('Un Chat bot básico programado por Angel, puedo responder a unas cuantas preguntas aunque no muchas, mi programador es un perezoso. Va por la sexta temporada de una caricatura china sobre superheroes.', ['que', 'eres'], respuesta_simple = False ,palabras_requeridas=['eres', 'Eres', 'que', 'Que'])


        respuesta('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes', 'Como'], respuesta_simple = False ,palabras_requeridas=['Como', 'como'])

        respuesta('Excelente', ['bien', 'Bien'], respuesta_simple = True)

        respuesta('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], respuesta_simple=True)

        respuesta('Muy poco, solo puedo contestar a unos pocos mensajes', ['que', 'haces', 'puedes', 'hacer'], respuesta_simple = False ,palabras_requeridas=['que', 'Que', 'Hacer'])

        respuesta('Whant you gone, de portal 2', ['cual', 'es', 'cancion', 'tu', 'Favorita', 'favorita'], respuesta_simple = False ,palabras_requeridas=['cual', 'Cual', 'cancion', 'Cancion', 'Favorita'])

        respuesta(canto, ['me', 'cancion', 'tu', 'cantame', 'favorita'], respuesta_simple = False ,palabras_requeridas=['cancion', 'favorita', 'cantantame'])

        respuesta('Adios', ['Adios','nos', 'vemos', 'hasta', 'pronto', 'salir'], respuesta_simple = True)


        best_match =  max(probabilidad_mayor, key=probabilidad_mayor.get)


        return 'No estoy seguro de lo que quieres decir' if probabilidad_mayor[best_match] < 1 else best_match


if __name__ == "__main__":
    chat = chatBot();
    while True:
        print('Bot: ', chat.get_respuesta(input('Tu: ')))

