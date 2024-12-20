This document is a continuation of the work undertaken in Assignment 2, where we defined a use case focusing on verifying the CO2 footprint claim of a building during its design phase. In that assignment, we identified the need for a specialized tool to calculate the environmental impact of structural elements, particularly focusing on concrete usage, to ensure compliance with sustainability regulations.

Problem/Claim

The tool solves the problem of verifying the CO2 footprint claim of a building during the design phase without the use phase. Specifically, it assesses whether the building adheres to sustainability standards, such as the limit of 12 kg CO2 eq./m²/year, by calculating the CO2 emissions based on the materials used in the IFC file.

In comparison group 6 claimed to have an LCA of X.

Problem Discovery

The problem arises in the context of early-stage building design, where there is a need to ensure compliance with environmental regulations while minimizing the CO2 footprint. This issue was identified during the design phase of sustainable construction projects, where quantifying materials and their environmental impacts is critical.

Description of the Tool

The tool extracts information from an IFC file to calculate the volume of elements that are made of concrete and apply a mean LCA (Life Cycle Assessment) emission factor. Therefore, the tool provides an approximate value of the CO2 footprint of concrete elements.

The tool focuses on the structural model elements:

Walls

Slabs

Columns

The total concrete volume of these elements are the multiplied by an emission factor for concrete estimated to 300 kg CO2-eq/m3 (based on an estimated mean for concrete from https://www.epddanmark.dk/uk/epd-database/)

The GFA is estimated using the total area of slabs on or above level 0. This is then used along with the standard lifespan of 50 years to calculate the kg CO2-eq / m2 / year.

The tool This tool is considered to be only part of a solution to the problem and would need further work in order to test the claim. The further work and limitations in order to reach our goal is described in the end of this assignment.

Advanced Building Design

The tool is useful in Stage B (Design Development) of Advanced Building Design. During this stage, the design evolves and decisions on material usage are made.

Relevant Subjects

This tool is applicable to the following subjects:

Sustainable Design

Structural Engineering

Environmental Impact Assessment

Required Information

To function correctly, the tool requires:

Model Details:

Structural elements (e.g., columns, walls, slabs).

Material specifications (e.g., concrete).

Geometric Properties:

Dimensions (e.g., height, thickness, area, or volume).

Emission Factors:

CO2 conversion factors (from LCA databases such as LCA Byg).

Design Context:

Slabs or floors in order to calculate Gross Floor Area (GFA) for CO2 footprint normalization.

Workflow and Details

Goal of the Tool

To calculate an approximate CO2 footprint in the early design stage to ensure compliance with building regulations and sustainability goals.

Model Use (BIM Use)

The tool supports environmental impact analysis by automating material quantification and CO2 estimation.

Further improvement of the tool:

Include multiple materials not just concrete

Differentiate between material specification

Include beams and other elements from the structural model

Or event extend the tool to function in architectural model

Limitations / what would we have liked to known earlier

Limited coding knowledge.

Due to limited knowledge we had to lower our ambitions during the process to only apply to one material and three elements.

Sorting based on material properties

We couldn’t find a way to reach the material layer in properties and correctly sort elements by material. Therefore, materials are only selected if “concrete” appears in the name of the element.

