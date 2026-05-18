import os

file_path = 'c:/Users/SANDRA/Desktop/LABbb de RINA/lab1/Laboratorio_RinaMarriaga/student_portal/templates/student_portal/curso.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First handle the multi-character ones
content = content.replace('TEORÃ A', 'TEORÍA')
content = content.replace('PRÃ CTICO', 'PRÁCTICO')
content = content.replace('estÃ ', 'está ')

replacements = {
    'Ã³': 'ó',
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã­': 'í',
    'Ãº': 'ú',
    'Ã‘': 'Ñ',
    'Ã±': 'ñ',
    'Â¿': '¿',
    'Â¡': '¡',
    'Ã“': 'Ó',
    'Ã‰': 'É',
    'Ã ': 'Á',
    'Ãš': 'Ú',
    'ðŸ“¡': '📡',
    'ðŸ“š': '📚',
    'ðŸ“¥': '📥',
    'ðŸ“‚': '📂',
    'ðŸ“ ': '📌',
    'âœ“': '✓',
    'âš\xa0ï¸ ': '⚠️',
    'ðŸ‘¤': '👤',
    'ðŸ’»': '💻',
    'âˆ‘': '∑',
    'âž”': '➔',
    'ðŸŸ¢': '🟢',
    'ðŸ”´': '🔴',
    'â† ': '←'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done fixing encodings.')
