# Collections as Data Task Force Report and Recommendations

Kevin Clair, Research Informatics and Publishing (chair)  
Linda Ballinger, Cataloging and Metadata Services  
Carmen Cole, William and Joan Schreyer Business Library  
Nathan Piekielek, Research Informatics and Publishing  
Andrea Pritt, Penn State Harrisburg Library  
Bethann Rea, Preservation, Conservation, and Digitization  
Caitlin Rizzo, Eberly Family Special Collections Library  
Heather Ross, Research Informatics and Publishing  
John Russell, Research Informatics and Publishing

* [Introduction](#introduction)
* [Collections as Data at Penn State](#collections-as-data-at-penn-state-university-libraries)
* [Background](#background)
* [Activities and Working Groups](#task-force-activities-and-working-groups)
* [Recommendations](#recommendations)

## Introduction

The Collections as Data Task Force was charged by the Libraries administration in March 2020 to define the scope of computational services for digital collections at the Libraries, develop workflows for publishing materials to support these services, and create a proof of concept for providing these services for the benefit of the Penn State community. Its membership included digital collections managers as well as subject liaisons with stewardship responsibilities, both at University Park and the Commonwealth Campuses.

The group was charged to complete the following specific tasks:

1. Create a Penn State-specific definition of collections as data projects and what falls within that description  
2. Develop review criteria and intake process for all potential collections as data projects
3. Evaluate and recommend infrastructure and technology for hosting and making collections as data accessible.  
    * Special attention should be paid to technology the library already supports
    * Technology and applications that can be linked from one platform to another or integrated into an existing platform  
4. Establish workflows and identify partners within the libraries (and potentially outside of the libraries) to support collections as data projects  
5. Begin to build a proof of concept service for publishing collections as data for the benefit of current and potential stakeholders

## Collections as Data at Penn State University Libraries

Collections as Data, in its imperative to consider our digital collections as sources of data for computational research, aligns with the Libraries’ stated strategic goals to maximize “the array of research materials available to the Penn State community” and to broaden “the concept of what constitutes ‘collecting’.” Collections as Data puts ethical considerations forefront and collections, policies, and technologies should flow from our ethical commitments. Collections as Data involves everyone who builds and manages collections, and rather than being approached as a project-centered method of providing access to collections, should be at the core of the digital collections program, in both collection development prioritization and digital collections production.

## Background

Collections as Data is [a philosophy of digital collection development](https://escholarship.org/uc/item/9881c8sv) encouraging computational use of the collections curated by digitization programs in libraries and archives, and the development of professional and ethical norms to ground the work. [The Collections as Data ethos](https://collectionsasdata.github.io/statement) was laid out in a series of workshops sponsored by the Institute of Museum and Library Services (IMLS) in 2017 and 2018, and consists of the following ten principles:

* Collections as data development aims to encourage computational use of digitized and born digital collections
* Collections as data stewards are guided by ongoing ethical commitments
* Collections as data stewards aim to lower barriers to use
* Collections as data designed for everyone serve no one
* Shared documentation helps others find a path to doing the work
* Collections as Data should be made openly accessible by default, except in cases where ethical or legal obligations preclude it
* Collections as data development values interoperability
* Collections as data stewards work transparently in order to develop trustworthy, long-lived collections
* Data as well as the data that describe those data are considered in scope
* The development of collections as data is an ongoing process and does not necessarily conclude with a final version

Projects and initiatives to build collections as data have taken on greater importance in the last few years as demands for computationally-ready collections have increased. Many major funding agencies have shown their interest in libraries exploring this new research and development area. Penn State Libraries have only recently begun to enhance our collections in this manner, and often without a centralized strategy or process.

## Task Force activities and working groups

The Task Force identified two high-level activities to complete in service of the group deliverables. These were the collection of use cases for collections as data services, and the development of workflows for publishing and maintaining collections as data. Work on these activities was divided among the Task Force in two sub-groups:

The **Use Cases Sub-group** (Kevin Clair, John Russell, Carmen Cole, Caitlin Rizzo, Heather Ross) considered use cases for Collections as Data at the University Libraries, and partners within and outside of the Libraries with whom additional use cases and Collections as Data personas may be developed. They considered existing cultural heritage digital collections in terms of their potential and readiness for being made available as data products, and consulted with faculty colleagues within the Libraries and across Penn State to identify research partners whose work aligns with the Libraries’ goals for Collections as Data services.  

The **Workflows Sub-group** (Kevin Clair, Linda Ballinger, Andrea Pritt, Bethann Rea) evaluated current publishing platforms and workflows for cultural heritage digital collections to assess their readiness for Collections as Data. They considered the existing and planned infrastructure for evaluating digital projects to determine where prospective publication of data products describing digital collections could find a fit, and identified publishing possibilities or shortcomings in the existing platforms for cultural heritage digital collections at the Libraries.

### Use Cases

The Use Cases sub-group identified several colleagues in the Libraries who work with digital collections and with researchers who wish to use them computationally, and spoke with them about the desired uses that they have observed. From these conversations, four broad categories of support for computational uses of digital collections were identified. A theme in these conversations was that many at Penn State, both within the Libraries and among the larger community, do not understand the principles of Collections as Data and how they might apply to their work as selectors, liaison librarians, and stakeholders of the digital collections program. Many of the use cases classified below serve to provide this educational role for community members.

Collection Management. Collections as data products or processes could be used to create data collections for use in teaching or research. This may be particularly useful for introducing computational research methods in disciplines covered by Penn State digital collections to undergraduate students.  

* Adding to our digital collections items that have been requested for digitization.  
* Adding to our digital collections data derived by researchers.  
* Metadata about metadata (for reliability, provenance, quality control).  
* Being able to track/measure impact of our digital collections/data as they are used and re-used.

**Text Creation and Mining.** These use cases include the ability to download transcriptions in bulk, either for a digital object or for an entire collection, in order to build a text corpus. (Our current digital repository architecture, to the extent it allows text download, only allows it at the page level.) Such access would allow researchers to identify resources in our digital collections at a deeper level than is allowed by metadata-based indexing and search alone, through scanning transcriptions and other text-based assets for mentions of a particular place, person, or event. Moreover, integrating these text products back into descriptive metadata may allow for new entry points into the digital collections, such as the ability to search across images for a person or a feature of the built environment, the presence of which was difficult to communicate through the limitations of metadata creation workflows.

Finally, supporting transcription platforms as a part of the digital collections infrastructure, and integrating the data from transcription platforms into the digital collections, may serve not only to generate data to improve the digital collections user experience, but also to increase engagement and investment with the digital collections program itself.  

**Cartographic Collections as Geospatial Data.** Common physical cartographic collections in academic libraries include print maps, atlases, and aerial photography negatives and contact prints – all of which were originally created and collected as scientific documents to authentically and accurately document the spatial properties of phenomenon on the earth’s surface and subsurface. For this reason, all physical cartographic resources are also useful as digital geospatial data.  

There are three levels of treating physical cartographic collections as digital geospatial data with coincident increases in difficulty to achieve each level and also increasing usefulness to contemporary researchers. Of note is that all of the below three levels below require that the physical cartographic resource be digitized, while levels 2 and 3 require that they are digitized in a way that preserves the geometric (I.e. spatial), accuracy of the original information presented. This is akin to requiring that optical character recognition (OCR) of digitized textual documents be of good enough quality that most words in the digital text are correctly spelled – correct spelling of words is like the correct placement of things on cartographic resources, without it the resource is of little use.

1. Enabling geographic search – enhancing catalog records (i.e. metadata) with basic geographic descriptors (i.e. coordinates), has been a common practice for some time. The practice is generally easy to achieve and automate although also is of limited utility to researchers as it only facilitates geographic search, but falls well short of allowing researchers to incorporate the information encoded on cartographic resources into the contemporary research process.
2. Georeferencing, rectification, and distortion correction – georeferencing is the well-established practice of associating the locations of numerous features on an image (i.e. a digitized cartographic resource), with the locations on a spatial coordinate system and world datum, recording the error of this step in a spatial metadata record, and publishing the result in a geospatial data file format. For maps and atlases, distortion correction is inherent in the georeferencing exercise whereas for aerial photography there remains systematic distortion that can be removed through interior orientation, relative orientation, absolute orientation and orthorectification. Many of these steps have been completely or mostly automated using common computer vision techniques and have been successfully applied to entire corpuses of scanned maps in the case of the USGS historic topographic map collection for example. The Penn State University Libraries Donald W. Hamer Center for Maps and Geospatial Information is currently developing tools and workflows to semi-automate this step for historic aerial photographs with early success. The result of this step is an image that is correctly placed on the earth’s surface, but falls short of digital spatial data that is easily incorporated into the contemporary research process.
3. Vectorization, feature extraction and image classification – the spatial information encoded on physical cartographic resources is represented with lines, color tones, text and symbols. Extracting this information and converting it to spatial data involves common practices of vectorization and feature extraction (in the case of maps and atlases), and image classification (in the case of aerial photographs). Again, common computer vision techniques like template matching and object-oriented image classification along with machine- and deep-learning techniques like neural networks and randomForests have proven useful for these steps although variation in map style, camera lens, and digitization practices limit our ability to fully automate these steps. The result of this step is a completely spatial dataset based on a physical cartographic collection.

A final expectation of providing access to cartographic collections as data is a streaming data service of some kind (i.e. REST services), that provide access to the data without the need for download. This is especially important with geospatial datasets that are often large in file size.  

There is already a well-established user community for geospatial data with demand for the products derived from physical cartographic resources described above being “High”.

**Bulk access to content and metadata.** Data packages consisting of bulk collection metadata, or potentially the collection materials themselves (to facilitate offline text or image analysis), was identified by the group as a possible Collections as Data use case. Librarians reported reference inquiries from visitors that could be easily addressed if it was possible to filter search results by particular parameters, such as geographic coverage or subject heading, and bulk download the metadata and/or content of the ensuing search results. This could also enable curatorial work or the development of Open Educational Resources (OER) around digital collections, and facilitate partnerships with other units on campus working in the cultural heritage digitization area, such as the Palmer Museum of Art.

### Workflows

The Workflows sub-group was asked to consider existing production processes and technologies in use at the Libraries for publishing digital collections, and look for ways in which computational access to those collections could be provided within them. The sub-group was also asked to look for any technology gaps that prevent computational access to digital collections. The work of the Workflows sub-group aligned with concurrent, high-level work on evaluating and improving digital collections production workflows and communication.

The group completed three tasks. First, it performed an environmental scan of the literature on Collections as Data and various projects on computational access to digital collections at peer institutions. This provided insight for the Task Force on what computational access could look like for different types of collections published at Penn State.

Second, the group reviewed existing projects in the University Libraries Digital Collections, identifying areas where collections might lend themselves well to computational access (such as through publication of transcript corpora or enhancement of metadata) and areas where further research into computational methods might be worthwhile.

Finally, the group looked at the Libraries’ current platforms for publishing digital collections, as well as other tools that could integrate with those platforms to allow for providing computational access to those collections. On its own, CONTENTdm provides little support for the kinds of bulk access to collection materials that are foundational for Collections as Data services, so third-party services would be essential for providing a host for text corpora, bulk metadata downloads, and other assets to which links from CONTENTdm could be provided. Possibilities discussed by the group included looking into working with other units on campus using Omeka for publishing and gathering user-contributed transcriptions of text content; integrating with ScholarSphere for publishing data about digital collections; and using custom interfaces to CONTENTdm collections for additional services, such as [CollectionBuilder](https://collectionbuilder.github.io). The group also noted the importance of creating and maintaining space for ongoing exploration and evaluation of new technologies to support computational access to digital collections, as they are released.

Three members of the Workflows sub-group also served concurrently on the Digital Collections Process Working Group, charged by the department heads of units involved with the digital collections production process to review and improve production workflows and communication. Through this integration, computational access will be part of the project evaluation process for digital collections, both in considering how it can be provided for all new digitization projects and in assessing ways in which it can be retroactively provided for existing collections. The group discussed several strategies for this, including publishing updated data dictionaries for metadata about digital collections to facilitate interpretation of the data; developing format-specific guidelines for computational access and services; and considering the provision of additional research support services, such as Collections as Data, as a digital project in its own right.

## Recommendations

### For the Digital Projects Team

Considerations for computational access to digital collections should be included in each digital collection or project managed by the Libraries. These considerations include identifying computational services for new collections, and retrofitting existing collections to support those services. While project submissions with an explicitly computational focus are expected and encouraged, Collections as Data asks for ethical and responsible computationality to be at the heart of everything that we do when publishing collections digitally. Establishing review criteria for computational services, and other initiatives to improve computational access to digital collections, will also be important. The Digital Collections Process Working Group has already started along this path; continued development of this criteria, and engaging stakeholders through groups such as the Campus Curators, should be encouraged.

The Digital Projects Team should also consider investigating technical tools and protocols to support Collections as Data services. For example, at the moment there is no clear path in the cultural heritage digital repository by which users might download a bulk text corpus for a digital collection or set of digital assets. The Digital Projects Team should consider transcription tools, such as [Zooniverse](https://zooniverse.org) or [From the Page](https://fromthepage.com), that can be used to gather transcriptions from end users, feed those transcriptions back into the cultural heritage repository, and allow publication of those transcripts with supporting metadata as data packages. As part of its overall strategy for open digital collections publication standards, the Digital Projects Team should also make publicly available its schemas and data dictionaries for publishing collections as data for various collection formats (e.g. text corpora, geo-located data describing cartographic and geospatial collections), in order for potential users to make informed decisions about whether the data will be applicable to their research and instructional uses.

Building ethical, responsible digital collections requires well-defined policies for the development and curation of digital collections. These policies will be living documents, and serve to prompt discussions about ethics, privacy, access, copyright, and other principles. Before computational access is created, collections will be appraised according to the principles set out in the Santa Barbara Statement and the appraisal document will be included in the collection. Appraisals that have negative results will be retained and available for community review. While the Digital Projects Team will ultimately be charged with carrying out these policies in practice, the development and review of these policies is a community process, and should involve representatives from the communities of collection stewards, subject librarians, and digital collections end users.

### For digital collections stewards and subject librarians

For Collections as Data to be successful, it needs a community of builders and users. Currently at Penn State, it is mostly unknown or misunderstood. To change this, we need to develop simple digital collections datasets that can be used to introduce liaison librarians, curators, and other stakeholders to the principles of Collections as Data and how they manifest in Penn State digital collections. We also need conversations within and beyond the Libraries about the Collections as Data framework, and how it may be made applicable to the work of librarians as well as research and teaching faculty. These conversations will hopefully lead to a wider array of data services and support within the digital collections program. Involving other librarians, faculty, and staff who can weigh in on potential use cases and delivery mechanisms for data derived from digital collections, or who are conducting research using digital collections, may provide insight on possible projects or workflow considerations for quantitative research around our own digital collections. There will need to be a mechanism in place for regularly assessing computational needs and identifying partners.

Collections stewards and subject librarians can also help to develop Collections as Data services through ongoing communication and advocacy with their faculty, staff, and student liaison communities. The primary goal of the Collections as Data initiative is to support teaching and research, and evaluation should assess the use of collections in the classroom and track the use of these collections in research. By engaging beyond the Libraries, collection stewards and subject librarians can help to develop the digital collections program by identifying and cultivating sources of computational digital collections projects from outside the digitization program.

### For the University Libraries  

The concerns for ethics and responsibility to the subjects of digital collections that are at the heart of Collections as Data should not be limited only to research support services for digital collections. These concerns should challenge the Libraries as a whole to place an ethics of care at the center of its stewardship strategy for all digital materials. The Libraries should develop a strategy for selecting, maintaining, and developing services around its digital collections across all repository and service platforms, identifying those materials which it is best positioned to make available through computational means and centering the perspectives and experiences of the subjects of those collections when doing so.
