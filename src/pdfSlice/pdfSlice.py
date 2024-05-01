#!/usr/bin/env python3

import sys
import argparse
from pypdf import PdfMerger, PdfReader, PdfWriter

def initArg():
    parser=argparse.ArgumentParser(prog="pdfSlice", description="slice and save the page of your pdf")
    parser.add_argument('infile', nargs='?')
    parser.add_argument('outfile', nargs='?')
    parser.add_argument('-p', '--pages', action='store', dest='pages',type=str, nargs='+', default=['item1', 'item2', 'item3'], help="Examples: infile outputfile -p 1-3 5 7-9 10-11 16")
    l_arg = parser.parse_args()
    print(l_arg.__dict__)
    return l_arg

def pdfSlice(l_infile,l_outfile,l_pages):
    print([l_infile,l_outfile,l_pages])
    reader = PdfReader(l_infile)
    merger = PdfWriter()
    for pageRange in l_pages:
        if(pageRange.find('-') != -1):
            begin_idx,end_idx = pageRange.split('-')
            if (begin_idx.isnumeric() and end_idx.isnumeric() == True):
                begin_idx = int(begin_idx)-1
                end_idx=int(end_idx) #  include the last page 
                if(begin_idx >= 0 and end_idx < reader.get_num_pages()):
                    for idx in range(begin_idx, end_idx):
                        merger.add_page(reader.pages[idx])
                else:
                    print("no output file created: some pages provided are out of boundaries")
                    return
            else:
                print("no output file created: provide only numericals arguments with the p option")
                return
        else:
            if (pageRange.isnumeric() == True):
                idxPage = int(pageRange)-1
                if(idxPage >= 0 and idxPage < reader.get_num_pages()):
                        merger.add_page(reader.pages[idxPage])
                else:
                    print("no output file created: some pages provided are out of boundaries")
                    return
            else:
                print("no output file created: provide only numericals arguments with the p option")
                return
    merger.write(l_outfile)


if __name__ == "__main__":
   args = initArg()
   infile,outfile,pages = args._get_kwargs()
   infile,outfile,pages = infile[1],outfile [1],pages[1]
   pdfSlice(infile,outfile,pages)

    