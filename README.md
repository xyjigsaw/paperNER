# paperNER

![](https://img.shields.io/badge/Status-Developing-brightgreen.svg)

Named Entity Recognition for Paper(PDF)

# Extractor/Algorithm

BERT + BiLSTM + CRF

BERT is based on [SCIBERT](https://github.com/allenai/scibert)

## Files

- main.py: Users input pdf file path then it will generate NER outputs.
- toolkit
  - pdf_parser: pdf2xml
- save: BERT model for NER(will be updated soon)
 
## Requirements (python packages)

- [kashgari](https://github.com/BrikerMan/Kashgari)
- tensorflow

Versions need to be compatible with each other.

```bash
pip install kashgari
pip install tensorflow
```

## preview
```bash
"C:\Program Files\Python36\python.exe" C:/Users/xy644/Desktop/scibert-project/paperNER/main.py
input file path: ELG.pdf
PaperXML.get_rf Error: list index out of range
PaperXML.get_rf Error: list index out of range
--------------------------------
text: Therefore, the discovery of such evolutionary patterns among events are of great value for event prediction, decision-making and scenario design of dialog systems.
labels [{'entity': 'OtherScientificTerm', 'start': 5, 'end': 6, 'value': 'evolutionary patterns'}, {'entity': 'Task', 'start': 14, 'end': 16, 'value': 'event prediction, decision-making'}]
	value: evolutionary patterns 	 OtherScientificTerm
	value: event prediction, decision-making 	 Task
--------------------------------
text: However, conventional knowledge graph mainly focuses on the entities and their relations, which neglects the real world events.
labels [{'entity': 'OtherScientificTerm', 'start': 2, 'end': 2, 'value': 'knowledge'}, {'entity': 'Method', 'start': 3, 'end': 3, 'value': 'graph'}]
	value: knowledge 	 OtherScientificTerm
	value: graph 	 Method
--------------------------------
text: In this paper, we present a novel type of knowledge base — Event Logic Graph (ELG), which can reveal evolutionary patterns and development logics of real world events.
labels [{'entity': 'Method', 'start': 9, 'end': 10, 'value': 'knowledge base'}, {'entity': 'Method', 'start': 12, 'end': 15, 'value': 'Event Logic Graph (ELG),'}]
	value: knowledge base 	 Method
	value: Event Logic Graph (ELG), 	 Method
--------------------------------
text: Specifically, ELG is a directed cyclic graph, whose nodes are events, and edges stand for the sequential, causal, conditional or hypernym-hyponym (“is-a”) relations between events.
labels [{'entity': 'Method', 'start': 1, 'end': 1, 'value': 'ELG'}, {'entity': 'Method', 'start': 4, 'end': 6, 'value': 'directed cyclic graph,'}, {'entity': 'OtherScientificTerm', 'start': 8, 'end': 8, 'value': 'nodes'}, {'entity': 'OtherScientificTerm', 'start': 10, 'end': 10, 'value': 'events,'}, {'entity': 'OtherScientificTerm', 'start': 12, 'end': 12, 'value': 'edges'}, {'entity': 'OtherScientificTerm', 'start': 16, 'end': 18, 'value': 'sequential, causal, conditional'}]
	value: ELG 	 Method
	value: directed cyclic graph, 	 Method
	value: nodes 	 OtherScientificTerm
	value: events, 	 OtherScientificTerm
	value: edges 	 OtherScientificTerm
	value: sequential, causal, conditional 	 OtherScientificTerm
--------------------------------
text: We constructed two domain ELG: financial domain ELG, which consists of more than 1.
labels [{'entity': 'Material', 'start': 3, 'end': 3, 'value': 'domain'}, {'entity': 'Material', 'start': 5, 'end': 6, 'value': 'financial domain'}]
	value: domain 	 Material
	value: financial domain 	 Material
--------------------------------
text: 5 million of event nodes and more than 1.
labels [{'entity': 'OtherScientificTerm', 'start': 3, 'end': 4, 'value': 'event nodes'}]
	value: event nodes 	 OtherScientificTerm
--------------------------------
text: 8 million of directed edges, and travel domain ELG, which consists of about 30 thousand of event nodes and more than 234 thousand of directed edges.
labels [{'entity': 'Material', 'start': 3, 'end': 4, 'value': 'directed edges,'}, {'entity': 'Material', 'start': 6, 'end': 8, 'value': 'travel domain ELG,'}, {'entity': 'OtherScientificTerm', 'start': 16, 'end': 17, 'value': 'event nodes'}]
	value: directed edges, 	 Material
	value: travel domain ELG, 	 Material
	value: event nodes 	 OtherScientificTerm
--------------------------------
text: Experimental results show that ELG is effective for the task of script event prediction.
labels [{'entity': 'Method', 'start': 4, 'end': 4, 'value': 'ELG'}, {'entity': 'Task', 'start': 11, 'end': 12, 'value': 'script event'}, {'entity': '[PAD]', 'start': 13, 'end': 13, 'value': 'prediction.'}]
	value: ELG 	 Method
	value: script event 	 Task
	value: prediction. 	 [PAD]
--------------------------------
text: This event sequence is a common pattern for the scenario of having lunch in a restaurant.
labels [{'entity': 'OtherScientificTerm', 'start': 1, 'end': 2, 'value': 'event sequence'}, {'entity': 'OtherScientificTerm', 'start': 12, 'end': 12, 'value': 'lunch'}]
	value: event sequence 	 OtherScientificTerm
	value: lunch 	 OtherScientificTerm
--------------------------------
text: Such patterns can reveal the basic rules of event evolutions and human behaviors.
labels [{'entity': 'Generic', 'start': 1, 'end': 1, 'value': 'patterns'}, {'entity': 'Task', 'start': 8, 'end': 9, 'value': 'event evolutions'}, {'entity': 'Task', 'start': 11, 'end': 12, 'value': 'human behaviors.'}]
	value: patterns 	 Generic
	value: event evolutions 	 Task
	value: human behaviors. 	 Task
--------------------------------
text: However, traditional knowledge graph takes the entity as the research focus, and investigate the properties of entities and the relationships between entities, which lacks of event-related knowledge.
labels [{'entity': 'Method', 'start': 2, 'end': 3, 'value': 'knowledge graph'}]
	value: knowledge graph 	 Method
--------------------------------
text: In order to discover the evolutionary patterns and logics of events, we propose an eventcentric knowledge graph — Event Logic Graph (ELG) and the framework to construct ELG.
labels [{'entity': 'OtherScientificTerm', 'start': 5, 'end': 6, 'value': 'evolutionary patterns'}, {'entity': 'OtherScientificTerm', 'start': 8, 'end': 8, 'value': 'logics'}, {'entity': 'OtherScientificTerm', 'start': 10, 'end': 10, 'value': 'events,'}, {'entity': 'Method', 'start': 14, 'end': 16, 'value': 'eventcentric knowledge graph'}, {'entity': 'Method', 'start': 18, 'end': 18, 'value': 'Event'}]
	value: evolutionary patterns 	 OtherScientificTerm
	value: logics 	 OtherScientificTerm
	value: events, 	 OtherScientificTerm
	value: eventcentric knowledge graph 	 Method
	value: Event 	 Method
--------------------------------
text: ELG is a directed cyclic graph, whose nodes are events, and edges stand for the sequential (the same meaning with “temporal”), causal, conditional or hypernym-hyponym (“is-a”) relations between events.
labels [{'entity': 'OtherScientificTerm', 'start': 3, 'end': 3, 'value': 'directed'}, {'entity': 'Method', 'start': 4, 'end': 5, 'value': 'cyclic graph,'}, {'entity': 'OtherScientificTerm', 'start': 7, 'end': 7, 'value': 'nodes'}, {'entity': 'OtherScientificTerm', 'start': 9, 'end': 9, 'value': 'events,'}, {'entity': 'OtherScientificTerm', 'start': 15, 'end': 15, 'value': 'sequential'}]
	value: directed 	 OtherScientificTerm
	value: cyclic graph, 	 Method
	value: nodes 	 OtherScientificTerm
	value: events, 	 OtherScientificTerm
	value: sequential 	 OtherScientificTerm
--------------------------------
text: Essentially, ELG is an event logic knowledge base, which can reveal evolutionary patterns and development logics of real world events.
labels [{'entity': 'Method', 'start': 1, 'end': 1, 'value': 'ELG'}, {'entity': 'Method', 'start': 4, 'end': 7, 'value': 'event logic knowledge base,'}, {'entity': 'OtherScientificTerm', 'start': 11, 'end': 12, 'value': 'evolutionary patterns'}, {'entity': 'OtherScientificTerm', 'start': 14, 'end': 15, 'value': 'development logics'}]
	value: ELG 	 Method
	value: event logic knowledge base, 	 Method
	value: evolutionary patterns 	 OtherScientificTerm
	value: development logics 	 OtherScientificTerm
--------------------------------
text: In the end, we need to merge event pairs to obtain the final event logic graph by connecting semantically similar events and generalizing each specific event.
labels [{'entity': 'OtherScientificTerm', 'start': 8, 'end': 8, 'value': 'pairs'}, {'entity': 'OtherScientificTerm', 'start': 13, 'end': 15, 'value': 'event logic graph'}]
	value: pairs 	 OtherScientificTerm
	value: event logic graph 	 OtherScientificTerm
--------------------------------
text: Numerous efforts have been made to extract temporal and causal relations from texts.
labels [{'entity': 'OtherScientificTerm', 'start': 7, 'end': 10, 'value': 'temporal and causal relations'}]
	value: temporal and causal relations 	 OtherScientificTerm
--------------------------------
text: Second, we propose a promising framework to construct ELG from a largescale unstructured text corpus.
labels [{'entity': 'Generic', 'start': 5, 'end': 5, 'value': 'framework'}, {'entity': 'Method', 'start': 8, 'end': 8, 'value': 'ELG'}, {'entity': 'Material', 'start': 11, 'end': 14, 'value': 'largescale unstructured text corpus.'}]
	value: framework 	 Generic
	value: ELG 	 Method
	value: largescale unstructured text corpus. 	 Material
--------------------------------
text: Third, experimental results show that ELG is capable of improving the performances of downstream applications, such as script event prediction.
labels [{'entity': 'Method', 'start': 5, 'end': 5, 'value': 'ELG'}, {'entity': 'Task', 'start': 13, 'end': 13, 'value': 'downstream'}, {'entity': 'Generic', 'start': 14, 'end': 14, 'value': 'applications,'}, {'entity': 'OtherScientificTerm', 'start': 17, 'end': 18, 'value': 'script event'}]
	value: ELG 	 Method
	value: downstream 	 Task
	value: applications, 	 Generic
	value: script event 	 OtherScientificTerm
--------------------------------
text: ELG is a directed cyclic graph, whose nodes are events, and edges stand for the sequential, causal, conditional or hypernym-hyponym relations between events.
labels [{'entity': 'OtherScientificTerm', 'start': 3, 'end': 5, 'value': 'directed cyclic graph,'}, {'entity': 'OtherScientificTerm', 'start': 7, 'end': 7, 'value': 'nodes'}, {'entity': 'OtherScientificTerm', 'start': 9, 'end': 9, 'value': 'events,'}, {'entity': 'OtherScientificTerm', 'start': 15, 'end': 18, 'value': 'sequential, causal, conditional or'}]
	value: directed cyclic graph, 	 OtherScientificTerm
	value: nodes 	 OtherScientificTerm
	value: events, 	 OtherScientificTerm
	value: sequential, causal, conditional or 	 OtherScientificTerm
--------------------------------
text: Essentially, ELG is an event logic knowledge base, which reveals evolutionary patterns and development logics of real world events.
labels [{'entity': 'Method', 'start': 1, 'end': 1, 'value': 'ELG'}, {'entity': 'Method', 'start': 4, 'end': 7, 'value': 'event logic knowledge base,'}, {'entity': 'OtherScientificTerm', 'start': 10, 'end': 11, 'value': 'evolutionary patterns'}, {'entity': 'OtherScientificTerm', 'start': 13, 'end': 14, 'value': 'development logics'}]
	value: ELG 	 Method
	value: event logic knowledge base, 	 Method
	value: evolutionary patterns 	 OtherScientificTerm
	value: development logics 	 OtherScientificTerm
text: This kind of commonsense event evolutionary patterns are usually hidden behind human beings’ daily activities, or online user generated contents.
labels [{'entity': 'OtherScientificTerm', 'start': 3, 'end': 6, 'value': 'commonsense event evolutionary patterns'}, {'entity': 'OtherScientificTerm', 'start': 11, 'end': 11, 'value': 'human'}, {'entity': 'OtherScientificTerm', 'start': 14, 'end': 14, 'value': 'activities,'}, {'entity': 'OtherScientificTerm', 'start': 16, 'end': 17, 'value': 'online user'}]
	value: commonsense event evolutionary patterns 	 OtherScientificTerm
	value: human 	 OtherScientificTerm
	value: activities, 	 OtherScientificTerm
	value: online user 	 OtherScientificTerm
--------------------------------
text: In our definition, each event must contain a trigger word (i.
labels [{'entity': 'OtherScientificTerm', 'start': 8, 'end': 9, 'value': 'trigger word'}]
	value: trigger word 	 OtherScientificTerm
--------------------------------
text: In general, events and the degree of abstraction of an event are closely related to the scene in which the event occurred, and a single event may become too abstract to understand without the context scenario.
labels [{'entity': 'Task', 'start': 1, 'end': 1, 'value': 'general,'}, {'entity': 'OtherScientificTerm', 'start': 2, 'end': 2, 'value': 'events'}, {'entity': 'OtherScientificTerm', 'start': 7, 'end': 7, 'value': 'abstraction'}, {'entity': 'OtherScientificTerm', 'start': 10, 'end': 10, 'value': 'event'}]
	value: general, 	 Task
	value: events 	 OtherScientificTerm
	value: abstraction 	 OtherScientificTerm
	value: event 	 OtherScientificTerm
--------------------------------
text: Abstract and generalized means that we do not concern about the exact participants, location and time of an event.
labels [{'entity': 'OtherScientificTerm', 'start': 12, 'end': 13, 'value': 'participants, location'}, {'entity': 'OtherScientificTerm', 'start': 18, 'end': 18, 'value': 'event.'}]
	value: participants, location 	 OtherScientificTerm
	value: event. 	 OtherScientificTerm
--------------------------------
text: For example, (have, a hot pot) and (go to, the airport) are reasonable event tuples to represent events.
labels [{'entity': 'OtherScientificTerm', 'start': 4, 'end': 5, 'value': 'hot pot)'}, {'entity': 'OtherScientificTerm', 'start': 7, 'end': 10, 'value': '(go to, the airport)'}, {'entity': 'OtherScientificTerm', 'start': 13, 'end': 14, 'value': 'event tuples'}]
	value: hot pot) 	 OtherScientificTerm
	value: (go to, the airport) 	 OtherScientificTerm
	value: event tuples 	 OtherScientificTerm
--------------------------------
text: While (go, somewhere), (do, the things) and (eat) are unreasonable or incomplete event representations, as their semantics are too vague to be understood.
labels [{'entity': 'Method', 'start': 1, 'end': 2, 'value': '(go, somewhere),'}, {'entity': 'Method', 'start': 5, 'end': 5, 'value': 'things)'}, {'entity': 'OtherScientificTerm', 'start': 6, 'end': 7, 'value': 'and (eat)'}, {'entity': 'OtherScientificTerm', 'start': 9, 'end': 12, 'value': 'unreasonable or incomplete event'}, {'entity': 'OtherScientificTerm', 'start': 16, 'end': 16, 'value': 'semantics'}]
	value: (go, somewhere), 	 Method
	value: things) 	 Method
	value: and (eat) 	 OtherScientificTerm
	value: unreasonable or incomplete event 	 OtherScientificTerm
	value: semantics 	 OtherScientificTerm
--------------------------------
text: We have four categories of directed edges: sequential directed edges, causal directed edges, conditional directed edges and hypernym-hyponym directed edges, which indicate different relationships between events.
labels [{'entity': 'OtherScientificTerm', 'start': 5, 'end': 15, 'value': 'directed edges: sequential directed edges, causal directed edges, conditional directed edges'}, {'entity': 'OtherScientificTerm', 'start': 17, 'end': 18, 'value': 'hypernym-hyponym directed'}]
	value: directed edges: sequential directed edges, causal directed edges, conditional directed edges 	 OtherScientificTerm
	value: hypernym-hyponym directed 	 OtherScientificTerm
--------------------------------
text: The sequential relation between two events refers to their partial temporal orderings.
labels [{'entity': 'OtherScientificTerm', 'start': 1, 'end': 2, 'value': 'sequential relation'}, {'entity': 'OtherScientificTerm', 'start': 9, 'end': 11, 'value': 'partial temporal orderings.'}]
	value: sequential relation 	 OtherScientificTerm
	value: partial temporal orderings. 	 OtherScientificTerm
--------------------------------
text: ” (have, lunch), (pay, the bill) and (leave the restaurant) compose a sequential event chain.
labels [{'entity': 'OtherScientificTerm', 'start': 5, 'end': 5, 'value': 'bill)'}, {'entity': 'OtherScientificTerm', 'start': 9, 'end': 9, 'value': 'restaurant)'}, {'entity': 'OtherScientificTerm', 'start': 12, 'end': 13, 'value': 'sequential event'}]
	value: bill) 	 OtherScientificTerm
	value: restaurant) 	 OtherScientificTerm
	value: sequential event 	 OtherScientificTerm
--------------------------------
text: The causal relation is the relation between the cause event and the effect event.
labels [{'entity': 'OtherScientificTerm', 'start': 1, 'end': 2, 'value': 'causal relation'}, {'entity': 'OtherScientificTerm', 'start': 8, 'end': 9, 'value': 'cause event'}]
	value: causal relation 	 OtherScientificTerm
	value: cause event 	 OtherScientificTerm
--------------------------------
text: For example, given the sentence “The nuclear leak in Japan leads to serious ocean pollution.
labels [{'entity': 'OtherScientificTerm', 'start': 6, 'end': 7, 'value': 'nuclear leak'}, {'entity': 'Task', 'start': 9, 'end': 9, 'value': 'Japan'}, {'entity': 'Task', 'start': 13, 'end': 14, 'value': 'ocean pollution.'}]
	value: nuclear leak 	 OtherScientificTerm
	value: Japan 	 Task
	value: ocean pollution. 	 Task
--------------------------------
text: It is obvious that the causal relation must be sequential.
labels [{'entity': 'OtherScientificTerm', 'start': 6, 'end': 6, 'value': 'relation'}]
	value: relation 	 OtherScientificTerm
--------------------------------
text: The conditional relation is a logical relation in which the illocutionary act employing one of a pair of propositions is expressed or implied to be true or in force if the other proposition is true.
labels [{'entity': 'OtherScientificTerm', 'start': 1, 'end': 2, 'value': 'conditional relation'}, {'entity': 'OtherScientificTerm', 'start': 5, 'end': 6, 'value': 'logical relation'}, {'entity': 'OtherScientificTerm', 'start': 10, 'end': 10, 'value': 'illocutionary'}]
	value: conditional relation 	 OtherScientificTerm
	value: logical relation 	 OtherScientificTerm
	value: illocutionary 	 OtherScientificTerm
--------------------------------
text: binations between frequency-based features may provide extra information that is useful for sequential relation and direction classification, shown in Table 2 (R1 to R11).
labels [{'entity': 'OtherScientificTerm', 'start': 0, 'end': 0, 'value': 'binations'}, {'entity': 'OtherScientificTerm', 'start': 2, 'end': 3, 'value': 'frequency-based features'}, {'entity': 'OtherScientificTerm', 'start': 12, 'end': 13, 'value': 'sequential relation'}, {'entity': 'OtherScientificTerm', 'start': 15, 'end': 16, 'value': 'direction classification,'}]
	value: binations 	 OtherScientificTerm
	value: frequency-based features 	 OtherScientificTerm
	value: sequential relation 	 OtherScientificTerm
	value: direction classification, 	 OtherScientificTerm
--------------------------------
input file path: 
```