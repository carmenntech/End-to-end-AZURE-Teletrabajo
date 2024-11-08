
# Análisis de datos sobre el teletrabajo mediante Azure ETL

## Descripción general

Este proyecto se centra en el desarrollo de un extenso pipeline de extracción, transformación y carga (ETL) que utiliza las capacidades avanzadas de Microsoft Azure. El pipeline recupera de manera eficiente los datos de la api de datagob para almacenarlos en Azure Blob Storage, las transformaciones necesarias se realizan mediante Azure Databricks (Pyspark) y Azure Data Factory, y los almacena en Azure Data Lake. Los datos analizados finales se almacenan de forma segura en una capa SQL para su uso posterior. Por ultimo se usa Power bi para la visualizacion final de los datos.

## Data flow:

1. **Extraer datos**: Recupera datos mediante http a la api de datagob para procesarlos y cargarlos en Azure Data Lake Storage Gen-2
![image](https://github.com/user-attachments/assets/e6cd5a35-5fb8-4f81-a8fb-90e923a0caa9)

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

## Extraccion de los datos de datagob y almacenamiento en Data Lake (pipeline 1: copy_http_to_storage )

1. Creamos una instancia de datafactory

![image](https://github.com/user-attachments/assets/5fe8abf1-c692-43fb-95f2-baf949e7bf17)

2. Crear link service de tipo http > ponemos el link base a la api de datagob (https://www.ine.es/)

![image](https://github.com/user-attachments/assets/beafe1a9-ccf7-42ee-89aa-2f6a4e54ac15)
![image](https://github.com/user-attachments/assets/a7a4df91-3478-4886-b154-d1a84b3d4cc0)

3. Creamos un dataset de tipo http, la ruta relativa la dejamos en blanco porque pasaremos ese valor por parametro 

![image](https://github.com/user-attachments/assets/408fabc1-b19b-4db8-bc76-be9f7e116a7c)
![image](https://github.com/user-attachments/assets/d1833e02-2419-4f60-bbe4-627004c3a14a)
![image](https://github.com/user-attachments/assets/c60d8090-6383-44e6-9660-fb654b365ff3)
![image](https://github.com/user-attachments/assets/7be954fa-fd51-400d-a0df-d3e5805fcb55)

4. Creamos una cuenta de storage (deshabilitar eliminacion temporal), creamos container 'rawdata'

![image](https://github.com/user-attachments/assets/b58fcfd2-e2e5-4d8a-bf28-fe07924f18ac)

5. Creamos link service y dataset con el container creado (link de tipo blob storage)

![image](https://github.com/user-attachments/assets/ae466e2b-e849-432a-98b5-6659b70d39e2)

![image](https://github.com/user-attachments/assets/1ef3bf9e-0dac-49dd-ae2f-9e07f6bbf2f0)

6. Vamos al apartado de pipelines > nuevo pipeline  > crear actividad de copia de http a storage

![image](https://github.com/user-attachments/assets/9ae3528a-3bb3-43fe-b90a-704eced75472)

7. Crear dataset con json guardado en el storage

![image](https://github.com/user-attachments/assets/4d36a126-b8f0-4ac6-aab3-4fd4d6818847)


8. Lookup > check recursividad y quitar el check de  solo la primera fila 

![image](https://github.com/user-attachments/assets/25abea94-0218-4760-a6d7-bf45a804dcea)

9. ForEach > chech recursividad, elemento: @activity('lookup').output.value
  ![image](https://github.com/user-attachments/assets/49e3a782-22e4-4e23-a8dd-913332db7fd4)

11. Dentro del ForEach copiamos la actividad de copia y cambiamos el parametro creado por @item.sourceURL

![image](https://github.com/user-attachments/assets/8fc61f4a-105e-4003-9a0e-b8c4ed4435d3)





































