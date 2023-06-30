import pandas as pd
import userdata

## Para efectos de este algoritmo, voy a suponer que tenemos la data ("userdata") de nuestra Ecommerce que corresponde a los datos de usuario.

conn = userdata.connect(host="",user="",password="")

## Vamos a crear una consulta en nuestra base de datos que corresponde a los usuarios que han realizado una compra en nuestra Ecommerce y que tienen como status: devolucion, del producto.

consulta = "SELECT * FROM Usuario WHERE status = 'devolucion'"

## utilizo la biblioteca de pandas para crear un sub conjunto con la data de la consulta.

sub_set = pd.read_sql_query(consulta, conn)




