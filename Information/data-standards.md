## Data Inventory Standards



### Datasets:

In total, 18 items, 6 csv files for each year, 2017, 2018 and 2020 respectively.



* Madrid:

  * `ArboladoParquesHistoricoSingularesForestales_YYYY`

    * | Original variable name | New variable name | Description                                             | Type   | Use                |
      | ---------------------- | ----------------- | ------------------------------------------------------- | ------ | ------------------ |
      | PARQUE                 | park              | The unique ID name of the park on which tree is located | string | To locate the tree |
      | ESPECIE                | scientific_name   | Botanical name for the dominant specie                  | string | To group by taxon  |
      | UNIDADES YEAR          | count             | Number of tree from same type                           | int    | To count/sum       |

  * `ArboladoZonasVerdesDistritosCalles_YYYY`

    * | Original variable name | New variable name     | Description                                                  | Type   | Use                       |
      | ---------------------- | --------------------- | ------------------------------------------------------------ | ------ | ------------------------- |
      | Nombre_distrito        | district_name         | The unique name of the district on which tree is located     | string | To locate the tree        |
      | Num_distrito           | district_name         | The unique ID number of the district on which tree is located | string | To locate the tree        |
      | NOMBRE_ESPECIE         | scientific_name       | Botanical name for the dominant specie                       | string | To group by taxon         |
      | UNIDADES YEAR          | count                 | Number of tree from same type                                | int    | To count/sum              |
      | Total                  | subTotalCountDistrict | Total amount of tree in each district within a city          | int    | To count/agg per district |

  * `Estado_arbolado_ParquesHistoricoSingularesForestales_YYYY`

    * | Original variable name           | New variable name | Description                                                  | Type   | Use                            |
      | -------------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------------------ |
      | PARQUE                           | park_name         | The unique name of the park on which tree is located         | string | To locate the tree             |
      | Altura Promedio (m)              | avgTreeHt         | Average height (m) of all trees in a Park. Calculated as distance from ground level to three top | int    | for growth curve or change     |
      | Perimetro Promedio (cm)          | avgTreePerim      | Average circumference of all trees in a Park. Diameter * Pi  | int    | Phenology/allometric equations |
      | Recién Plantado y no consolidado | n_ageNew          | Number of trees which age is 1 to 5 years                    | int    | Phenology/allometric equations |
      | Joven                            | n_ageJuvenile     | Num of trees in juvenile stage                               | int    |                                |
      | Maduro                           | n_ageAdult        | Num of trees Achieved max. Optimal development               | int    |                                |
      | Viejo                            | n_ageOld          | Num of trees deprecated age stage                            | int    |                                |
      | Otros                            | n_others          | Number of trees death and others                             | int    |                                |
      | Total General                    | subTotalCountPark | Total amount of trees in each park within a city             | int    | To count/agg per district      |
      | Total                            | totalCountPark    | Total amount of tree in all parks within a city              | int    | To count/agg the whole city    |

  * `EstadoZonasVerdesDistritosCalles_YYYY`

    * | Original variable name                   | New variable name     | Description                                                  | Type   | Use                            |
      | ---------------------------------------- | --------------------- | ------------------------------------------------------------ | ------ | ------------------------------ |
      | NOMBRE DISTRITO                          | area_name             | Name of the area/district on which tree is located           | string | To locate the park             |
      | Num_DISTRITO                             | area_code             | The unique ID name of the park on which tree is located      | int    |                                |
      | Recién Plantado y no consolidado (RPyNC) | n_ageNew              | Number of trees which age is 1 to 5 years                    | int    | Phenology/allometric equations |
      | Altura Media (Hmedia)_RRLyNC             | avgTreeHt_New         |                                                              |        |                                |
      | Joven (J)                                | n_ageJuvenile         | Num of trees in juvenile stage                               | int    |                                |
      | Hmedia_J                                 | avgTreeHt_Juvenile    | Average height of all J trees in a Park. Calculated as distance from ground level to three top (m) | int    | for growth curve or change     |
      | Maduro (M)                               | n_ageAdult            | Num of trees Achieved max. Optimal development               | int    |                                |
      | Hmedia_M                                 | avgTreeHt_Adult       | Average height of all M trees in a Park. Calculated as distance from ground level to three top | int    | for growth curve or change     |
      | Viejo (V)                                | n_ageOld              | Num of trees deprecated age stage                            | int    |                                |
      | HMedia_V                                 | avgTreeHt_Juvenile    | Average height of all J trees in a Park. Calculated as distance from ground level to three top | int    | for growth curve or change     |
      | Otros                                    | n_others              | Number of trees death and others                             | int    |                                |
      | Hmedia_O                                 | avgTreeHt_Others      | Average height of all O trees in a Park. Calculated as distance from ground level to three top | int    | for growth curve or change     |
      | Total General                            | subTotalCountDistrict | Total amount of trees in each district within a city         | int    | To count/agg per district      |
  
  * `MasasParquesHistoricoSingularesForestales_YYYY`
  
  * * | Original variable name       | New variable name | Description                                                  | Type   | Use                       |
      | ---------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------------- |
      | PARQUE                       | park_name         | The unique name of the park on which tree is located         | string | To locate the tree        |
      | ESPECIE PREDOMINANTE         | scientific_name   | Botanical name for the dominant specie                       | string | To group by taxon         |
      | UNIDADES YEAR                | count             | Number of tree from same type                                | int    | To count/sum              |
      | Total General                | subTotalCountPark | Total amount of trees in each park within a city             | int    | To count/agg per district |
      | SUPERFICIE OCUPADA (m2)      | surfaceArea       | Estimated using density of each mass of all trees in each park within a city (m2) | float  |                           |
      | Superficie (ha)              | surface           | Calculated area equal to a squared 100 m sides (h)           | float  |                           |
      | Superficie TOTAL Parque (ha) | surfacePark (h)   | Surface of the total park                                    | float  |                           |
  
  * `MasasZonasVerdesDistritosCalles_YYYY`
  
  * * | Original variable name       | New variable name | Description                                                  | Type   | Use                |
      | ---------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------ |
      | Nombre_distrito              | district_name     | The unique name of the district on which tree is located     | string | To locate the tree |
      | Num_distrito                 | district_name     | The unique ID number of the district on which tree is located | string | To locate the tree |
      | NOMBRE_ESPECIE               | scientific_name   | Botanical name for the dominant specie                       | string | To group by taxon  |
      | Unidades YEAR                | count             | Number of tree from same type                                | int    | To count/sum       |
      | SUPERFICIE OCUPADA (m2)      | SurfaceArea       | Estimated using density of each mass of all trees in each district within a city (m2) | float  |                    |
      | Superficie (ha)              | Surface           | Calculated area equal to a squared 100 m sides (h)           | float  |                    |
      | Superficie TOTAL Parque (ha) | surfacePark (h)   | Surface of the total park                                    | float  |                    |



---

### District Level



---

### Park Level



---

### Specie Level
