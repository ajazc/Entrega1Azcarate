# Pasos para el desarrolo de un proyecto
	Ir a la carpeta y ejecutar
	python -m django startproject ProyectoFinal
	crear app
        python manage.py startapp AppFutbol
	crear carpeta template dentro de la app
	registrar la app en setting dentro del proyecto inicial
	Corro el siguiente comando para verificar que este todo correcto con la app
		python .\manage.py check AppFutbol
	hago un commit
# Algunos modelos propuestos
jugadores
	nombre
	numero
	posicion
	equipo
	edad
equipos
	Nombre
	pais
	nombre_entrenador
partidos
	identificador
	equipo 1
	equipo 2 
	fecha_partido

### Luego de crear los modelos hay que realizar las migraciones
python manage.py makemigrations
python manage.py migrate
### Dentro del proyecto en urls.py es necesario agregar
  la ruta general que va atender la aplicacion en este caso AppFutbol
### Creo las views o controladores que van a contestar a las solicitudes del usuario

### Mi idea con los templates es tener una base de template que contendra boostraps y desde ahi heredan el resto

### Agregado boostraps con rutas static

### El archivo base.html va ser el padre del resto de los html 

### En el archivo forms.py comienzo a crear los formularios


# RUTAS DEL PROYECTO 
	host:8000/AppFutbol/ ----> inicio 
	host:8000/AppFutbol/jugadores ----> formulario para cargar jugador
	host:8000/AppFutbol/equipos ----> formulario para cargar equipo
	host:8000/AppFutbol/partidos ----> formulario para cargar partidos
	host:8000/AppFutbol/Buscar ----> formulario para buscar un jugador
	host:8000/AppFutbol/BuscarJugadores ----> Presenta los resultados de la busqueda 
	host:8000/AppFutbol/VerPartidos ----> Muestra los partidos
	host:8000/AppFutbol/VerEquipos ----> Muestra los Equipos


# FUNCIONALIDADES 
	DENTRO DEL ARCHIVO VIEWS.PY SE ENCUENTRAN LAS DEFINICIONES DE LAS FUNCIONALIDADES QUE ATIENDEN CADA UNA DE LAS RUTAS
# ADMIN 
	aazcarate
	1234