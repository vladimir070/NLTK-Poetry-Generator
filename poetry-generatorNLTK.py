import nltk
import random

# (Предварительно, загружены необходимые ресурсы: CMUdict - см. выше)

# Списки слов (можно настроить)
subjects = ['star', 'moon', 'wind', 'heart', 'sky', 'ocean', 'dream', 'fire', 'rain', 'sun', 'shadow', 'world', 'soul', 'time', 'hope', 'love', 'night', 'day', 'sea', 'earth', 'sea', 'tree', 'bee', 'me', 'key', 'knee', 'degree']  # Добавлено много рифмующихся
verbs = ['shines', 'glows', 'whispers', 'beats', 'lights', 'flows', 'dances', 'burns', 'falls', 'dreams', 'weeps', 'sings', 'flies', 'moves', 'breathes', 'remembers', 'forgets', 'lives', 'dies', 'exists', 'sees', 'flees', 'bends', 'sends', 'ends'] # Добавлено много рифмующихся
adjectives = ['bright', 'silent', 'gentle', 'brave', 'clear', 'deep', 'dark', 'cold', 'warm', 'vast', 'ancient', 'sacred', 'golden', 'silver', 'fragile', 'eternal', 'secret', 'lost', 'free', 'wild', 'blue', 'new', 'true', 'few', 'through', 'hue'] # Добавлено много рифмующихся
adverbs = ['gently', 'brightly', 'softly', 'quickly', 'clearly', 'deeply', 'boldly', 'freely', 'truly', 'newly', 'throughly', 'dearly', 'nearly'] # Добавлено много рифмующихся
#Для более сложной рифмовки, можно разбить все на группы
# Grouping words by potential rhyme - не идеально, но хоть что-то
group_a = ['sun', 'run', 'fun', 'one']
group_b = ['glows', 'shows', 'knows', 'goes', 'flows']
group_c = ['night', 'light', 'sight', 'flight', 'delight', 'kite', 'bright', 'height', 'mite', 'blight', 'right', 'white', 'fright', 'plight', 'bite', 'write', 'invite']
group_d = ['free', 'see', 'me', 'be', 'tree']

# Функция для получения рифм
def get_rhymes(word):
    """Возвращает список слов, рифмующихся с заданным словом."""
    try:
        from nltk.corpus import cmudict
        pronouncing_dict = cmudict.dict()
        rhymes = []
        for pron in pronouncing_dict.get(word, []):  #Обрабатываем случаи, когда слова нет
            rhymes.extend(
                [word for word, pron2 in pronouncing_dict.items() if pron == pron2[-1]]
            )
        return rhymes
    except LookupError:
        nltk.download('cmudict')
        return []


def generate_rhyming_line(line_number, prev_rhyme_word=None, use_group=False):
    """Генерирует строку, рифмующуюся с prev_rhyme_word."""
    if line_number in (0, 2): #Первая и третья строки - случайные
        if use_group:
             subject = random.choice(subjects)
             verb = random.choice(verbs)
             rhyme_word = random.choice(group_c)  #Используем отдельный список рифмы
             return f"{subject} {verb} the {rhyme_word}"
        else:
             subject = random.choice(subjects)
             verb = random.choice(verbs)
             adjective = random.choice(adjectives)
             return f"{subject} {verb} {adjective}"
    else: #Вторая и четвертая строки - должны рифмоваться с предыдущими
        if prev_rhyme_word is None:
            return "Error: No previous word for rhyme!"
        rhymes = get_rhymes(prev_rhyme_word)
        if rhymes:
            rhyme_word = random.choice(rhymes) #Выбираем случайное слово, рифмующееся с предыдущим
            return f"And {random.choice(verbs)} in the {rhyme_word}" #Используем это слово для рифмы
        else:
            return f"No rhymes found for {prev_rhyme_word}"


def generate_poem():
    """Генерирует четверостишье с рифмой ABAB."""
    line1 = generate_rhyming_line(0, use_group=True) #Используем группы для рифмы
    word1 = line1.split()[-1] #берем последнее слово для рифмы
    line2 = generate_rhyming_line(1, word1) #Передаем последнее слово первой строки
    line3 = generate_rhyming_line(2, use_group=True) #Используем группы для рифмы
    word3 = line3.split()[-1] #берем последнее слово третьей строки для рифмы
    line4 = generate_rhyming_line(3, word3) #Передаем последнее слово третьей строки
    return f"{line1}\n{line2}\n{line3}\n{line4}"

poem = generate_poem()
print(poem)