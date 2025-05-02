# Poetry Generator with NLTK

A configurable poetry generator supporting multiple rhyme schemes, powered by NLTK's phonetic algorithms.

## Features
- 🎭 **Flexible Rhyme Schemes**: ABAB, ABBA, and custom patterns
- 📚 **Thematic Dictionaries**: Predefined word groups (nature, emotion, mystic)
- 🤖 **Smart Rhyme Detection**: NLTK-based + fallback rhyme groups
- ✨ **Natural Constructions**: 4+ sentence templates with varied structures
- ⚙️ **Customizable Parameters**: Easily modify themes and patterns

## Supported Rhyme Schemes
**Default: ABAB**  
A (nature) - The silent moon illuminates night
B (emotion) - Where heart whispers endless light
A (nature) - Beneath ancient stones, a flight
B (emotion) - In shadows dwells forgotten might

**ABBA Example**:  
def generate_poem():
    line1, rhyme1 = generate_rhyming_line(group='nature')  # A
    line2, rhyme2 = generate_rhyming_line(group='emotion') # B
    line3, rhyme3 = generate_rhyming_line(prev_rhyme=rhyme2) # B
    line4, rhyme4 = generate_rhyming_line(prev_rhyme=rhyme1) # A
    return format_poem([line1, line2, line3, line4])

## Installation
pip install -r requirements.txt
python -m nltk.downloader cmudict

Configuration
Modify in code:

rhyme_groups = {
    'nature': ['night', 'light', 'flight', 'sight'],
    'emotion': ['heart', 'art', 'part', 'start'],
    'mystic': ['veil', 'pale', 'tale', 'grail']
}

subjects = ['moon', 'star', 'wind', 'ocean', 'flame']
verbs = ['whispers', 'dances', 'transforms', 'awakens']
adjectives = ['silent', 'crimson', 'ancient', 'mystic']

Sample Output

The radiant forest breathes night,  
Where shadows weave their secret art.  
A fragile dream recalls the light,  
In silent waves, reborn heart.  
Full Documentation | Changelog
