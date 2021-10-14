# dir
cd data

yarrrml-parser -i ../mapping-esgreen.yarrr.yml -o mapping-esgreen.rml.ttl

java -jar rmlmapper.jar -m mapping-esgreen.rml.ttl -o output-rdf.ttl -s turtle

cd ..

# yarrrml-parser -i mapping-esgreen.yarrr.yml -o mapping-esgreen.rml.ttl

# java -jar rmlmapper.jar -m data/mapping-esgreen.rml.ttl -o data/output-rdf.ttl -s turtle

# Move-Item -Path mapping-esgreen.rml.ttl -Destination data\mapping-esgreen.rml.ttl

# java -jar rmlmapper.jar -m data/mapping-esgreen.rml.ttl -o data/output-rdf.ttl -s turtle

# java -jar rmlmapper.jar -m mapping-esgreen.rml.ttl -o output-rdf.ttl -s turtle

# yarrrml-parser -i mapping-small.yarrr.yml -o mapping-small.rml.ttl

# yarrrml-parser -i ../etl/mapping-small.yarrr.yml -o mapping-small.rml.ttl