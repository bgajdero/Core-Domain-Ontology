from owlready2 import default_world, get_ontology, Thing, rdfs

cdo_onto = get_ontology("https://onto.colossi.network/cdo")
cdo = cdo_onto.get_namespace("https://onto.colossi.network/cdo#")

time = default_world.get_ontology("http://www.w3.org/2006/time").load(reload=True)

with cdo:
    class CDOThing(Thing):
        pass
    rdfs.comment[CDOThing] = ["CDOThing is the top CDO class."]

    #======================================
    class Behaviour(CDOThing):
        pass
    rdfs.comment[Behaviour] = ["The monitoring of harmonization consistency across datasets. Superclass of Action and Object."]
    class Passive(Behaviour):
        pass
    rdfs.comment[Passive] = ["A background validation system ensuring harmonized data integrity. (Object)"]
    class Active(Behaviour):
        pass
    rdfs.comment[Active] = ["A manually triggered pipeline process for schema adjustments. (Action)"]

    class Perspective(CDOThing):
        pass
    rdfs.comment[Perspective] = ["The interpretative stance on structuring AI training data. Can be an instance of either Subjective (superclass of Concept) or Objective (Superclass of Event)."]
    class Objective(Perspective):
        pass
    rdfs.comment[Objective] = ["The measurable accuracy of harmonized data transformation. Superclass of Event."]
    class Subjective(Perspective):
        pass
    rdfs.comment[Subjective] = ["The human-defined priority of ontology terms within semantic mapping. (Concept)"]
    #######################################
    class Object(Passive):
        pass
    rdfs.comment[Object] = ["The dataset ingested into the pipeline for processing."]

    class Attribute(CDOThing):
        pass
    rdfs.comment[Attribute] = ["A specific metadata field (e.g., column name in a schema)."]

    class hasAttribute(Object >> Attribute):
        pass

    class Form(CDOThing):
        pass
    rdfs.comment[Form] = ["The DSL-formatted schema model used for standardization."]

    class Kernel(CDOThing):
        pass
    rdfs.comment[Kernel] = ["The core processing unit performing schema synthesization."]
    class isProcessedBy(Attribute >> Kernel):
        pass
    class Schema(CDOThing):
        pass
    rdfs.comment[Schema] = ["The unified schema generated for harmonizing structured and unstructured data."]
    class structures(Kernel >> Schema):
        pass
    class isSystemicTo(Schema >> Form):
        pass
    class Chart(CDOThing):
        pass
    rdfs.comment[Chart] = ["The rendered display with data from the form."]
    class isVisualizedAs(Form >> Chart):
        pass
    class Text(CDOThing):
        pass
    rdfs.comment[Text] = ["Unstructured data converted into structured format via NLP."]
    class isEncodedAs(Chart >> Text):
        pass

    #######################################
    class Event(Objective):
        pass
    rdfs.comment[Event] = ["A new dataset ingestion or schema synthesis process initiation."]

    class Field(CDOThing):
        pass
    rdfs.comment[Field] = ["A specific record field (e.g., a column within a structured dataset)."]
    class occursIn(Event >> Field):
        pass
    class Shell(CDOThing):
        pass
    rdfs.comment[Shell] = ["The secured environment protecting transformations at each stage."]
    class isEncapsulatedBy(Field >> Shell):
        pass
    class Record(CDOThing):
        pass
    rdfs.comment[Record] = ["A harmonized data entry within the transformed dataset."]
    class isPartOf(Shell >> Record):
        pass

    class Log(CDOThing):
        pass
    rdfs.comment[Log] = ["The recorded process logs of the schema synthesization and transformation pipeline."]
    class loggedAt(Log >> time.Instant):
        pass

    class isStemmaticTo(Record >> Log):
        pass
    class isComposedOf(Log >> Record):
        inverse_property = isStemmaticTo
        pass

    class Ledger(CDOThing):
        pass
    rdfs.comment[Ledger] = ["The immutable audit trail of all pipeline operations."]
    class isAggregatedIn(Log >> Ledger):
        pass

    class Track(CDOThing):
        pass
    rdfs.comment[Track] = ["The sequential tracking of dataset modifications across the pipeline."]
    class isTrackedBy(Ledger >> Track):
        pass

    class State(CDOThing):
        pass
    rdfs.comment[State] = ["The current status of a dataset as it moves through pipeline stages."]
    class isRecordedIn(State >> Log):
        pass
    #------------------------------
    class Stemma(CDOThing):
        pass
    rdfs.comment[Stemma] = ["The lineage representation of each transformation process, forming a full provenance record."]
    class underpins(Text >> Stemma):
        pass
    class hasLineage(Track >> Stemma):
        pass



    #===============================
    class Effect(CDOThing):
        pass
    rdfs.comment[Effect] = ["The impact of schema standardization on downstream AI model performance. Relates Object to Event"]

    class traces(Stemma >> Effect):
        pass
    class Mechanism(CDOThing):
        pass
    rdfs.comment[Mechanism] = ["The transformation logic applied to raw data during harmonization."]
    class isRealizedThrough(Effect >> Mechanism):
        pass
    class Scheme(CDOThing):
        pass
    rdfs.comment[Scheme] = ["The structured workflow guiding schema synthesis and frame contextualization. Relates Object to Concept."]
    class constructs(Mechanism >> Scheme):
        pass
    class hasStructure(Object >> Scheme):
        pass
    class demonstrates(Event >> Effect):
        pass
    class isCausal(Object >> Effect):
        pass
    class enables(Form >> Mechanism):
        pass

    #######################################
    class Concept(Subjective):
        pass
    rdfs.comment[Concept] = ["The semantic mapping of schema elements to ontology terms."]

    class Term(CDOThing):
        pass
    rdfs.comment[Term] = ["A standardized term used for ontology-based contextualization."]
    class describedBy(Concept >> Term):
        pass
    class Interface(CDOThing):
        pass
    rdfs.comment[Interface] = ["The API allowing external data sources to connect to the pipeline."]
    class isExposedThrough(Term >> Interface):
        pass
    class Frame(CDOThing):
        pass
    rdfs.comment[Frame] = ["The contextual metadata describing the relationship between schema attributes and ontology terms."]
    class isContexualizedBy(Interface >> Frame):
        pass
    class Notice(CDOThing):
        pass
    rdfs.comment[Notice] = ["A system alert regarding inconsistencies in harmonization or missing ontology mappings."]
    class isEpistemicTo(Frame >> Notice):
        pass
    class contains(Notice >> Frame):
        pass


    class Policy(CDOThing):
        pass
    rdfs.comment[Policy] = ["The enforced data governance rules ensuring compliance."]
    class isRegulatedBy(Notice >> Policy):
        pass
    class Note(CDOThing):
        pass
    rdfs.comment[Note] = ["A record of human-interpreted decisions made in data transformation."]
    class isReferencedBy(Notice >> Policy):
        pass
    
    class contextualizes(Concept >> Object):
        pass

    class hasKnowledge(Concept >> Scheme):
        pass
    #===============================
    class Goal(CDOThing):
        pass
    rdfs.comment[Goal] = ["The objec tive of transforming data into an AI-ready format. Relates Concept to Event."]
    class isAchieved(Event >> Goal):
        pass
    class defines(Concept >> Goal):
        pass

    #######################################
    class Action(Active):
        pass
    rdfs.comment[Action] = ["The execution of a transformation or harmonization operation."]

    class Value(CDOThing):
        pass
    rdfs.comment[Value] = ["A computed quality score assessing data integrity."]
    class processes(Action >> Value):
        pass
    class Function(CDOThing):
        pass
    rdfs.comment[Function] = ["The normalization and harmonization functions applied to data."]
    class isEnabledBy(Value >> Function):
        pass
    class Packet(CDOThing):
        pass
    rdfs.comment[Packet] = ["A data bundle of structured metadata and schema updates."]
    class isExecutedThrough(Function >> Packet):
        pass
    class Payload(CDOThing):
        pass
    rdfs.comment[Payload] = ["The extracted and transformed structured dataset ready for training AI models."]
    class isSystematic(Packet >> Payload):
        pass                
    class isTransmittedBy(Payload >> Packet):
        pass
    class encodes(Packet >> State):
        pass
    class Statement(CDOThing):
        pass
    rdfs.comment[Statement] = ["The declared compliance of a dataset with regulatory standards."]
    class isDeclaredBy(Payload >> Statement):
        pass
    class Fact(CDOThing):
        pass
    rdfs.comment[Fact] = ["A verified, processed data point ensuring accuracy."]
    class isAffirmedBy(Statement >> Fact):
        pass
    class triggers(Action >> Event):
        pass

    #======================================
    class Method(CDOThing):
        pass
    rdfs.comment[Method] = ["The specific technique used for package harmonization and frame contextualization. Relates Action to Concept:"]
    class Reason(CDOThing):
        pass
    rdfs.comment[Reason] = ["The rationale for selecting specific schema transformations. Relates Action to Event."]
    class instanceOf(Action >> Method):
        pass
    class isExpressedAs(Concept >> Method):
        pass
    class isJustifiedBy(Method >> Reason):
        pass
    class hasIntelligence(Action >> Reason):
        pass
    class hasCausality(Event >> Reason):
        pass

    class Purpose(CDOThing):
        pass
    rdfs.comment[Purpose] = ["The intent behind structuring and harmonizing datasets for AI model training."]
    class fulfills(Method >> Purpose):
        pass
    class guides(Purpose >> Reason):
        pass
    #-----------------------------------------
    class Package(CDOThing):
        pass
    rdfs.comment[Package] = ["The complete harmonized dataset with transformation instructions."]
    class validates(Fact >> Package):
        pass
    class utilizes(Package >> Method):
        pass
    class formsBasisOf(Note >> Package):
        pass
    #======================================
    class Cause(CDOThing):
        pass
    rdfs.comment[Cause] = ["The causal relationship between raw data variations and harmonization requirements. Relates Action to Object)."]
    class initiates(Action  >> Cause):
        pass
    class isAffectedBy(Object >> Cause):
        pass
    

    #######################################
    class Data(CDOThing):
        pass
    rdfs.comment[Data] = ["The structured and unstructured data ingested into the pipeline."]

    class capturedAs(Data >> Object):
        pass
    class exchangedThrough(Data >> Action):
        pass
    class enteredAs(Data >> Event):
        pass
    class accessedBy(Data >> Concept):
        pass

    #######################################
    class isLoggedAs(Packet >> Record):
        pass

    class Receipt(CDOThing):
        pass
    rdfs.comment[Receipt] = ["A cryptographic proof confirming a dataset transformation and validation."]
    class acknowledges(Receipt >> Payload):
        pass
    class isAcknowledgedBy(Record >> Receipt):
        pass