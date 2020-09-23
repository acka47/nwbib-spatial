import rdflib

g = rdflib.Graph()

g.parse("nwbib-spatial.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    CONSTRUCT { ?broad skos:narrower ?narrow }
       WHERE {
           { ?narrow skos:broader ?broad }
       }""")

with open("narrower.ttl", "w") as output:
            output.write(qres.serialize(format='turtle'))