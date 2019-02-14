
		#elif "next" in addressdata[sira]:
			#yerlestirme=yerlestirme+1
		
		#elif "end" not in addressdata[sira]:
				#print('edit yok else çalıştı ******************** array işleri')
				s=0
				while "next" not in addressdata[yerlestirme]:
					print("satır  :",sira,"kural :",yerlestirme,"array:",array_basi,s,".member degeri",)
					print(address_raw[array_basi][s])
					address_raw[array_basi][s]=addressdata[yerlestirme]
					s=s+1
					yerlestirme+=1
				yerlestirme=yerlestirme+1
				#print("while dan cikti :", yerlestirme)
		

		
		#print(address_raw)
		
		