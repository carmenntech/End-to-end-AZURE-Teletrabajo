
### Extraccion de los datos de datagob 

https://datos.gob.es/es/catalogo/ea0010587-porcentaje-de-la-jornada-laboral-detallada-por-dias-realizada-actualmente-en-modalidad-de-teletrabajo-por-tipo-de-trabajo-segun-su-disponibilidad-para-el-teletrabajo-total-o-parcial-identificador-api-t25-p450-base_2011-a2021-l0-04061-px1

https://datos.gob.es/es/catalogo/ea0010587-posibilidad-de-teletrabajar-y-teletrabajo-efectivo-de-forma-total-o-parcial-por-caracteristicas-demograficas-identificador-api-t25-p450-base_2011-a2021-l0-04055-px1

https://datos.gob.es/es/catalogo/ea0010587-ventajas-y-desventajas-declaradas-sobre-el-teletrabajo-por-comunidades-y-ciudades-autonomas-identificador-api-t25-p450-base_2011-a2021-l0-08042-px1

https://datos.gob.es/es/catalogo/ea0010587-acceso-remoto-reuniones-a-traves-de-internet-y-teletrabajo-identificador-api-tpx-cienciaytecn_2981-eticce-a2023_a2024_11941-2ca_11949-1cag_11950-l0-cag04-px

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








