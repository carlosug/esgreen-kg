## Data Inventory Standards



### Datasets:

In total, 18 items, 6 csv files for each year, 2017, 2018 and 2020 respectively.

* Madrid:

  * `ArboladoParquesHistoricoSingularesForestales_YYYY`

    * | Original variable name | New variable name | Description                                             | Type   | Use                |
      | ---------------------- | ----------------- | ------------------------------------------------------- | ------ | ------------------ |
      | PARQUE                 | park              | The unique ID name of the park on which tree is located | `string` | To locate the tree |
      | ESPECIE                | scientific_name   | Botanical name for the dominant specie                  | `string` | To group by taxon  |
      | UNIDADES YEAR          | count             | Number of tree from same type                           | `int`    | To count/sum       |
      
      ```ttl
      # ArboladoParquesHistoricosSingularesyForestalesYYYY.csv
      ######## Turtle syntax ########
      :Jardines-del-buen-retiro rdf:type :Park .
      Park sio: isLocatedIn District .
      :Jardines-del-buen-retiro sio:contains :collection-of-aesculus-hippocastanum .
      :collection-of-aesculus-hippocastanum a sio:Collection .
      :collection-of-aesculus-hippocastanum sio:hasMember :aesculus-hippocastanum .
      :aesculus-hippocastanum a :habitatSpecies.
      :aesculus-hippocastanum sio: has-unique-indentifier :EUNIS-code .
      :EUNIS-Code sio:has-value "G3.74" .
      :collection-of-aesculus-hippocastanum sio:has-attribute :ah_count .
      :cph_count a sio:memberCount .
      :cph_count sio:has-value "6377"
       
      ```
      
      
  
  * `ArboladoZonasVerdesDistritosCalles_YYYY`
  
    * | Original variable name | New variable name     | Description                                                  | Type   | Use                       |
      | ---------------------- | --------------------- | ------------------------------------------------------------ | ------ | ------------------------- |
      | Nombre_distrito        | district_name         | The unique name of the district on which tree is located     | ``string`` | To locate the tree        |
      | Num_distrito           | district_name         | The unique ID number of the district on which tree is located | `string` | No use        |
      | NOMBRE_ESPECIE         | scientific_name       | Botanical name for the dominant specie                       | `string` | To group by taxon         |
      | UNIDADES YEAR          | count                 | Number of tree from same type                                | `int`    | To count/sum              |
      | Total                  | subTotalCountDistrict | Total amount of tree in each district within a city          | `int`    | No use |

  * Expected triples:
```rdf

######## Turtle syntax ########

:distrito rdf:type sio:Site .
:distrito sio:isLocatedIn Nombre_distrito .
:distrito sio:contains :collection-of-especie .

:collection-of-especie rdf:type sio:Collection .
:collection-of-especie sio:hasMember :especie .
:collection-of-especie sio:has-attribute :unidades .
:unidades a sio:memberCount .
:unidades sio:has-value "unidades_year" .
:unidades sio:has-unit obo:UO_0000189 .
:unidades sio.measuredAt, Literal(datatype=XSD.date)))

:especie a :habitatSpecies.
:especie sio:UniqueIdentifier :ESPECIE-code .
:especie RDFS.label :ESPECIE .
:especie RDFS.seeAlso :WIKI-ESPECIE .
```
  
  * `Estado_arbolado_ParquesHistoricoSingularesForestales_YYYY`
  
    * | Original variable name           | New variable name | Description                                                  | Type   | Use                            |
      | -------------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------------------ |
      | PARQUE                           | park_name         | The unique name of the park on which tree is located         | ``string`` | To locate the tree             |
      | Altura Promedio (m)              | avgTreeHt         | Average height (m) of all trees in a Park. Calculated as distance from ground level to three top | `int`    | for growth curve or change     |
      | Perimetro Promedio (cm)          | avgTreePerim      | Average circumference of all trees in a Park. Diameter * Pi  | ``int``    | Phenology/allometric equations |
      | Recién Plantado y no consolidado | n_ageNew          | Number of trees which age is 1 to 5 years                    | ``int``    | Phenology/allometric equations |
      | Joven                            | n_ageJuvenile     | Num of trees in juvenile stage                               | `int`    |                                |
      | Maduro                           | n_ageAdult        | Num of trees Achieved max. Optimal development               | `int`    |                                |
      | Viejo                            | n_ageOld          | Num of trees deprecated age stage                            | `int`    |                                |
      | Otros                            | n_others          | Number of trees death and others                             | `int`    |                                |
      | Total General                    | subTotalCountPark | Total amount of trees in each park within a city             | `int`    | To count/agg per district      |
      | Total                            | totalCountPark    | Total amount of tree in all parks within a city              | `int`    | To count/agg the whole city    |
      
