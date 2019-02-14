#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script gets address database and 
selects an address group extracts the ip 
addressesin a sorted state with whois information."""

__author__      = "Mesut Bayrak"
__copyright__   = "Copyright 2016, Planet Earth"

import sys
#from tabulate import tabulate
import os

def readconfigfile(file_name):
	satirlar=[]
	f = open(file_name,'r')
	for line in f:
		satirlar.append(line)
	return satirlar
def burda_dur(mesaj):
	try:
		input(mesaj)
	except SyntaxError:
		pass


def getvdoms(wholeconfig):
	vdoms=[]
	vdom_line=[]
	c=-1
	for line in wholeconfig:
		c=c+1
		if "config vdom" in wholeconfig[c]:
			vdoms.append((wholeconfig[c+1].strip('edit ').strip('\n'),c))
	#print("vdomlariniz :", vdoms)	
	return vdoms
 

def getaddreses_invdom(addressdata,vdom_start,vdom_end):
	address_start=0
	address_end=0

	x=vdom_start -1 
	for d in range(vdom_start,vdom_end):	
		x=x+1
		if addressdata[x].lstrip() == 'config firewall address\n': 
			#print(x)
			#print(addressdata[x].lstrip())
			address_start=x
		else:
			if addressdata[x].lstrip() == 'config firewall multicast-address\n': 
				#print(x)
				#print(addressdata[x].lstrip())
				address_end=x-1
	return address_start,address_end
		
def getaddreses(addressdata,*lines):

	lines_start=int(lines[0][0])
	lines_stop=int(lines[0][1])
	rule_count=0
	k=lines_stop-lines_start
	print("satir_sayisi :",k)

	for rules_1 in range (lines_start,lines_stop):
		if "edit" in addressdata[rules_1]:
			rule_count=rule_count+1
	"""
	İlgili vdom'daki rule sayısını yukarıda buluyorum.
	"""
	print('Rule sayısı = ',rule_count)
	w, h = 31, rule_count;
	address_raw = [[0 for x in range(w)] for y in range(h)] 
	array_basi=-1
	yerlestirme=lines_start+1
	print(yerlestirme)
#'''
#|subnet|Geography|iprange|FQDN|Wildcard-FQDN|Dynamic-Sdn-Address|
#'''
	for sira in range (lines_start,lines_stop): # 6961- 10873

		if "edit" in addressdata[yerlestirme]:
			array_basi+=1
			temiz_kural =addressdata[yerlestirme]
			address_raw[array_basi][0]=temiz_kural.strip('edit  ').strip("\"\n")
			yerlestirme+=1
		
			
		elif "uuid" in addressdata[yerlestirme]:
			address_raw[array_basi][2]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		
		elif "visibility" in addressdata[yerlestirme]:
			address_raw[array_basi][3]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1

####    Subnet  dizilimleri
		elif "subnet" in addressdata[yerlestirme]:
			address_raw[array_basi][4]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1

####    IP RANGE dizilimleri
		elif "type iprange" in addressdata[yerlestirme]:
			address_raw[array_basi][22]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		elif "start-ip" in addressdata[yerlestirme]:
			address_raw[array_basi][23]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		elif "end-ip" in addressdata[yerlestirme]:
			address_raw[array_basi][24]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1

####    FQDN dizilimleri
		elif "type fqdn" in addressdata[yerlestirme]:
			address_raw[array_basi][25]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		elif "fqdn \"" in addressdata[yerlestirme]:
			address_raw[array_basi][26]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		
####    Wildcard FQDN dizilimleri
		elif "type wildcard-fqdn" in addressdata[yerlestirme]:
			address_raw[array_basi][27]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		elif "wildcard-fqdn \"" in addressdata[yerlestirme]:
			address_raw[array_basi][28]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		
		elif "comment" in addressdata[yerlestirme]:
			address_raw[array_basi][29]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		
		elif "associated-interface" in addressdata[yerlestirme]:
			address_raw[array_basi][30]=addressdata[yerlestirme].strip('        ')
			yerlestirme+=1
		
		elif "next" in addressdata[yerlestirme]:
			yerlestirme+=1


		else:
			yerlestirme+=1
		
		# os.system('clear') 
		# print('satır no  :', sira,'yerlestirme',yerlestirme)
		# print('satır:',addressdata[yerlestirme])
		# print('address_raw',address_raw[array_basi])
		# burda_dur('döngü')
		
	return address_raw

		 #wildcard-fqdn
		 #iprange
		 #subnet
def getgroups(linestart,linestop):
	pass

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
else:
    mesaj = 'Girdiğiniz dosya ({})'
    print(mesaj.format(sys.argv[1]))
    icerik=readconfigfile(sys.argv[1])
    vdomlar=getvdoms(icerik)
    print("Kullanilan vdomlar :",vdomlar)
    
    addres_arailk=getaddreses_invdom(icerik,vdomlar[2][1],vdomlar[3][1])
    print("ARVATO vdom adres araligi : ",addres_arailk)
    
    adresler=getaddreses(icerik,addres_arailk)
    #print(adresler)
    array_length = len(adresler)
    print(array_length)
   
    for x in adresler:
    	print(x)

    # 	print('\n')
   












