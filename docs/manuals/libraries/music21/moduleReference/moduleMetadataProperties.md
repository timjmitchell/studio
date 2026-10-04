Source: https://music21.org/music21docs/moduleReference/moduleMetadataProperties.html

# music21.metadata.properties

## PropertyDescription

class music21.metadata.properties.PropertyDescription(*uniqueName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *namespace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *oldMusic21Abbrev: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *oldMusic21WorkId: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *valueType: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[DatePrimitive](moduleMetadataPrimitives.html#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") | [Text](moduleMetadataPrimitives.html#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") | [Copyright](moduleMetadataPrimitives.html#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = <class 'music21.metadata.primitives.Text'>*, *needsArticleNormalization: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *isContributor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/metadata/properties.html#PropertyDescription)
:   Describes a single standard metadata property.

    * name: str is the namespace’s name of the property (the tail of the property term URI).
    * namespace: str is a shortened form of the URI for the set of terms.
      :   + ‘dcterms’ means the property term is from the Dublin Core terms,
            :   defined at <<https://www.dublincore.org/specifications/dublin-core/dcmi-terms/>>
          + ‘marcrel’ means the property term is from the MARC Relator terms,
            :   defined at <<https://id.loc.gov/vocabulary/relators.html>>
          + ‘humdrum’ means the property term is from the Humdrum reference record terms,
            :   defined at <<https://www.humdrum.org/reference-records/>>
    * isContributor: bool is whether the property describes a contributor.
    * needsArticleNormalization: bool is whether the property values might
      :   benefit from article normalization when getting as a string (this is
          generally True for various kinds of titles).
    * oldMusic21Abbrev: str is the backward compatible music21 abbreviation for this
      :   property.
    * oldMusic21WorkId: str is the backward compatible music21 name for this property.
    * uniqueName: str is the official music21 name for this property, that is unique
      :   within the list of properties. There is always a unique name, but the
          uniqueName field is only set if name is not unique enough.
          To get the unique name from a particular PropertyDescription, call:
          (desc.uniqueName if desc.uniqueName else desc.name)
    * valueType: Type is the actual type of the value that will be stored in the metadata.
      :   This allows auto-conversion to take place when clients store items in the
          metadata, and is the tuple element type clients will always receive from
          md[‘uniqueName’] or md[‘namespace:name’].

[`PropertyDescription`](#music21.metadata.properties.PropertyDescription "music21.metadata.properties.PropertyDescription") methods

PropertyDescription.\_\_eq\_\_(*other*)
:   Return self==value.
