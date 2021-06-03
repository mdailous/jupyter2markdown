#!/usr/local/bin/env python3
"""Jupyter Notebook to Markdown Converter.

Converts Jupyter notebooks to markdown format. The resulting markdown file is saved in the same directory with the same base name as the Jupyter Notebook.

Copyright 2021 Michael S. Dailous

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
from argparse import ArgumentParser
from json import load
from pathlib import Path

VERSION="0.0.1"
DEBUG=False

def debugPrint(text: str):
    """Writes debug output.
    
    The specified string is output only if the debugging has been enabled.
    
    Parameters
    ----------
    text : str
        The string to output
    
    Returns
    -------
    Nothing
    """
    if DEBUG:
        print(text)


def convert(cell):
    """Converts the Jupyter Notebook source list to markdown.
    
    Parameters
    ----------
    cell : map
        A cell from the Jupyter notebook
        
    Returns
    -------
    A string containing the markdown formatted source contents.
    """

    markdownResult=""
    if cell['cell_type'] == 'code':
        markdownResult += '```\n'

    for line in cell['source']:            
        markdownResult += line

    if cell['cell_type'] == 'code':
        markdownResult += '\n```'
    
    debugPrint(markdownResult)
    markdownResult += '\n\n'
    
    return markdownResult

if __name__ == "__main__":
    parser = ArgumentParser(description="Jupyter Notebook to Markdown Converter (v{})".format(VERSION))
    parser.add_argument('notebookFile', metavar='NOTEBOOK', help='The Jupyter Notebook to convert. Specify the full path if the file is not in the current directory')
    parser.add_argument('--debug', dest='debug', default=False, action='store_true', help='Enables debugging output')
    parser.add_argument('--overwrite', dest='overwriteOutput', default=False, action='store_true', help='Forces overwriting the markdown file')
    
    args=parser.parse_args()
    DEBUG=args.debug
    
    notebookFile=Path(args.notebookFile)
    if not notebookFile.exists() or not notebookFile.is_file():
        print("The file {} does not exist. Please specify the full path to the filename.".format(notebookFile.absolute()))
        sys.exit(-1)
    
    markdownFile=Path(notebookFile.parent.joinpath("{}.md".format(notebookFile.stem)))
    if markdownFile.exists() and not args.overwriteOutput:
        print("Markdown file [{}] already exists. Either delete the file or use the --overwrite flag to force overwriting.".format(markdownFile))
        sys.exit(-1)

    debugPrint("[+] Saving markdown to {}".format(markdownFile))

    debugPrint("[+] Loading Juptyer Notebook file")
    with notebookFile.open('r') as f:
        json_data = load(f);
        debugPrint("[-] {}".format(json_data))
    
    with markdownFile.open('w') as f:
        debugPrint("[+] Processing notebook")
        for cell in json_data['cells']:
            debugPrint("[-] Cell: {}".format(cell))
            f.write(convert(cell))
        f.flush()
        f.close()
        
    print("Markdown saved to {}".format(markdownFile.absolute()))
