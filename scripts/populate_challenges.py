import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import CourseContent, InteractiveChallenge

def populate():
    # Remove existing challenges to avoid duplicates if run multiple times
    InteractiveChallenge.objects.all().delete()
    
    contents = CourseContent.objects.all()
    count = 0
    for content in contents:
        # Just create 1-3 simple challenges for every lesson so it's fully populated
        
        # Challenge 1
        InteractiveChallenge.objects.create(
            content=content,
            prompt=f"Pregunta conceptual sobre {content.title}: ¿Cuál de las siguientes opciones describe mejor el objetivo principal de este tema?",
            code_snippet="",
            choices_json=json.dumps([
                "Optimizar el rendimiento computacional",
                "Comprender el modelo subyacente y aplicar las fórmulas correctamente",
                "Evitar el uso de librerías externas",
                "Ninguna de las anteriores"
            ]),
            correct_index=1,
            feedback="El objetivo de esta lección es comprender el modelo para aplicarlo, no solo optimizar código o evitar librerías."
        )
        
        # Challenge 2
        InteractiveChallenge.objects.create(
            content=content,
            prompt=f"Identificación de errores en {content.title}: Si el sistema presenta un comportamiento anómalo, ¿cuál es el primer paso de depuración?",
            code_snippet="def analizar(data):\n    # TODO: Revisar posibles fallos\n    return procesar(data)",
            choices_json=json.dumps([
                "Borrar el código y empezar de nuevo",
                "Revisar el log de errores y los datos de entrada",
                "Aumentar los recursos del servidor (RAM/CPU)",
                "Ignorar la anomalía si ocurre raramente"
            ]),
            correct_index=1,
            feedback="Siempre debes empezar revisando los logs y los datos de entrada para entender el contexto del error."
        )
        
        # Challenge 3
        InteractiveChallenge.objects.create(
            content=content,
            prompt=f"Aplicación de {content.title} en un entorno real:",
            code_snippet="",
            choices_json=json.dumps([
                "Se usa exclusivamente en laboratorios de investigación",
                "Solo es útil para problemas teóricos",
                "Se puede aplicar para resolver problemas complejos de clasificación, optimización o predicción en la industria",
                "Su aplicación comercial está prohibida"
            ]),
            correct_index=2,
            feedback="Casi todos estos conceptos tienen aplicaciones directas en la industria (sistemas de recomendación, logística, finanzas, etc)."
        )
        count += 3

    print(f"✅ Se crearon {count} retos interactivos (3 por lección).")

if __name__ == '__main__':
    populate()
