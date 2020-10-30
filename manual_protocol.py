
​
def ManualFunctionProtocol(inputDictionary,protocolType):
    """This function takes in a dictionary with all the inputs to run a manual protocol
    as well as a string that defines whether you run a BASIC, GG or BioBricks assembly"""
        
    
    GGProtocol=("1)Add buffer_vol of Buffer and water_vol of water \n2) Add linearised Vector Backbone and inserts (required mass insert (g) = desired insert/vector molar ratio x mass of vector (g) x ratio of insert to vector lengths) \n3)Add ENZYME_VOL of the restriction enzyme and LIGASE_VOL of the ligation enzyme \n4) Place Solution (if ligating less than four fragments) in the Thermocycler for: \n \t a.37°C for 2-4h \n  \t b.50°C for 5 minutes \n \t c.80°C for 10 minutes \n4) If working with more than three fragments place in thermocycler for: \n\ta.50 cycles 37°C for 2min, 16°C for 5min\n\tb. 50°C for 5min (only once) \n\tc. 80°C for 10min (only once)")
    
    BasicProtocol="1)Add Buffer (T4_BUFF_VOL  + CLIP_MAST_WATER ) \n2)Add Bsa1 and T4 ligase (BSAI_VOL , T4_LIG_VOL) \n3)Add iP and iS linkers (100μM) \n4)Add DNA Part at a concentration of 50ng/μl per kb of the storage plasmid. \n5)Thermocycler \n \t a.37°C for 1 hour\n \t b.20°C for 20minutes \n \t c.65°C for 20 minutes\n6)Purification (magnetic bead purification or other)\n7)Assembly: \n \t a.Add purified DNA parts + BSA +NEB4 +dH20\n8)Thermocycler:\n \t a.Incubate at 50°C for 45 minutes"
    
    BioBricksProtocol="1)Add BioBrick parts and the destination plasmid\n2)Add (water) of H20 and NEBBuffer10x of buffer to each tube\n3)Add appropriate restriction enzymes in order: EcoRI, Spel, Xbal,Pstl (EcoRI-HF, SpeI, XbaI,PstI)\n4)Thermocycler:\n \ta.37°C for 30 minutes\n \tb.80°C for 20 minutes \n5)Mix the digests together and add H20: (water?) ligase buffer: T4Ligase10x and T4Ligase of ligase\n6)Thermocycler:\n \ta.Room temperature 30minutes\n \tb.80°C for 20 minutes"
   
    if protocolType=="BASIC":
        BasicProtocol=BasicProtocol.replace('T4_BUFF_VOL ',"T4 volume " + inputDictionary["T4_BUFF_VOL"])
        BasicProtocol=BasicProtocol.replace('BSAI_VOL ',"BsaI volume " + inputDictionary["BSAI_VOL"])
        BasicProtocol=BasicProtocol.replace('T4_LIG_VOL',"T4 volume " + inputDictionary["T4_LIG_VOL"])
        BasicProtocol=BasicProtocol.replace('CLIP_MAST_WATER',"water volume " + inputDictionary["CLIP_MAST_WATER"])
        #CLIP_MAST_WATER is the incorrect variable check with gaby
        print(BasicProtocol)
        return BasicProtocol
​
    elif protocolType=="GG":
        #GGProtocol=GGProtocol.replace('buffer_vol ', + inputDictionary["buffer_vol"])
        #GGProtocol=GGProtocol.replace('water_vol ', + inputDictionary["water_vol"])
        #GGProtocol=GGProtocol.replace('ENZYME_VOL ', + inputDictionary["ENZYME_VOL"])
        #GGProtocol=GGProtocol.replace('LIGASE_VOL ', + inputDictionary["LIGASE_VOL"])
        #GGProtocol=GGProtocol.replace('ENZYME_VOL ', + inputDictionary["ENZYME_VOL"])
​
        print(GGProtocol)
        return GGProtocol
        
    elif protocolType=="BioBricks":
        BioBricksProtocol=BioBricksProtocol.replace('water' ,"water volume:" +inputDictionary["water"])
        BioBricksProtocol=BioBricksProtocol.replace('NEBBuffer10x' ,"NEBBuffer10x volume:" + inputDictionary["NEBBuffer10x"])
        BioBricksProtocol=BioBricksProtocol.replace('EcoRI-HF',"EcorRI-HF volume:" + inputDictionary["EcoRI-HF"])
        BioBricksProtocol=BioBricksProtocol.replace('Spel',"Spel volume:" + inputDictionary["Spel"])
        BioBricksProtocol=BioBricksProtocol.replace('Xbal',"Xbal volume:" + inputDictionary["Xbal"])
        BioBricksProtocol=BioBricksProtocol.replace('Pstl',"Pstl volume:" + inputDictionary["Pstl"])
        BioBricksProtocol=BioBricksProtocol.replace('T4Ligase',"T4Ligase volume:" + inputDictionary["T4Ligase"])
        print(BioBricksProtocol)
        return BioBricksProtocol
        
    else: 
        print("Invalid protocolType")
        return("ERROR")
​
    
    
Dict = {"T4_BUFF_VOL": '1ml', "BSAI_VOL": '2ml', "T4_LIG_VOL": '3ml', "CLIP_MAST_WATER" : "4ml"} 
ManualFunctionProtocol(Dict,"BASIC")
​
​
print("\n\n\n")
Dict = {"water": '1ml', "NEBBuffer10x": '2ml', "EcoRI-HF": '3ml', "Spel" : "4ml", "Xbal": "5ml", 'Pstl': "7ml", "T4Ligase" : "8ml"} 
ManualFunctionProtocol(Dict,"BioBricks")
print("\n\n\n")
​
​
Dict = {"water": '1ml', "NEBBuffer10x": '2ml', "EcoRI-HF": '3ml', "Spel" : "4ml", "Xbal": "5ml", 'Pstl': "7ml", "T4Ligase" : "8ml"} 
ManualFunctionProtocol(Dict,"GG")