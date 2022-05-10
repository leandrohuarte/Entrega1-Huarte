# Entrega1-Proyecto final del curso Python de CoderHouse
Entrega intermedia del proyecto final
Con Cassandra Gaggiotti elegimos hacer una página de venta de juegos digitales. 
Tomamos el archivo del entregable anterior mío (MVT_HUARTE), cambiamos el nombre de la aplicacion a AppJuegos y como primera medida le agregamos las clases que queríamos en models (juegos PS4, colecciones y pagos), junto con sus views, importando los modelos necesarios en cada caso.
Posteriormente generamos el urls.py dentro de la app para agregar los path, y en el url de la carpeta del proyecto global agregamos el url de la app.
Chequeamos el funcionamiento de los mismos, con el checkapp y runserver, para verificar que las clases estaban bien creadas y relacionadas con sus vistas.
Agregamos en admin.py los modelos para registrarlos.
Creamos un html dentro de la app para cada cada clase, las vinculamos a las views para tener una vista por modelo. Chequeamos nuevamente su vinculación, y procedimos a crear el html padre, borrando lo que no nos interesaba y colocando el bloque con la info que queríamos que cambiara en cada vista de html.
Una vez comprobado su correcto funcionamiento, creamos el forms.py, y generamos los formularios con la funcion def dentro de views para cada clase. Comprobamos su funcionamiento y generamos cada html de cada formulario para cargar datos. A su vez, hicimos el mismo procedimiento para la busqueda dentro de la base de datos.
Agregamos los path a urls.py de la aplicación, con su correspondiente views y volvimos a correr el codigo.
Para el de PS4 en particular modificamos el html para que aparezca el formulario de carga dentro de la página misma.
