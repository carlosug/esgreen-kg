### Semantic model figure

This module describes the data elements related to [tree inventory dataset](https://github.com/carlosug/opengov-kg/blob/main/etl/data/inputs/preprocessing). It covers the ESGREEN level of Arbolado Zonas Verdes Distritos y Calles. The data specification can e found on the Open Data Madrid Platform at this [link](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=0101507f09436610VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default).

<p align="center">
    <a href="../images/arbolado_2.png" target="_blank">
        <img src="../images/arbolado_2.png">
    </a>
</p>

***

### Example RDF (turtle):

```ttl
@prefix : <http://purl.org/ejp-rd/cde/v020/example-rdf/> .
@prefix obo: <http://purl.obolibrary.org/obo/> . 
@prefix sio: <http://semanticscience.org/resource/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix wiki: <http://en.wikipedia.org/wiki/> .
@prefix schema: <http://schema.org/>.


:distrito_ a schema:AdministrativeArea ;
    sio:similarTo sio:Township ;
    sio:isLocatedIn "Madrid"^^xsd:string ;
    sio:HasValue "Moratalaz"^^xsd:string ;
    sio:contains :collectionOfTrees ;
    # sio:collection  :collectionOfEspecies ;
    # sio:contains :especie ;
    # sio:hasMember :especie_name ;
    sio:hasAttribute :geo_ .


# geolocation for district
:geo_ a sio:GeographicPosition ;
    sio:hasAttribute :latitude_ ;
    sio:hasAttribute :longitude_ ;
    sio:hasAttribute :postal_code_ .

:latitude_ a sio:Latitude ;
    sio:HasValue "34.5"^^xsd:float .

:longitude_ a sio:Longitude ;    
    sio:HasValue "123"^^xsd:float .
    
:postal_code_ a sio:PostalCode ;
    sio:HasValue "20067"^^xsd:integer .


:collectionOfTrees a sio:collection ;
    sio:HasValue "Moratalaz-Populus_nigra"^^xsd:string ;
    sio:hasAttribute :unidades_ ;
    sio:IsRealizedIn :count_process_ ;
    sio:hasMember :especie_ .

:especie_ a sio:BiologicalEntity ;
# :especie a sio:Object .
    sio:hasAttribute :identifier_ ;
    sio:label :especie_name_ ;
    sio:equivalentTo wiki:_especie_name_ ;
    sio:isPartOf :collectionOfTrees .

:identifier_ a sio:Identifier ; # from external dataset 
    sio:denotes :especie_name_ ;
    sio:HasValue "gbif_000008"^^xsd:string .

:especie_name_ a sio:ScientificName ;
    sio:HasValue "Populus_nigra"^^xsd:string .

:count_process_ a sio:Process, sio:DataCollection ;
    sio:label "count measuring process"^^xsd:string ;
    sio:hasOutput :count_output_ .

:count_output_ a sio:InformationContentEntity ;
    sio:refersTo :unidades_ .

:unidades_ a sio:MemberCount ;
    sio:hasValue "35"^^xsd:integer ;
    sio:hasUnit obo:UO_0000189 ;
    sio:measuredAt "2021"^^xsd:date .

```

***

### Data Description


| Original variable name | New variable name     | Description                                                  | Type   | Use                       | SIO Term | Other Term |
| ---------------------- | --------------------- | ------------------------------------------------------------ | ------ | ------------------------- | -------- | ---------  |
| Nombre_distrito        | district_name         | The unique name of the district on which tree is located     | `string` | To locate the tree        | [SpatialRegion](https://vemonet.github.io/semanticscience/browse/class-siospatialregion.html) | |
| Num_distrito           | district_name         | The unique ID number of the district on which tree is located | `string` | No use        | | |
| NOMBRE_ESPECIE         | scientific_name       | Botanical name for the dominant specie                       | `string` | To group by taxon         | [MaterialEntity](https://vemonet.github.io/semanticscience/browse/class-siomaterialentity.html) | Specie |
| UNIDADES YEAR          | count                 | Number of tree from same type                                | `int`    | To count/sum              |[MemberCount](https://vemonet.github.io/semanticscience/browse/class-siomembercount.html)|
| Total                  | subTotalCountDistrict | Total amount of tree in each district within a city          | `int`    | No use | | |


### Mapping:
[Python Script](https://github.com/carlosug/opengov-kg/blob/main/etl/generate_rdf2.py)
### Output:
[RDF File](https://github.com/carlosug/opengov-kg/blob/main/etl/outputs/rdflib-output2.ttl)

### CHALLENGES AND TODO:
* Remove unnecessary rows as total, num district and aggregate values.
* 2017 has to be converted into csv file.
* All entities uses SIO schema but the issue will be to map each entity with global identifier within biodiversity database (e.g. wikidata API such https://www.wikidata.org/w/api.php?action=wbsearchentities&search=pinus&language=en or https://www.gbif.org/species/2684241).
* Still data has to be cleaned e.g. extra text in some rows, even if character latin has been removed previously.
* Inconsistency file and variable names.
* Georeferencing still has to happen.
* District a Spatial region or Site SIO class.
