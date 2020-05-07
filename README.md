# Blast2GFF
This program takes format 6 of blast output and converts the information to a gff file for use in a genome browser
## Getting Started

### Prerequisites
```
You must be on a Linux/Unix environment
Python 3.0 or newer (I used 3.8.2)
IGV downloaded on your system
```
### Setup
- Download [IGV](https://software.broadinstitute.org/software/igv/download)
- Download [Python 3.x](https://www.python.org/downloads/)

### Inputs/Outputs and How to Run
- Inputs: `blast2gff.py` and `FILE.bln6`
- How to run: `py blast2gff.py FILE.bln6`
- Output: `results.gff`

### Use: 
  - Open IGV and load in the genome that your blast results are from by going to `Genome>Load Genome From File...>`
  - Load in your gff file by going to `File>Load from File...`
  - Matches will be displayed, colored to their match percentage, with a gradient from green (100%) to red (80%)

### Bugs/Limitations
  - I was unable to display # of reads supporting each TelContig/SubTelContig and # of blast alignments to genome for each Tel/SubTelContig as the calculations I wrote looks at each line individually before writing it to the gff. Displaying these would require looking at the file as a whole before adding data to each individual lines.
  
### Author
Arthur Davis
