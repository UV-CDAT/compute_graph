# compute_graph

Data analysis generally involves taking some source data and performing some series of operations upon it until you have reached your desired output. This library provides tools to generate a representation of that process; if you generate nodes and link them together, you will be able to derive the series of nodes necessary to recreate any individual node, by tracing the operations back to the original data. This allows complex data products to be serialized in a simple format, for easy transfer over the wire, and recomputed at the other end.