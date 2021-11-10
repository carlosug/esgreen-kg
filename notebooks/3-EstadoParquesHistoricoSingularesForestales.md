### Semantic model figure

This module describes the data elements related to tree inventory dataset.


<p align="center">
    <a href="../images/arbolado_3.png" target="_blank">
        <img src="../images/arbolado_3.png">
    </a>
</p>

***

### Example RDF (turtle):

```ttl

@prefix esgreen: <https://w3id.org/esgreen/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix obo: <http://purl.obolibratory.org/obo> .


esgreen:capricho_de_la_alameda_de_osuna a sio:site ;
    rdfs:label "capricho_de_la_alameda_de_osuna"^^xsd:string .

esgreen:collection-of-trees-locatedin-capricho_de_la_alameda_de_osuna a sio:Collection .

esgreen:collection-of-trees-locatedin-capricho_de_la_alameda_de_osuna-life-Status-joven a sio:LifeStatus,
        sio:MemberCount ;
    sio:hasQuality "joven" ;
    sio:hasUnit obo:UO_0000189 ;
    sio:hasValue 558.0,
        668.0 ;
    sio:measuredAt "2018-01-01"^^xsd:date,
        "2019-01-01"^^xsd:date .

esgreen:collection-of-trees-locatedin-capricho_de_la_alameda_de_osuna-life-Status-joven a sio:DimensionalQuantity ;
    sio:hasQuality "joven" ;
    sio:hasUnit obo:UO_0000007 ;
    sio:hasValue "40.0"^^xsd:float ;
    sio:measuredAt "2017-01-01"^^xsd:date .

```

***

### Data Description
    
  
| Original variable name           | New variable name | Description                                                  | Type   | Use                            | SIO Term | Other Term |
| -------------------------------- | ----------------- | ------------------------------------------------------------ | ------ | ------------------------------ | ------- | ---------- |
| PARQUE                           | park_name         | The unique name of the park on which tree is located         | ``string`` | To locate the tree             |   |  |
| Altura Promedio (m)              | avgTreeHt         | Average height (m) of all trees in a Park. Calculated as distance from ground level to three top | `int`    | for growth curve or change     | | |
| Perimetro Promedio (cm)          | avgTreePerim      | Average circumference of all trees in a Park. Diameter * Pi  | ``int``    | Phenology/allometric equations | | |
| Recién Plantado y no consolidado | n_ageNew          | Number of trees which age is 1 to 5 years                    | ``int``    | Phenology/allometric equations | | |
| Joven                            | n_ageJuvenile     | Num of trees in juvenile stage                               | `int`    |                                | | |
| Maduro                           | n_ageAdult        | Num of trees Achieved max. Optimal development               | `int`    |                                | | |
| Viejo                            | n_ageOld          | Num of trees deprecated age stage                            | `int`    |                                | | |
| Otros                            | n_others          | Number of trees death and others                             | `int`    |                                | | |
| Total General                    | subTotalCountPark | Total amount of trees in each park within a city             | `int`    | To count/agg per district      | | |
| Total                            | totalCountPark    | Total amount of tree in all parks within a city              | `int`    | To count/agg the whole city    | | |


### Mapping:
[Python Script](https://github.com/carlosug/opengov-kg/blob/main/etl/generate_rdf3.py)
### Output:
[RDF File](https://github.com/carlosug/opengov-kg/blob/main/etl/outputs/rdflib-output3.ttl)

### CHALLENGES AND TODO:
* Data cleaning: remove latin character and others _(*&(&#))_, unnecessary rows as total and aggregate values. [see data-cleaning.py](https://github.com/carlosug/opengov-kg/blob/main/etl/data-cleaning.py)
* All entities uses SIO schema but **specie** is not clear yet.
* The issue will be to map each entity with global identifier within biodiversity database (e.g. wikidata API such https://www.wikidata.org/w/api.php?action=wbsearchentities&search=pinus&language=en or https://www.gbif.org/species/2684241). [see data-argumentation.py](https://github.com/carlosug/opengov-kg/blob/main/etl/data-argumentation.py)
* Inconsistency file and variable names and therefore harmonization of the entity names.
* **Data Argumentation with georeferencing parks and taxo, family and other related terms from scientificname.** [see unique-species.py](https://github.com/carlosug/opengov-kg/blob/main/etl/unique-species.py)
