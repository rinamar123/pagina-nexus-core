import os
import re

file_path = 'c:/Users/SANDRA/Desktop/LABbb de RINA/lab1/Laboratorio_RinaMarriaga/student_portal/templates/student_portal/curso.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

done_icon = '<span class="status-icon status-done"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00ff80" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></span>'
pending_icon = '<span class="status-icon status-pending"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="gray" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></span>'
lock_icon = '<span class="status-icon" style="opacity: 0.5;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="gray" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></span>'

# Replace using regex to avoid dealing with weird characters
content = re.sub(r'<span class="status-icon status-done">.*?</span>', done_icon, content)
content = re.sub(r'<span class="status-icon status-pending">.*?</span>', pending_icon, content)
content = re.sub(r'<span class="status-icon" style="opacity: 0.5;">.*?</span>', lock_icon, content)

# Trophy text
content = re.sub(r'<h2 style="color: var\(--neon-blue\); margin-bottom: 1rem;">.*?PARCIAL FINAL DESBLOQUEADO</h2>', '<h2 style="color: var(--neon-blue); margin-bottom: 1rem;">🏆 PARCIAL FINAL DESBLOQUEADO</h2>', content)
content = content.replace('SOPORTE TÃ‰CNICO', 'SOPORTE TÉCNICO')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Regex replace done.')
