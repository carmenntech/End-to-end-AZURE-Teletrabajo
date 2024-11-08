
# Análisis de datos sobre el teletrabajo mediante Azure ETL

## Descripción general

Este proyecto se centra en el desarrollo de un extenso pipeline de extracción, transformación y carga (ETL) que utiliza las capacidades avanzadas de Microsoft Azure. El pipeline recupera de manera eficiente los datos de la api de datagob para almacenarlos en Azure Blob Storage, las transformaciones necesarias se realizan mediante Azure Databricks (Pyspark) y Azure Data Factory, y los almacena en Azure Data Lake. Los datos analizados finales se almacenan de forma segura en una capa SQL para su uso posterior. Por ultimo se usa Power bi para la visualizacion final de los datos.

## Data flow:

1. **Extraer datos**: Recupera datos mediante http a la api de datagob para procesarlos y cargarlos en Azure Data Lake Storage Gen-2
2. **Transformar datos** : Utiliza PySpark en Azure Databricks para analizar y procesar los datos, almacenando los resultados en Azure Data Lake Storage Gen2
3. **Cargar datos** : Transfiere los datos procesados ​​a una base de datos SQL de Azure para establecer una capa de informes para la creación de paneles
4. **Automatizacion**: Construye pipelines de extremo a extremo en Azure Data Factory para automatizar el flujo de datos desde la extracción hasta las capas de informes


## Prerrequisitos

- __Suscripción__ a Microsoft Azure
- __Azure Blob Storage__ : un servicio que proporciona almacenamiento de objetos escalable para grandes cantidades de datos no estructurados, ideal para almacenar imágenes, vídeos y otros datos binarios.
Almacenamiento de Azure Data Lake Gen2 : una solución de almacenamiento altamente escalable diseñada específicamente para análisis de big data, que combina las capacidades de Azure Blob Storage y Azure Data Lake.
- __Azure Databricks__ : una plataforma de análisis avanzada basada en Apache Spark, diseñada para el procesamiento de big data, aprendizaje automático y proyectos colaborativos de ciencia de datos.
- __Azure SQL Server__ : un servicio de base de datos relacional totalmente administrado que utiliza el motor de SQL Server para proporcionar almacenamiento y procesamiento de datos confiables y de alto rendimiento.
- __Base de datos SQL de Azure__ : un servicio de base de datos relacional administrado que ofrece compatibilidad con el motor de SQL Server y proporciona soluciones de bases de datos escalables y seguras para aplicaciones modernas.
- __Azure Data Factory__ : un servicio integral de integración de datos que permite la creación, programación y orquestación de flujos de trabajo ETL (Extracción, Transformación, Carga) y ELT (Extracción, Carga, Transformación), con una interfaz visualmente intuitiva para crear flujos de trabajo basados ​​en datos para mover y transformar datos a escala.

## Conjunto de datos 

El conjunto de datos utilizado en este proyecto contiene información detallada sobre el teletrabajo en España; las ventajas y desventajas de este modelo de trabajo, porcentaje de personas teletrabajadoras por comunidad autonoma, sexo, actividad... 

Origen de los datos:

| URL  | URL API Datagob |
| ------------- | ------------- |
| https://datos.gob.es/es/catalogo/ea0010587-porcentaje-de-la-jornada-laboral-detallada-por-dias-realizada-actualmente-en-modalidad-de-teletrabajo-por-tipo-de-trabajo-segun-su-disponibilidad-para-el-teletrabajo-total-o-parcial-identificador-api-t25-p450-base_2011-a2021-l0-04061-px1)  | https://www.ine.es/jaxi/files/tpx/csv_bdsc/50160.csv |
|https://datos.gob.es/es/catalogo/ea0010587-posibilidad-de-teletrabajar-y-teletrabajo-efectivo-de-forma-total-o-parcial-por-caracteristicas-demograficas-identificador-api-t25-p450-base_2011-a2021-l0-04055-px1|https://www.ine.es/jaxi/files/tpx/csv_bdsc/50154.csv|
|https://datos.gob.es/es/catalogo/ea0010587-ventajas-y-desventajas-declaradas-sobre-el-teletrabajo-por-comunidades-y-ciudades-autonomas-identificador-api-t25-p450-base_2011-a2021-l0-08042-px1|https://www.ine.es/jaxi/files/tpx/csv_bdsc/50077.csv|
|https://datos.gob.es/es/catalogo/ea0010587-acceso-remoto-reuniones-a-traves-de-internet-y-teletrabajo-identificador-api-tpx-cienciaytecn_2981-eticce-a2023_a2024_11941-2ca_11949-1cag_11950-l0-cag04-px|https://www.ine.es/jaxi/files/tpx/csv_bdsc/71035.csv|

# Paso a paso del proyecto

## Extraccion de los datos de datagob y almacenamiento en Data Lake

1. Crear link service de tipo http > ponemos el link base a la api de datagob (https://www.ine.es/)
2. Creamos un dataset de tipo http, creamos un parametro 

## Paso a paso del proyecto

### opcion 1

Creamos el link service a la web (de tipo http) base donde vamos a extraer los csv, en este caso es ine.es

![image](https://github.com/user-attachments/assets/5f476056-9786-41a4-bf2d-7c44ba1363ec)

Despues creamos un dataset con el csv de la plataforma (tambien de tipo http)

![image](https://github.com/user-attachments/assets/17d3d328-b795-40de-928e-78f08fccb560)

Creamos un storage acount de tipo data lake gen 2 y creamos su linked service, despues procedemos a crear un nuevo dataset de tipo data lake

![image](https://github.com/user-attachments/assets/ea8c9801-b3b3-45a5-86bb-d07feca5e222)

---------------------------------------------------------------------------------------

### opcion 2

Creamos dos parametros, uno para la url y otro para el nombre del fichero

![image](https://github.com/user-attachments/assets/15a20af0-c630-4f17-8539-25482b94b418)

Creamos un data lake gen 2, y dentro de el un contenedor 'config' donde cargaremos el json

![image](https://github.com/user-attachments/assets/70323aea-d6c9-4dc0-8d5c-5253c4fbc6ca)

Dataset > Crear nuevo dataset > Azure blob storage > json > seleccionar el json 



![image](https://github.com/user-attachments/assets/14d01161-62b3-490c-83d5-d190514129e6)

for each > check secuencial > Contenido dinamico > @activity('Lookup1').output.value

![image](https://github.com/user-attachments/assets/e102059d-c60d-4d17-8413-2bcf130a56f7)

Dentro de del foreach > set_varibale > nueva variable > añadir contenido dinamico > @item().sourceURL

![image](https://github.com/user-attachments/assets/749d6cfd-46ec-4064-ba92-58f9c2e75515)

### opcion 3

Nuevo link serviced hhtp >

![image](https://github.com/user-attachments/assets/fb4dc8ac-eaf5-428b-bde3-fd51c59957aa)








