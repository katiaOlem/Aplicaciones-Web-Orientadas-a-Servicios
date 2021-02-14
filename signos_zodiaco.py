import json 
import web
import random #//texto aleatorio



zodiacales= {}
urls = (
  '/(.*)','Signos',
)

app = web.application(urls, globals())

class Signos():
  def __init__(self):
    pass
      
  def GET(self, fechas):
    try:
      mes = int(fechas[3:5])
      dia = int(fechas[0:2])
      print(mes,dia)
      dia = random.randint(0,11) #//horoscopos del dia 

      horos = ["Mirar el lado positivo de las cosas es algo que hoy debes imponerte como una obligación. Puede que no estes de acuerdo con muchas cosas, pero enfadarte solo va a perjudicarte a ti y los demas van a seguir su camino tan tranquilos, tenlo en cuenta",
      "Le gusta lo concreto y disfruta de los bienes materiales, el lujo y lo relacionado con lo terrenal; es racional y algo materialista. Suele ser tranquilo y paciente, sabe esperar el momento oportuno para sus objetivos. Como buen signo de tierra esta muy apegado a la naturaleza y valora el hogar y la familia. A veces es muy conformista y puede ser brusco, algo que sorprende a los que le rodean.",
      "Llega el fin de la semana y con el la oportunidad de descansar y desconectar de tensiones inutiles que no te aportan nada bueno y lo sabes de sobra. Debes hacer un ejercicio de control para evitarlas. Un buen paseo te ayudara a sentirte mejor, con buen tono.",
      "Es el mas extraño de todo el zodiaco y en ocasiones aparece como muy sentimental y en otras como un personaje inaccesible que vive en su propio mundo. Como signo de agua, posee una intuición y una imaginacion fuera de lo comun. A veces es muy ingenuo pero siempre cree firmemente en la bondad de las personas. En el amor, necesita proteccion y sentirse seguro.",
      "Su personalidad resulta, simplemente, arrolladora. Regido por el sol, posee una fuerza que impulsa a moverse a los demas y siempre quiere brillar y dominar. Y esto, que es una cualidad, a menudo se convierte en un defecto porque puede ser bastante dominante e intransigente. Sin embargo, no conoce la venganza, es generoso en lo material y en lo personal y es el mejor jefe para un equipo.",
      "Reflexivo, practico y ordenado, le apasiona lo establecido y piensa bien cada paso que da. Signo de tierra, y muy trabajador, es capaz de llevar a cabo grandes empresas por su mente detallista y esquematica, lo que a veces le lleva a cierta obsesion. Siempre tiene una palabra amable para cualquier persona y en el amor, su corazon y su mente entran en conflicto demasiado a menudo.",
      "Sereno y tranquilo, mantiene siempre el equilibrio entre lo posible y sus sueños, aunque lucha por ellos. Signo de aire, dominado por Venus, su caracter es fuerte y no se precipita en comprometerse con nada ni con nadie si no lo ve claro, lo que le lleva a evitar situaciones desagradables sean las que sean. Suele ser simpatico y sociable y con sensibilidad para el arte.",
      "Misterioso y contradictorio, signo de agua bajo la dominante de Marte y Pluton, posee un carácter apasionado y sensual que resulta muy atractivo. En general es muy inteligente, lo que le hace ser versatil para conseguir sus fines que a veces son poco claros. Su voluntad es ferrea, muy vitalista y con fuerte sexualidad, nunca resulta indiferente ni en el amor ni en el trabajo.",
      "Es un aventurero nato que siempre mira hacia delante y posee una naturaleza dual que le lleva a ser a veces muy evolucionado y otras muy primitivo. Signo de fuego, dominado por Jupiter, no le gustan las injusticias ni los dobleces. Es comunicativo, alegre y expansivo, aunque no soporta las criticas y puede ser bastante derrochador. En lo afectivo, necesita sentirse libre.",
      "Es uno de los mas disciplinados del zodiaco y lo aplica a todo lo que rodea su vida. Es un signo de tierra, dominado por Saturno que le hace ser constructor y reflexivo. Normalmente es muy realista y alcanza el exito por su teson. Demasiado introspectivo, le cuesta expresar sus emociones y sus sentimientos y nadie penetra en su intimidad. Tiene un alto sentido del deber.",
      "Su espiritu es poderoso, sabe ver hacia el futuro con libertad intelectual y de espiritu y posee una gran imaginacion. Signo de aire, dominado por Saturno y Urano, a veces es algo melancolico y cae fascinado por lo misterioso, lo que le lleva a ser poco practico. Es altruista y le gusta probar cualquier clase de innovacion. Afectivamente es cautivador, pero no soporta la monotonia.",
      "Es un excelente amigo dispuesto a ayudar y hacer favores. Es sensible, amable e intuitivo y suele acertar en sus juicios. Son afectuosos y casi siempre sinceros y pacificos. Signo de agua, dominado por Jupiter y Neptuno, lucha demasiado consigo mismo y tiene tendencia a la soledad. Vive un mundo muy espiritual y en el amor suele ser muy romantico y sentimental."


     


      ]
      horoscopo = {}

     #//"Aries"
      if dia >= 21 and mes == 3 or mes == 4 and dia <= 20:
        horoscopo= {}
        horoscopo["name"]="Aries"
        horoscopo["elemento"] = "Fuego"
        horoscopo["numero"] = "7,17 & 21 "
        horoscopo["color"]="rojo"
        horoscopo["horoscopodia"] = horos[dia]
        horoscopo["icono"]="https://static.diariofemenino.com/media/20983/c/horoscopo-de-la-mujer-aries-asi-es-su-caracter-y-personalidad-lg.jpg"
        horoscopo["fecha"] = "21 de Marzo - 20 de Abril"
        result= json.dumps(horoscopo)
        return result
       
       #//"Tauro"
      elif  dia >= 21 and mes == 4 or mes == 5 and dia <= 20:
        horoscopo = {}
        horoscopo["name"] ="Tauro"
        horoscopo["elemento"] = "Tierra"
        horoscopo["numero"] = "4,6 & 11 "
        horoscopo["color"] ="Verde"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://tvazteca.brightspotcdn.com/dims4/default/cee3a22/2147483647/strip/true/crop/1920x1080+0+0/resize/968x545!/format/jpg/quality/80/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F98%2F3f%2F5530b212491db73f453128ec6539%2Fzodiac-timemachine-tauro.jpg",
        horoscopo["fecha"] = "21 de Abril - 20 de Mayo"
        result= json.dumps(horoscopo)
        return result

       #///"Geminis"
      elif  dia >= 21 and mes == 5 or mes == 6 and dia <= 20:
        horoscopo = {}
        horoscopo["name"] ="Geminis"
        horoscopo["elemento"] = "Aire"
        horoscopo["numero"] = "3,12 & 18. "
        horoscopo["color"] ="Amarillo"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-geminis.jpg"
        horoscopo["fecha"] = "21 de Mayo - 20 de Junio"
        result= json.dumps(horoscopo)
        return result

      #//"Cancer"
      elif  dia >= 21 and mes == 6 or mes == 7 and dia <= 20:
        horoscopo = {}
        horoscopo["name"] ="Cancer"
        horoscopo["elemento"] = "Agua"
        horoscopo["numero"] = "2,8 & 12"
        horoscopo["color"] ="Blanco"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-cancer.jpg"
        horoscopo["fecha"] = "21 de Junio - 20 de Julio"
        result= json.dumps(horoscopo)
        return result

       #"Leo"//
      elif  dia >= 21 and mes == 7 or mes == 8 and dia <= 21:
        horoscopo = {}
        horoscopo["name"] ="Leo"
        horoscopo["elemento"] = "Fuego"
        horoscopo["numero"] = "1,9 & 10"
        horoscopo["color"] ="Amarillo"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-leo.jpg"
        horoscopo["fecha"] = "21 de Julio - 21 de Agosto"
        result= json.dumps(horoscopo)
        return result


      #//"Virgo"
      elif  dia >= 22 and mes == 8 or mes == 9 and dia <= 22:
        horoscopo = {}
        horoscopo["name"] ="Virgo"
        horoscopo["elemento"] = "Tierra"
        horoscopo["numero"] = "10,15 & 27"
        horoscopo["color"] ="Marron"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-virgo.jpg"
        horoscopo["fecha"] = "22 de Agosto - 22 de Septiembre"
        result= json.dumps(horoscopo)
        return result


     #"Libra"//
      elif  dia >= 23 and mes == 9 or mes == 10 and dia <= 22:
        horoscopo = {}
        horoscopo["name"] ="Libra"
        horoscopo["elemento"] = "Aire"
        horoscopo["numero"] = "2,8 & 19"
        horoscopo["color"] ="Rosa"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-libra.jpg"
        horoscopo["fecha"] = "23 de Septiembre - 22 de Octubre"
        result= json.dumps(horoscopo)
        return result

        #//"Escorpio"
      elif  dia >= 23 and mes == 10 or mes == 11 and dia <= 22:
        horoscopo = {}
        horoscopo["name"] ="Escorpio"
        horoscopo["elemento"] = "Agua"
        horoscopo["numero"] = "4,13 & 21"
        horoscopo["color"] ="Rojo"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-escorpio.jpg"
        horoscopo["fecha"] = "23 de Octubre - 22 de Noviembre"
        result= json.dumps(horoscopo)
        return result


      #"Sagitario"//
      elif  dia >= 23 and mes == 11 or mes == 12 and dia <= 20:
        horoscopo = {}
        horoscopo["name"] ="Sagitario"
        horoscopo["elemento"] = "Fuego"
        horoscopo["numero"] = "9,14 & 23"
        horoscopo["color"] ="Violeta"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://cloudfront-us-east-1.images.arcpublishing.com/radiomitre/7D7UAELJ5NH2JBVYZ2S56BD6YI.gif"
        horoscopo["fecha"] = "23 de Noviembre - 20 de Diciembre"
        result= json.dumps(horoscopo)
        return result


      #//"Capricornio"
      elif  dia >= 21 and mes == 12 or mes == 1 and dia <= 19:
        horoscopo = {}
        horoscopo["name"] ="Capricornio"
        horoscopo["elemento"] = "Tierra"
        horoscopo["numero"] = "3,6 & 25"
        horoscopo["color"] ="Gris"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-capricornio.jpg"
        horoscopo["fecha"] = "21 de Diciembre - 19 de Enero"
        result= json.dumps(horoscopo)
        return result 
      
      #//"Acuario"
      elif  dia >= 20 and mes == 1 or mes == 2 and dia <= 18:
        horoscopo = {}
        horoscopo["name"] ="Acuario"
        horoscopo["elemento"] = "Aire"
        horoscopo["numero"] = "7,14 & 20"
        horoscopo["color"] ="Turquesa"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-acuario.jpg"
        horoscopo["fecha"] = "20 de Enero - 18 de Febrero"
        result= json.dumps(horoscopo)
        return result 
      #//piscis
      elif  dia >= 19 and mes == 2 or mes == 3 and dia <= 20:
        horoscopo = {}
        horoscopo["name"] ="Piscis"
        horoscopo["elemento"] = "Agua"
        horoscopo["numero"] = "19"
        horoscopo["color"] ="Violeta"
        horoscopo["horoscopodeldia"] = horos[dia]
        horoscopo["icono"] = "https://horoscopo.lavanguardia.com/img/horoscopo-piscis.jpg"
        horoscopo["fecha"] = "19 de Febrero - 20 de Marzo"
        result= json.dumps(horoscopo)
        return result 
      
    except:
      
      horoscopo = {}
      horoscopo["Fecha"] = "Para  Conocer tu Signo " + str(fechas)
      horoscopo["Signo"] = "Ingrese su fecha de nacimiento comenzando por dia/mes"
      result= json.dumps(horoscopo)
      return result


if __name__ == "__main__":
	app.run()



     
      


      
