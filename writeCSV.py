#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import csv
from csv import reader
from os.path import exists

FILE = "codes.csv"

fileheader = ["incident","store","ean"]

INC="12345"
STORE="Toulouse"
EAN="145673"

row_exists = False

def writeCSV(newrow):
    with open(FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(newrow)

def createCSV():
    with open(FILE, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fileheader)

def checkCSV(newrow):
    with open(FILE) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if set(row)==set(newrow):
                return True
    return False

if __name__ == '__main__':
    
    print("Debut")

    inc=INC
    store=STORE
    ean=EAN

    newrow = [inc, store, ean]
    if not exists(FILE):
        createCSV()
    else:
        row_exists = checkCSV(newrow)
    if row_exists:
        print("Ligne existe, ignorer")
    else:
        writeCSV(newrow)

    print("Fin")