* Expected triples:


######## Turtle syntax ########
```ttl
:PARQUE rdf:type sio:Site .
:PARQUE sio:contains :collection-of-ESPECIE-STATUS .
:collection-of-ESPECIE-STATUS rdf:type sio:Collection .
:collection-of-trees sio:hasAttribute :age .
:age a :subClassOf sio:dimensional-quantity .
:age sio: has-label :lifeCycleInfo .
:lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
:Recien plantado y no consolidado a sio:memberCount .
:membercount sio:has-value "Recien plantado y no consolidado" .
:lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
:Recien plantado y no consolidado a sio:memberCount .
:membercount sio:has-value "Recien plantado y no consolidado" .
:lifeCycleInfo sio:has-label "Joven" .
:Joven a sio:memberCount .
:membercount sio:has-value "Joven" .  
:collection-of-trees sio:hasAttribute : Maduro .
:Maduro a sio:mean .
:Maduro sio: has-value "Maduro" .
:collection-of-trees sio:hasAttribute : Viejo .
:Viejo a sio:mean .
:Viejo sio: has-value "Viejo" .
      
  
  * `EstadoZonasVerdesDistritosCalles_YYYY`
  
    * | Original variable name                   | New variable name     | Description                                                  | Type   | Use                            |
      | ---------------------------------------- | --------------------- | ------------------------------------------------------------ | ------ | ------------------------------ |
      | NOMBRE DISTRITO                          | area_name             | Name of the area/district on which tree is located           | `string` | To locate the park             |
      | Num_DISTRITO                             | area_code             | The unique ID name of the park on which tree is located      | `int`    |                                |
      | Recién Plantado y no consolidado (RPyNC) | n_ageNew              | Number of trees which age is 1 to 5 years                    | `int`    | Phenology/allometric equations |
      | Altura Media (Hmedia)_RRLyNC             | avgTreeHt_New         |                                                              |        |                                |
      | Joven (J)                                | n_ageJuvenile         | Num of trees in juvenile stage                               | `int`    |                                |
      | Hmedia_J                                 | avgTreeHt_Juvenile    | Average height of all J trees in a Park. Calculated as distance from ground level to three top (m) | `int`    | for growth curve or change     |
      | Maduro (M)                               | n_ageAdult            | Num of trees Achieved max. Optimal development               | `int`    |                                |
      | Hmedia_M                                 | avgTreeHt_Adult       | Average height of all M trees in a Park. Calculated as distance from ground level to three top | `int`    | for growth curve or change     |
      | Viejo (V)                                | n_ageOld              | Num of trees deprecated age stage                            | `int`    |                                |
      | HMedia_V                                 | avgTreeHt_Juvenile    | Average height of all J trees in a Park. Calculated as distance from ground level to three top | `int`    | for growth curve or change     |
      | Otros                                    | n_others              | Number of trees death and others                             | `int`    |                                |
      | Hmedia_O                                 | avgTreeHt_Others      | Average height of all O trees in a Park. Calculated as distance from ground level to three top | `int`    | for growth curve or change     |
      | Total General                            | subTotalCountDistrict | Total amount of trees in each district within a city         | `int`    | To count/agg per district      |
      
      ```ttl
      # EstadoZonasVerdesDistritosCalles_YYYY.csv
      ######## Turtle syntax ########
      
      :Barajas rdf:type :District .
      District sio: similarTo :township .
      :barajas sio:contains :collection-of-trees .
      :collection-of-trees a sio:Collection .
      :collection-of-trees sio:hasAttribute :age .
      :age a :subClassOf sio:dimensional-quantity.
      :age sio: has-label :lifeCycleInfo .
      :lifeCycleInfo sio:has-value "New" .
      :lifeCycleInfo a sio:memberCount .
      :cph_count sio:has-value "1039" .
      :collection-of-trees sio:hasAttribute : averageHeight-barajas .  
      :averageHeight-barajas a sio:mean .
      :averageHeight-barajas sio: has-value "4.19"
      ```
      
      
  
  * `MasasParquesHistoricoSingularesForestales_YYYY`
  
  * * | Original variable name       | New variable name | Description                                                  | Type   | Use                       |
      | ---------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------------- |
      | PARQUE                       | park_name         | The unique name of the park on which tree is located         | `string` | To locate the tree        |
      | ESPECIE PREDOMINANTE         | scientific_name   | Botanical name for the dominant specie                       | `string` | To group by taxon         |
      | UNIDADES YEAR                | count             | Number of tree from same type                                | `int`    | To count/sum              |
      | Total General                | subTotalCountPark | Total amount of trees in each park within a city             | `int`    | To count/agg per district |
      | SUPERFICIE OCUPADA (m2)      | surfaceArea       | Estimated using density of each mass of all trees in each park within a city (m2) | `float`  |                           |
      | Superficie (ha)              | surface           | Calculated area equal to a squared 100 m sides (h)           | `float`  |                           |
      | Superficie TOTAL Parque (ha) | surfacePark (h)   | Surface of the total park                                    | `float`  |                           |
  
    ```ttl
    # MasasParquesHistoricoSingularesForestales_YYYY.csv
    ######## Turtle syntax ########
    
    :Parques-Madrid-Rio rdf:type :Park .
    Park sio: isLocatedIn District .
    :Parques-Madrid-Rio sio:contains :collection-of-pinus-alepensis .
    :collection-of-pinus-alepensis a sio:Collection .
    :collection-of-pinus-alepensis sio:hasMember :pinus-alepensis .
    :pinus-alepensis a :habitatSpecies.
    :pinus-alepensis sio: has-unique-indentifier :EUNIS-code .
    :EUNIS-Code sio:has-value "G3.74" .
    :collection-of-pinus-alepensis sio:has-attribute :parques-madrid-rio_sa .
    ::parques-madrid-rio_sa a sio:SurfaceArea.
    ::parques-madrid-rio_sa sio:has-value "92970.17" .
    :collection-of-pinus-alepensis sio:has-attribute :parques-madrid-rio_count .
    ::parques-madrid-rio_count a sio:memberCount.
    ::parques-madrid-rio_count sio:has-value "2811" .
     
    ```
    
    
    
  * `MasasZonasVerdesDistritosCalles_YYYY`
  
  * * | Original variable name       | New variable name | Description                                                  | Type   | Use                |
      | ---------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------ |
      | Nombre_distrito              | district_name     | The unique name of the district on which tree is located     | `string` | To locate the tree |
      | Num_distrito                 | district_name     | The unique ID number of the district on which tree is located | `string` | To locate the tree |
      | NOMBRE_ESPECIE               | scientific_name   | Botanical name for the dominant specie                       | `string` | To group by taxon  |
      | Unidades YEAR                | count             | Number of tree from same type                                | `int`    | To count/sum       |
      | SUPERFICIE OCUPADA (m2)      | SurfaceArea       | Estimated using density of each mass of all trees in each district within a city (m2) | `float`  |                    |
      | Superficie (ha)              | Surface           | Calculated area equal to a squared 100 m sides (h)           | `float`  |                    |
      | Superficie TOTAL Parque (ha) | surfacePark (h)   | Surface of the total park                                    | `float`  |                    |



```ttl
# MasasZonasVerdesDistritosCalles_YYYY.csv
######## Turtle syntax ########

:arganzuela rdf:type :District .
District sio: similarTo :township .
:barajas sio:contains :collection-of-pinus-halepensis .
:collection-of-pinus-halepensis a sio:Collection .
:collection-of-pinus-halepensis sio:hasMember :Pinus-halepensis .
:pinus-halepensis a :habitatSpecies.
:pinus-halepensis sio: has-unique-indentifier :EUNIS-code .
:EUNIS-Code sio:has-value "G3.74" .
:collection-of-pinus-halepensis sio:has-attribute :cph_count .
:cph_count a sio:memberCount .
:cph_count sio:has-value "6973"
 
```

