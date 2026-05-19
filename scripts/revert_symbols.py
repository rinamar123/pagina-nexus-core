import os

file_path = 'c:/Users/SANDRA/Desktop/LABbb de RINA/lab1/Laboratorio_RinaMarriaga/student_portal/templates/student_portal/curso.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('✓', 'âœ”')
content = content.replace('🕒', 'ðŸ•’')
content = content.replace('🔒', 'ðŸ”’')
content = content.replace('🏆', 'ðŸ †')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Symbols reverted successfully.')
