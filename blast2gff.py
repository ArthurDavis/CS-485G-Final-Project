import re
import sys
import csv
import os

def main():
  if (len(sys.argv)==1):
    print("Usage: 'py blast2gff.py blastfile.bln6'")
    exit
  else:
    blastfile= sys.argv[1]
    with open(blastfile, newline='') as data:
      data_reader = csv.reader(data, delimiter=' ')
      result=open("resluts.gff", "w+")
      color='#000000'
      for line in data_reader:
        direction='+'
        if (float(line[2]) >= 98 and float(line[2]) <= 100):
          color="#228B22"
        elif (float(line[2]) >= 96 and float(line[2]) < 98):
          color="#33891E"
        elif (float(line[2]) >= 94 and float(line[2]) < 96):
          color="#46881A"
        elif (float(line[2]) >= 92 and float(line[2]) < 94):
          color="#5A8717"
        elif (float(line[2]) >= 90 and float(line[2]) < 92):
          color="#6F8613"
        elif (float(line[2]) >= 88 and float(line[2]) < 90):
          color="#858510"
        elif (float(line[2]) >= 86 and float(line[2]) < 88):
          color="#846C0C"
        elif (float(line[2]) >= 84 and float(line[2]) < 86):
          color="#835209"
        elif (float(line[2]) >= 82 and float(line[2]) < 84):
          color="#823706"
        elif (float(line[2]) >= 80 and float(line[2]) < 82):
          color="#811C03"
        else:
          color="#800000"
        if (line[8]>line[9]): 
          direction="-"
        gff_line="{}\tBlast\tContig\t{}\t{}\t.\t{}\t.\tName={}; %_Blast_Alignment={}; Alignment_Length={}; color={}\n".format(line[1], line[8], line[9], direction, line[0], line[2], line[3], color)
        result.write(gff_line)
      result.close()
    
if __name__ == '__main__':
  main()