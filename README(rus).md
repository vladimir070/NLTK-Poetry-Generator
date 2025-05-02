# Генератор стихов с использованием NLTK

Конфигурируемый генератор стихов с поддержкой различных схем рифмовки, использующий фонетические алгоритмы NLTK.

## Возможности
- 🎭 **Гибкие схемы рифмовки**: ABAB, ABBA и кастомные шаблоны
- 📚 **Тематические словари**: Предопределенные группы слов (природа, эмоции, мистика)
- 🤖 **Интеллектуальное определение рифм**: На базе NLTK + резервные группы рифм
- ✨ **Естественные конструкции**: 4+ шаблона предложений с вариативной структурой
- ⚙️ **Настраиваемые параметры**: Легкая модификация тем и паттернов

## Поддерживаемые схемы рифмовки
**По умолчанию: ABAB**  
Автоматическое чередование рифмующихся строк с шаблонами:  
Строка 1 (A)
Строка 2 (B)
Строка 3 (A)
Строка 4 (B)

**ABBA**  
Обратный паттерн рифмовки:  
Строка 1 (A)
Строка 2 (B)
Строка 3 (B)
Строка 4 (A)

Default: ABAB
A (nature) - The silent moon illuminates night 
B (emotion) - Where heart whispers endless light 
A (nature) - Beneath ancient stones, a flight 
B (emotion) - In shadows dwells forgotten might

ABBA Example:
def generate_poem(): line1, rhyme1 = generate_rhyming_line(group='nature') 
# A line2, rhyme2 = generate_rhyming_line(group='emotion') 
# B line3, rhyme3 = generate_rhyming_line(prev_rhyme=rhyme2)
# B line4, rhyme4 = generate_rhyming_line(prev_rhyme=rhyme1) 
# A return format_poem([line1, line2, line3, line4])

Installation
pip install -r requirements.txt python -m nltk.downloader cmudict

Configuration Modify in code:

rhyme_groups = { 'nature': ['night', 'light', 'flight', 'sight'], 'emotion': ['heart', 'art', 'part', 'start'], 'mystic': ['veil', 'pale', 'tale', 'grail'] }

subjects = ['moon', 'star', 'wind', 'ocean', 'flame'] 
verbs = ['whispers', 'dances', 'transforms', 'awakens'] 
adjectives = ['silent', 'crimson', 'ancient', 'mystic']

Sample Output

The radiant forest breathes night,
Where shadows weave their secret art.
A fragile dream recalls the light,
In silent waves, reborn heart.
