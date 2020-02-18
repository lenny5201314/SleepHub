import random
import string

def random_string_generator():
    characters = '0123456789'
    result=''
    for i in range(0, 11):
        result += random.choice(characters)
    
    return result



def unique_music_id_generator(instance):
    music_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(musicid= music_new_id).exists()
    if qs_exists:
        return unique_music_id_generator(instance)
    return music_new_id