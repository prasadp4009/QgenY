#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: genIntf.py
Author: Prasad Pandit
Email: prasadp4009@gmail.com
Github: https://github.com/prasadp4009
Description: Script to generate SV interface from module
"""

import sys, getopt
import re

DEBUG_ON = False

def gen_intf(inFile, outFile):
    """docstring for gen_intf"""
    module_ports = ''
    module_name  = ''
    found_module = False
    found_ports  = False
    keywords     = ["input", "output", "inout", "wire", "reg", "logic", "bit"]
    with open(inFile, 'r') as file:
        module_name = inFile.split('.')[0]
        while True:
            line = file.readline()
            if "module "+module_name in line:
                module_ports = module_ports + line
                found_module = True
                break
        while found_module:
            line = file.readline()
            if ");" not in line:
                module_ports = module_ports + line
                found_ports = True
            else:
                module_ports = module_ports + line
                break
        #print(module_ports)
    if found_module and found_ports:
        parameter_port_list = module_ports[module_ports.find("("):module_ports.find(");")+1]
        parameter_port_list = parameter_port_list.splitlines()
        intf_list = []
        invalid_entry = []

        for line in parameter_port_list:
            comment = line.strip()
            #print(line)
            if "//" == comment[:2]:
                comment = comment + "\n"
                intf_list.append('\n')
                intf_list.append("  "+comment)
                intf_list.append('\n')
            elif "parameter" in line:
                temp = line.strip().split(',')[0] + ';\n'
                intf_list.append("  "+temp)
                #print(temp)
            elif "input" in line:
                check_input = re.sub('\s+', ' ', line.strip()).split(' ')[0]
                if check_input == "input":
                    if "//" in line:
                        port_part, comment_part = line.strip().split('//')
                        port_part = re.sub('\s+', ' ', port_part.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "logic "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Input : " + comment_part + "\n"
                        intf_list.append(intf_signal)
                    else:
                        port_part = re.sub('\s+', ' ', line.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "logic "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Input" + "\n"
                        intf_list.append(intf_signal)
                else:
                    invalid_entry.append(line)
            elif "output" in line:
                check_input = re.sub('\s+', ' ', line.strip()).split(' ')[0]
                if check_input == "output":
                    if "//" in line:
                        port_part, comment_part = line.strip().split('//')
                        port_part = re.sub('\s+', ' ', port_part.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "logic "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Output: " + comment_part + "\n"
                        intf_list.append(intf_signal)
                    else:
                        port_part = re.sub('\s+', ' ', line.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "logic "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Output" + "\n"
                        intf_list.append(intf_signal)
                else:
                    invalid_entry.append(line)
            elif "inout" in line:
                check_input = re.sub('\s+', ' ', line.strip()).split(' ')[0]
                if check_input == "inout":
                    if "//" in line:
                        port_part, comment_part = line.strip().split('//')
                        port_part = re.sub('\s+', ' ', port_part.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "wire  "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Inout : " + comment_part + "\n"
                        intf_list.append(intf_signal)
                    else:
                        port_part = re.sub('\s+', ' ', line.strip()).split(' ')
                        has_bitWidth = False
                        bitWidth = ''
                        signal_names = ''
                        for component in port_part:
                            if component not in keywords:
                                if '[' in component:
                                    bitWidth = component
                                    has_bitWidth = True
                                else:
                                    signal_names = signal_names + " " +component
                        intf_signal = "logic "
                        intf_signal = intf_signal.rjust(8)
                        
                        if signal_names[-1] == ',':
                            signal_names = signal_names[:-1].ljust(32)
                            signal_names = signal_names + ';'
                        else:
                            signal_names = signal_names.ljust(32)
                            signal_names = signal_names + ';'
                        if has_bitWidth:
                            intf_signal = intf_signal + bitWidth
                        
                        intf_signal = intf_signal.ljust(20)
                        intf_signal = intf_signal + signal_names + " // Inout" + "\n"
                        intf_list.append(intf_signal)
                else:
                    invalid_entry.append(line)
            else:
                invalid_entry.append(line)

        if DEBUG_ON:
            sys.exit()

        with open(outFile, 'w') as file:
            intf_name = module_name + "_intf"
            write_string = "`ifndef " + intf_name.upper() + "__SV\n"
            file.write(write_string)
            write_string = "`define " + intf_name.upper() + "__SV\n\n"
            file.write(write_string)
            write_string = "interface " + intf_name + ";\n\n"
            file.write(write_string)
            for line in intf_list:
                file.write(line)
            write_string = "\nendinterface: " + intf_name + "\n"
            file.write(write_string)
            write_string = "`endif\n"
            file.write(write_string)
            write_string = "// End of File: " + intf_name + ".sv"
            file.write(write_string)
        if invalid_entry:
            with open(module_name+"_parse_err.log", 'w') as file:
                file.write("Lines with errors\n\n")
                for line in invalid_entry:
                    file.write(line+"\n")
        print(module_name + " interface generation successfull!!")

def main(argv):
    """docstring for main"""
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('gen_intf.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('gen_intf.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg.strip(" ")
        elif opt in ("-o", "--ofile"):
            outputFile = arg.strip(" ")
    print('Input file is', inputFile)
    print('Output file is', outputFile)
    gen_intf(inputFile, outputFile)

if __name__ == '__main__':
    main(sys.argv[1:])
