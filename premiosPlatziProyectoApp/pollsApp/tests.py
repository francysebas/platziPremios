import datetime
from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from .models import Pregunta

# Create your tests here.

class PreguntaModelTests(TestCase):

    def test_publicado_con_futura_pregunta(self):
        '''retorna falso para la preguntas fechas y preguntas que son del futuro, no serian recientes'''
        time= timezone.now()+datetime.timedelta(days=30)
        futura_pregunta= Pregunta(pregunta_text="Quien es el mejor director de cursos de platzi", publicacion_fecha=time)
        self.assertIs(futura_pregunta.test_publicado_con_futura_pregunta(), False)

    def test_publicado_con_pasado_pregunta(self):
        '''retorna falso para la preguntas fechas y preguntas que son del futuro, no serian recientes'''
        time= timezone.now()+datetime.timedelta(days=30)
        futura_pregunta= Pregunta(pregunta_text="Quien es el mejor director de cursos de platzi", publicacion_fecha=time)
        self.assertIs(futura_pregunta.test_publicado_con_pasado_pregunta(), False)

    def test_publicado_con_igual_pregunta(self):
        '''retorna falso para la preguntas fechas y preguntas que son del futuro, no serian recientes'''
        time= timezone.now()
        futura_pregunta= Pregunta(pregunta_text="Quien es el mejor director de cursos de platzi", publicacion_fecha=time)
        self.assertIs(futura_pregunta.test_publicado_con_igual_pregunta(), False)