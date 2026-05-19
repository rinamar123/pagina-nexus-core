import os

file_path = 'c:/Users/SANDRA/Desktop/LABbb de RINA/lab1/Laboratorio_RinaMarriaga/student_portal/templates/student_portal/curso.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

done_icon = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00ff80" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
pending_icon = '<svg width="14" height="14" viewBox="0 0 24 24" fill=\"none\" stroke=\"gray\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"12\" r=\"10\"></circle><polyline points=\"12 6 12 12 16 14\"></polyline></svg>'
lock_icon = '<svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"gray\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"11\" width=\"18\" height=\"11\" rx=\"2\" ry=\"2\"></rect><path d=\"M7 11V7a5 5 0 0 1 10 0v4\"></path></svg>'
trophy_icon = '🏆'

content = content.replace('âœ”', done_icon)
content = content.replace('ðŸ•’', pending_icon)
content = content.replace('ðŸ”’', lock_icon)
content = content.replace('ðŸ †', trophy_icon)
content = content.replace('SOPORTE TÃ‰CNICO', 'SOPORTE TÉCNICO')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Icons and text fixed successfully.')
