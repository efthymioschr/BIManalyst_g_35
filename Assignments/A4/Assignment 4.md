Title:
CO₂ Footprint Calculation Tool for Structural Concrete

Summary: 
This Python-based tool analyzes IFC models to estimate the CO₂ footprint of concrete elements (walls, slabs, and columns) during the design phase. It supports sustainable design by automating material quantification and footprint calculation.\\


Our specific focus is on environmental impact analysis for structural concrete elements during the design phase. The tool addresses sustainability by verifying CO₂ footprint claims, aligning with a BIM use focused on quantifying material volumes and estimating life cycle impacts. The tool extracts data from IFC files to calculate the total volume of concrete structural elements (walls, slabs, and columns), normalizes this to the Gross Floor Area (GFA), and estimates the CO₂ footprint per square meter per year.

The tool operates within the OpenBIM framework, leveraging the ifcopenshell library to automate calculations, ensuring compliance with sustainability regulations (e.g., a 12 kg CO₂ eq./m²/year limit). This supports decision-making in Stage B (Design Development) of the building lifecycle.

This tool development aligns with the OpenBIM Analyst Role, Learning Level 2, as it involves:

1) Analyzing IFC files using Python scripting with ifcopenshell for property extraction and geometry calculations.
2) Custom environmental analysis, including material-specific footprint estimates.
3) Intermediate-level development of Python-based scripts to handle data extraction and calculations.

While the tool fulfills Level 2 objectives, future refinements (e.g., broader material handling and API integration) could elevate it to Analyst Level 3.

Explicit Summary Section
Title: CO₂ Footprint Calculation Tool for Structural Concrete
Summary: A Python-based OpenBIM tool to estimate CO₂ footprints of concrete walls, slabs, and columns in the design phase using IFC data, promoting sustainability and compliance with environmental standards.
