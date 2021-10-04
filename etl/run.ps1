yarrrml-parser -i mapping-esgreen.yarrr.yml -o data/mapping-esgreen.rml.ttl
java -jar rmlmapper.jar -m data/mapping-esgreen.rml.ttl -o data/output-rdf.ttl -s turtle