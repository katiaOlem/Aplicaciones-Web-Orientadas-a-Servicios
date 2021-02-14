import json


horoscopo =[
  
    {
      "name":"Aries",
      "elemento": "Fuego",
      "numero" :"7,17 & 21 ",
      "color":"rojo",
      "horoscopo":"Mirar el lado positivo de las cosas es algo que hoy debes imponerte como una obligación. Puede que no estés de acuerdo con muchas cosas, pero enfadarte solo va a perjudicarte a ti y los demás van a seguir su camino tan tranquilos, tenlo en cuenta",
      "icono":"https://static.diariofemenino.com/media/20983/c/horoscopo-de-la-mujer-aries-asi-es-su-caracter-y-personalidad-lg.jpg",
      "fecha":"21 de Marzo - 20 de Abril"

    },
    {

      "name":"Tauro",
      "elemento": "Tierra",
      "numero" :"4,6 & 11 ",
      "color":"Verde",
      "horoscopodeldia":"Le gusta lo concreto y disfruta de los bienes materiales, el lujo y lo relacionado con lo terrenal; es racional y algo materialista. Suele ser tranquilo y paciente, sabe esperar el momento oportuno para sus objetivos. Como buen signo de tierra está muy apegado a la naturaleza y valora el hogar y la familia. A veces es muy conformista y puede ser brusco, algo que sorprende a los que le rodean.",
      "icono":"https://tvazteca.brightspotcdn.com/dims4/default/cee3a22/2147483647/strip/true/crop/1920x1080+0+0/resize/968x545!/format/jpg/quality/80/?url=https%3A%2F%2Ftvazteca.brightspotcdn.com%2F98%2F3f%2F5530b212491db73f453128ec6539%2Fzodiac-timemachine-tauro.jpg",
      "fecha":"21 de Abril - 20 de Mayo"



    },
    {

      "name":"Géminis",
      "elemento": "Aire",
      "numero" :"3,12 & 18.",
      "color":"Amarillo",
      "horoscopodeldia":"Llega el fin de la semana y con él la oportunidad de descansar y desconectar de tensiones inútiles que no te aportan nada bueno y lo sabes de sobra. Debes hacer un ejercicio de control para evitarlas. Un buen paseo te ayudará a sentirte mejor, con buen tono.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-geminis.jpg",
      "fecha":"21 de Mayo - 20 de Junio"


    },
    {

      "name":"Cáncer",
      "elemento": "Agua",
      "numero" :" 2,8 & 12",
      "color":"Blanco",
      "horoscopodeldia":"Es el más extraño de todo el zodiaco y en ocasiones aparece como muy sentimental y en otras como un personaje inaccesible que vive en su propio mundo. Como signo de agua, posee una intuición y una imaginación fuera de lo común. A veces es muy ingenuo pero siempre cree firmemente en la bondad de las personas. En el amor, necesita protección y sentirse seguro.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-cancer.jpg",
      "fecha":"21 de Junio - 20 de Julio"



    },
    {

      "name":"Leo",
      "elemento": "Fuego",
      "numero" :"1,9 & 10",
      "color":"Amarillo",
      "horoscopodeldia":"Su personalidad resulta, simplemente, arrolladora. Regido por el sol, posee una fuerza que impulsa a moverse a los demás y siempre quiere brillar y dominar. Y esto, que es una cualidad, a menudo se convierte en un defecto porque puede ser bastante dominante e intransigente. Sin embargo, no conoce la venganza, es generoso en lo material y en lo personal y es el mejor jefe para un equipo.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-leo.jpg",
      "fecha":"21 de Julio - 21 de Agosto"



    },
    {

      "name":"Virgo ",
      "elemento": "Tierra",
      "numero" :"10,15 & 27",
      "color":"Marrón",
      "horoscopodeldia":"Reflexivo, práctico y ordenado, le apasiona lo establecido y piensa bien cada paso que da. Signo de tierra, y muy trabajador, es capaz de llevar a cabo grandes empresas por su mente detallista y esquemática, lo que a veces le lleva a cierta obsesión. Siempre tiene una palabra amable para cualquier persona y en el amor, su corazón y su mente entran en conflicto demasiado a menudo.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-virgo.jpg",
      "fecha":"22 de Agosto - 22 de Septiembre"



    },
    {

      "name":"Libra",
      "elemento": "Aire",
      "numero" :" 2,8 & 19",
      "color":"Rosa",
      "horoscopodeldia":"Sereno y tranquilo, mantiene siempre el equilibrio entre lo posible y sus sueños, aunque lucha por ellos. Signo de aire, dominado por Venus, su carácter es fuerte y no se precipita en comprometerse con nada ni con nadie si no lo ve claro, lo que le lleva a evitar situaciones desagradables sean las que sean. Suele ser simpático y sociable y con sensibilidad para el arte.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-libra.jpg",
      "fecha":"23 de Septiembre - 22 de Octubre"



    },
    {

      "name":"Escorpio",
      "elemento": "Agua",
      "numero" :" 4,13 & 21",
      "color":"Rojo",
      "horoscopodeldia":"Misterioso y contradictorio, signo de agua bajo la dominante de Marte y Plutón, posee un carácter apasionado y sensual que resulta muy atractivo. En general es muy inteligente, lo que le hace ser versátil para conseguir sus fines que a veces son poco claros. Su voluntad es férrea, muy vitalista y con fuerte sexualidad, nunca resulta indiferente ni en el amor ni en el trabajo.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-escorpio.jpg",
      "fecha":"23 de Octubre - 22 de Noviembre"



    },
    {

      "name":"Sagitario",
      "elemento": "Fuego",
      "numero" :" 9,14 & 23",
      "color":"Violeta",
      "horoscopodeldia":"Es un aventurero nato que siempre mira hacia delante y posee una naturaleza dual que le lleva a ser a veces muy evolucionado y otras muy primitivo. Signo de fuego, dominado por Júpiter, no le gustan las injusticias ni los dobleces. Es comunicativo, alegre y expansivo, aunque no soporta las críticas y puede ser bastante derrochador. En lo afectivo, necesita sentirse libre.",
      "icono":"https://cloudfront-us-east-1.images.arcpublishing.com/radiomitre/7D7UAELJ5NH2JBVYZ2S56BD6YI.gif",
      "fecha":"23 de Noviembre - 20 de Diciembre"



    },
    {

      "name":"Capricornio",
      "elemento": "Tierra",
      "numero" :" 3,6 & 25",
      "color":"Gris",
      "horoscopodeldia":"Es uno de los más disciplinados del zodiaco y lo aplica a todo lo que rodea su vida. Es un signo de tierra, dominado por Saturno que le hace ser constructor y reflexivo. Normalmente es muy realista y alcanza el éxito por su tesón. Demasiado introspectivo, le cuesta expresar sus emociones y sus sentimientos y nadie penetra en su intimidad. Tiene un alto sentido del deber.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-capricornio.jpg",
      "fecha":"21 de Diciembre - 19 de Enero"



    },
    {

      "name":"Acuario",
      "elemento": "Aire",
      "numero" :" 7,14 & 20",
      "color":"azul turquesa",
      "horoscopodeldia":"Su espíritu es poderoso, sabe ver hacia el futuro con libertad intelectual y de espíritu y posee una gran imaginación. Signo de aire, dominado por Saturno y Urano, a veces es algo melancólico y cae fascinado por lo misterioso, lo que le lleva a ser poco práctico. Es altruista y le gusta probar cualquier clase de innovación. Afectivamente es cautivador, pero no soporta la monotonía.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-acuario.jpg",
      "fecha":"20 de Enero - 18 de Febrero"



    },
    {

      "name":"Piscis",
      "elemento": "Agua",
      "numero" :" 19",
      "color":"violeta",
      "horoscopodeldia":"Es un excelente amigo dispuesto a ayudar y hacer favores. Es sensible, amable e intuitivo y suele acertar en sus juicios. Son afectuosos y casi siempre sinceros y pacíficos. Signo de agua, dominado por Júpiter y Neptuno, lucha demasiado consigo mismo y tiene tendencia a la soledad. Vive un mundo muy espiritual y en el amor suele ser muy romántico y sentimental.",
      "icono":"https://horoscopo.lavanguardia.com/img/horoscopo-piscis.jpg",
      "fecha":"19 de Febrero - 20 de Marzo"



    }




  ]

print(horoscopo[11])