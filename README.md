# Knowledge Graph for Open Government Data - Case of ESGREEN
🌲 A RDF knowledge graph for green spaces infrastructure (trees, parkland, green areas) data of a city that are relevant for [Open City Project](https://github.com/CiudadesAbiertas). 

> To make **BIODIVERSITY** data Interoperable (the <b>I</b> in FAIR).

## SPARQL Research questions
* 1. **city center** most abundant organisms.
* 2. **outside** city center.
* 3. **areas** with least and most diverse species  diversity (Shannon Index).
* 4. **Diversity Index**:  we can measure how evenly diversity exists in your tree inventory.
---

## Inputs
A total of 18 datasets originally from [Madrid Green Data Space](https://mgds.oeg.fi.upm.es/datasets.html) are used to generate the Ontology. These datasets consist of measures (e.g., number of trees) and dimensions describing the measures (e.g., regions)

- [Raw Datasets](https://github.com/carlosug/opengov-kg/tree/main/etl/data/inputs)
- [Clean Dataset](https://github.com/carlosug/opengov-kg/tree/main/etl/data/inputs/preprocessing)

### Other external datasets:
We will map each specie with global identifier within biodiversity database (e.g. [wikidata API](https://www.wikidata.org/w/api.php?action=wbsearchentities&search=pinus&language=en) or [Global Biodiversity Information Facility](https://www.gbif.org/species/2684241). This will allow us to get further information about species such kingdom, genus name, family name and global identifier. [See data-argumentation.py](https://github.com/carlosug/opengov-kg/blob/main/etl/data-argumentation.py)


- [Unique Tree data](https://github.com/carlosug/opengov-kg/blob/main/etl/data/inputs/preprocessing/normalized.csv)
    + Geographical location
    + Scientific or species name
    + Genus name
    + Family name
    + Global Identifier

[Open Tree of Life](https://opentreeoflife.github.io/) or [Encyclopedia of Life](https://eol.org/) are some other free and open biodiversity data.

## Data Model
Concepts and properties are annotated with the [Semanticscience  Integrated Ontology](https://bioportal.bioontology.org/ontologies/SIO/).

The figure below gives an overview of upper level concepts and properties used in our data model.

<p align="center"> 
	<img src="images/diagram-complex2.png"> 
</p> 

You can browse different **ESGREEN modules** by visiting the links below:

* [Arbolado Parques Historico y Singulares](notebooks/1-ArboladoParquesHistoricosSingularesForestales.md)
* [Arbolado Zonas Verdes Distritos Calles](notebooks/2-ArboladoZonasVerdesDistritosCalles.md)
* [Estado Parques Historico y Singulares](notebooks/3-EstadoParquesHistoricoSingularesForestales.md)
* [Estado Zonas Verdes Distritos Calles](notebooks/4-EstadoZonasVerdesDistritosCalles.md)
* [Masas Parques Historico Singulares Forestales](notebooks/5-MasasParquesHistoricoSingularesForestales.md)
* [Masas Zonas Verdes Distritos Calles](notebooks/6-MasasZonasVerdesDistritosCalles.md)

We have used this [API](http://ejprd.fair-dtls.surf-hosted.nl:5000/) to generate documentation related to ESGREEN modules.


---
## License

**Copyright (C) 2021**

MIT License 

---
