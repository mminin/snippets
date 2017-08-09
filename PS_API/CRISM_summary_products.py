## VIVIANO-BECK summary products:

#Product #1: R770 # higher value more dusty or icy # Sensitive to slope effects, clouds
#Note: this product uses *median* of the 5 channels... I don't know how to do median on rasdaman.
#QUESTION: How do i find median on RASDAMAN?
print tqs(f_encode( f_toEncode1S(770) , 'unsigned char', '"jpg"'))

#Product #2: RBR = R770/R440 # Red/blue ratio # higer value indicates more npFeOx # Sensitive to dust in atmosphere
RBRd = f_over(bandName(bandsS(770)),bandName(bandsS(440)))
RBRn = f_times( f_isNotNull(bandName(bandsS(770))), f_isNotNull(bandName(bandsS(440))) )
print tqs(f_encode( f_toEncode( RBRd, RBRn) , 'unsigned char', '"jpg"'))

#Product #3: BD530_2 = BD of 530 over 716 to 440. # Higher value has more fine-grained crystalline hematite
#BD530_2 = 1-(R530/(a*R716+b*R440));
#BD530_2 = 1-(R530/Rc)#Needs function computeRc
#Rc=(a*Rs+b*Rl) # c=530, s=716, l=440
#b=(c-s)/(l-s)
print tqs(f_encode( f_toEncodeBD3S(530,716,440) , 'unsigned char', '"jpg"'))

#Product #4: SH600_2 = 600 shoulder height over 533 to 716 
#Select ferric minerals (scpecially hematite and goethite) or compacted texture) [see Fischer and Pieters 1993]
#Sensitive to high opacity in atmosphere

print tqs(f_encode( f_toEncodeSH3S(600,533,716) , 'unsigned char', '"jpg"'))

print tqs(f_encode( f_toEncodeBD3Sinv(600,533,716) , 'unsigned char', '"jpg"'))

#Product #5: SH770 =  SH775 over 716 to 860 
# Select ferric minerals, less sensitive to LCP than SH600_2
#Sensitive to high opacity in atmosphere

print tqs(f_encode( f_toEncodeSH3S(775,716,860) , 'unsigned char', '"jpg"'))

print tqs(f_encode( f_toEncodeBD3Sinv(775,716,860) , 'unsigned char', '"jpg"'))

#Product #6: BD640_2: BD624 over 600 to 760
# Select ferric minerals (especially maghemite)
# Obscured by VNIR detector artifact

print tqs(f_encode( f_toEncodeBD3S(624,600,760) , 'unsigned char', '"jpg"'))


#Product #7: BD860_2: BD860 over 755 to 977
# Select crystalline ferric minerals (especially hematite)
# Ok

print tqs(f_encode( f_toEncodeBD3S(860,755,977) , 'unsigned char', '"jpg"'))

#Product #8: BD920_2: BD920 over 807 to 984
# Crystalline ferric minerals and LCP
# Ok

print tqs(f_encode( f_toEncodeBD3S(920,807,984) , 'unsigned char', '"jpg"'))
print tqs(f_encode( f_toEncodeBD3Sinv(920,807,984) , 'unsigned char', '"jpg"'))

#Product #9: required fininding the first derivative of a best fit 5th order polynomial. No idea how to do this in Rasdaman

#Product #10: requires Product #9

#Product #11: requires integrating

#Product #12: R1330
# IR albedo: ices > dust > unaltered mafics
# no caveats
print tql(f_encode( f_toEncode1L(1330) , 'unsigned char', '"jpg"'))

#Product #13: BD1300: BD 1320 over 1080 to 1750: (1320,1080,1750)
#1.3 um absorption associated with Fe2+ substitution in plagioclase
#Plagioclase with Fe2+ substitution
#Caveats: Fe-Olivine can be > 0

print tql(f_encode( f_toEncodeBD3L(1320,1080,1750) , 'unsigned char', '"jpg"'))


print tqs(f_encode( f_BandDepthL(1320,1080,1750) , 'unsigned char', '"jpg"'))
#f_BandDepthL(c,s,l)

#Product #14: OLLINDEX3: Detect broad absorption centred at 1 um
#OLINDEX3 = RB1080*0.03+RB1152*0.03+RB1210*0.03+RB1250*0.03+RB1263*0.07+RB1276*0.07+RB1330*0.12+RB1368*0.12+RB1395*0.14+RB1427*0.18+RB1470*0.18
#Where RBx=(RCx-Rx)/RCx, 
#and Rc denotes a value of a pont along point on slope Rc anchored at R1750 and R2400
#Olivines will be strongly > 0
#Caveates HCP, Fe-pyllosilicates
k_Rs = bandName(bandsL(1750))
k_Rl = bandName(bandsL(2400))

#f_R = lambda w: bandName(bandsL(w))
#f_RCx = lambda c,s,l: f_plus( f_times(str(f_waveRatio(c,s,l)),f_minus(f_R(l),f_R(s))),f_R(s) )
#f_RCxOLINDEX3 = lambda c: f_RCx(c, 1750,2400)
f_RBxx = lambda c: f_over(f_minus(f_RCxOLINDEX3(c),f_R(c)), f_RCxOLINDEX3(c)  ) #NEED TO FIX THIS ONE !!!

OLINDEX3raw = '('+f_RBxx(1080)+' * 0.03 + '+f_RBxx(1152)+' * 0.03 + '+f_RBxx(1210)+' * 0.03 +'+f_RBxx(1250)+'* 0.03 +'+f_RBxx(1263)+' * 0.07 + '+f_RBxx(1276)+' * 0.07 + '+f_RBxx(1330)+' * 0.12 + '+f_RBxx(1368)+' * 0.12 + '+f_RBxx(1395)+' * 0.14 + '+f_RBxx(1427)+' * 0.18 + '+f_RBxx(1470)+' * 0.18)'

#f_indexNN = lambda waveList: '(' + ' * '.join( map(lambda c: f_isNotNull(f_R(c)), waveList )) + ')'

OLINDEX3nn = f_indexNN([1750,2400,1080,1152,1210,1250,1263,1276,1330,1368,1395,1427,1470])


print tql(f_encode( f_toEncode(OLINDEX3raw,OLINDEX3nn) , 'float', '"tif"'))


#Product #15: LCPINDEX2: Detect broad absorption centred at 1.81um
#LCPINDEX2: RB1690*0.20+RB1750*0.20+RB1810*0.30+RB1870*0.30; RC anchored at R1560 and R2450
#Pyroxene is strongly +; favors HCP
#Caveats: none

print tql(f_encode( f_toEncodeIndex([(1690,0.20),(1750,0.20),(1810,0.30),(1870,0.30)],1560,2450) , 'int', '"jpg"'))
args = [[(1690,0.20),(1750,0.20),(1810,0.30),(1870,0.30)],1560,2450]
print tql(f_encode( f_times(f_indexRAW(*args),f_indexNN([x[0] for x in args[0]] + [args[1],args[2]])) , 'float', '"tif"'))

#Product #16: HCPINCEX2: Detect broad absorption centred at 2.12 um
#Pyroxene is strongly +; favors HCP
#Caveats: LCP
args = [[(2120,0.10),(2140,0.10),(2230,0.15),(2250,0.30),(2430,0.20),(2460,0.15)],1690,2530]
print tql(f_encode( f_toEncodeIndex(*args) , 'int', '"jpg"'))
#print tql(f_encode( f_times(f_indexRAW(*args),f_indexNN(*args)) , 'float', '"tif"'))
print tql(f_encode( f_times(f_indexRAW(*args),f_indexNN([x[0] for x in args[0]] + [args[1],args[2]])) , 'float', '"tif"'))

#Product #17: 1.0-2.3 um spectral variance
#Requires computing a line of best fit - nearly impossible to do 
#since average value will have to be computed for each 
#point of deviation separately (not possible to buffer value in a variable).

#Product #18: ISLOPE1: spectral slope 1: (R1815-R2530)/(W2530-W1815)
#Don't understand what is W2530 and W1815. Paper provides no explanation.

#Product #19: BD1400: 1395 over 1330 to 1467
#Hydrated or hydroxylated minerals
#No caveats.
print tql(f_encode( f_toEncodeBD3L(1395,1330,1467) , 'unsigned char', '"jpg"'))

#Product #20: BD1435: 1435 over 1370 to 1470
#CO2 ice, some hydrated minerals
#No caveats.
print tql(f_encode( f_toEncodeBD3L(1435,1370,1470) , 'unsigned char', '"jpg"'))

#Product #21: BD1500_2: 1525 over 1367 to 1808
#H2O ice on surface or in atmosphere
#No caveats.
print tql(f_encode( f_toEncodeBD3L(1525,1367,1808) , 'unsigned char', '"jpg"'))

#Product #22: 1 - (1-BD1435)/(1-BD1500_2)
# CO2 H2O mixtures, >1 for more CO2, <1 for more H2O
#No caveats.
print tql(f_encode(f_toEncode(f_minus('1',f_over(f_minus('1', f_BandDepthL(1435,1370,1470)), f_minus('1', f_BandDepthL(1525,1367,1808)))),f_times(nnMaskWL_3(1435,1370,1470),nnMaskWL_3(1525,1367,1808))) , 'unsigned char', '"jpg"'))

print tql(f_encode(f_toEncode(f_minus('1',f_over(f_minus('1', f_BandDepthL(1435,1370,1470)), f_minus('1', f_BandDepthL(1525,1367,1808)))),f_times(nnMaskWL_3(1435,1370,1470),nnMaskWL_3(1525,1367,1808))) , 'float', '"tif"'))

#Product #23: BD1750_2: 1750 over 1690 to 1815
#Gypsum Alunite
#No caveats.
print tql(f_encode( f_toEncodeBD3L(1750,1690,1815) , 'unsigned char', '"jpg"'))

#Product #24: 0.5*BD(1930,1850,2067)+0.5*BD(1985,1850,2067) = 0.5*(BD(1930,1850,2067)+BD(1985,1850,2067))
#Bound molecular H2O except monohydrated sulfates
#No caveats.
k_mean_BD1930_BD1985 = f_times('0.5',f_plus(f_BandDepthL(1930,1850,2067),f_BandDepthL(1985,1850,2067)))
k_mean_BD1930_BD1985_nn = f_times(nnMaskWL_3(1930,1850,2067),nnMaskWL_3(1985,1850,2067))
f_toEncode(k_mean_BD1930_BD1985, k_mean_BD1930_BD1985_nn)
print tql(f_encode( f_toEncode(k_mean_BD1930_BD1985, k_mean_BD1930_BD1985_nn) , 'unsigned char', '"jpg"'))

#Product #25: BD1900r2: 1.9um H2O band depth
#H2O
#No caveats.
# 1-( RRC1908 +RRC1914 +RRC1921 +RRC1928 +RRC1934 +RRC1941 ) / ( RRC1862 +RRC1869 +RRC1875 +RRC2112 +RRC2120 +RRC2126 )
# Where RRCxxxx = Rxxxx / RCxxxx, slope RC anchored at R1850 and R2060.
#f_RCx = lambda c,s,l: f_plus( f_times(str(f_waveRatio(c,s,l)),f_minus(f_R(l),f_R(s))),f_R(s) )
BD1900r2NN = f_indexNN([1908,1914,1921,1928,1934,1941,1862,1869,1875,2112,2120,2126],1850,2060)
BD1900r2NumerList = [1908,1914,1921,1928,1934,1941] 
BD1900r2DenomList = [1862,1869,1875,2112,2120,2126]
BD1900r2 = f_minus('1',f_over(f_sumRRCx(BD1900r2NumerList,1850,2060),f_sumRRCx(BD1900r2DenomList,1850,2060)))
print tql(f_encode( f_toEncode(BD1900r2, BD1900r2NN) , 'unsigned char', '"jpg"'))
print tql(f_encode( f_toEncode(BD1900r2, BD1900r2NN) , 'float', '"tif"'))

#Product #26: BDI2000: requires integration

#Product #27: BD2100_2: 2132 over 1930 to 2250
#H2O in monohydrated sulfates
#Caveats: Alunite, Serpentine
print tql(f_encode( f_toEncodeBD3L(2132,1930,2250) , 'unsigned char', '"jpg"')) #IS SOMETHING WRONG HERE? HOW COME ALL L BAND DEPTHS LOOK MESSED UP?

#Product #28: BD2165: 2165 over 2120 to 2230
#Pyrophyllite Kaolinite group
#Caveats: Beidellite, Allophane, Imogolite
print tql(f_encode( f_toEncodeBD3L(2165,2120,2230) , 'unsigned char', '"jpg"')) #PERHAPS JUST THE DATA IS VERY POOR (NOISY)

#Product #29: BD2190: 2185 over 2120 to 2250
#Beidellite, Allophane, Imogolite
#Caveats: Kaolinite group
print tql(f_encode( f_toEncodeBD3L(2185,2120,2250) , 'unsigned char', '"jpg"'))
print tql(f_encode( f_toEncode(f_BandDepthL(2185,2120,2250), f_indexNN([2185,2120,2250]) ), 'unsigned char', '"jpg"')) #it's same as above

#Product #30: MIN2200: minimum[BD(2165,2120,2350),BD(2210,2120,2350)]
#Kaolinite group
#No caveats.
print tql(f_encode( f_toEncode( f_minimum(f_BandDepthL(2165,2120,2350),f_BandDepthL(2210,2120,2350)), f_indexNN([2165,2120,2350,2210])), 'unsigned char', '"jpg"'))

#Product #31: BD2210_2: 2210 over 2165 to 2250
#Al-OH minerals
#Caveats: Gypsum, Alunite
print tql(f_encode( f_toEncodeBD3L(2210,2165,2250) , 'unsigned char', '"jpg"'))

#Product #32: D2200: 2.2um dropoff: 1-(RRC2210+RRC2230)/(2*RRC2165), RC anchored at R1815 and R2430
#Al-OH minerals
#Caveats: Chlorite, Prehnite
print tql(f_encode( f_toEncode(f_over(f_sumRRCx([2210,2230],1815,2430), f_times('2', f_RRCx(2165,1815,2430))), f_indexNN([2210,2230,2165,1815,2430])), 'unsigned char', '"jpg"'))

#Product #33: BD2230: 2235 over 2210 to 2252
#Hydroxylated ferric sulfate
#Caveats: Other Al-OH minerals
print tql(f_encode( f_toEncodeBD3L(2235,2210,2252) , 'unsigned char', '"jpg"'))

#Product #34: BD2250: 2245 over 2120 to 2340
#Opal and other Al-OH minerals
#No Caveats
print tql(f_encode( f_toEncodeBD3L(2245,2120,2340) , 'unsigned char', '"jpg"'))

#Product #35: MIN2250: min(BD(2210,2165,2350),BD(2265,2165,2350)):
#Opal
#No caveats
print tql(f_encode( f_toEncode( f_minimum(f_BandDepthL(2210,2165,2350),f_BandDepthL(2265,2165,2350)), f_indexNN([2210,2165,2350,2265])), 'unsigned char', '"jpg"'))

#Product #36: BD2265: 2265 over 2210 to 2340
#Jarosite, Gibbsite, Acid-leached nontronite
#No caveats
print tql(f_encode( f_toEncodeBD3L(2265,2120,2340) , 'unsigned char', '"jpg"'))

#Product #37: BD2290: 2290,2250,2350
#Mg, Fe-OH minerals; Also CO2 ice
#Caveats: Mg-Carbonate
print tql(f_encode( f_toEncodeBD3L(2290,2250,2350) , 'unsigned char', '"jpg"'))

#Product #38: D2300: 2.3 um dropoff
# 1-RRCsum(2290,2320,2330)/RRCsum(2120,2170,2210), anchored at R1815 and R2530
#Hydroxylated Fe, Mg, slilcates strongly > 0
#Caveats: Mg-Carbonate
print tql(f_encode( f_toEncode(f_minus('1',f_over(f_sumRRCx([2290,2320,2330],1815,2530),f_sumRRCx([2120,2170,2210],1815,2530))),f_indexNN([2290,2320,2330,1815,2530,2120,2170,2210])), 'unsigned char', '"jpg"'))

#Product #39: BD2355: 2355, 2300 2450
#Chlorite, Prehnite, Pumpellyite
#Caveats: Carbonate, Serpentine
print tql(f_encode( f_toEncodeBD3L(2355, 2300, 2450) , 'unsigned char', '"jpg"'))

#Product #40: SINDEX2: SH(2290,2120,2400)
#Hydrated sulfates (mono and polyhydrated sulfates) will be strongly > 0
#Caveats: Ices.
print tql(f_encode( f_toEncodeSH3L(2290,2120,2400) , 'unsigned char', '"jpg"'))

#Product #41: ICER2_2: RB2600, anchored at R2456 R2530
#CO2 versus water ice/soil; CO2 will be strongly > 0, water ice will be <0.
#No caveats
print tql(f_encode( f_toEncode(f_RBx(2600,2456,2530),f_indexNN([2600,2456,2530])), 'unsigned char', '"jpg"'))

#Product #42: MIN2295_2480: Mg Carbonate overtone band depth and metal-OH band
#Minimum[BD(2295,2165,2364), BD(2480,2364,2570)]
#Mg carbonates; both overtones must be present
#Caveats: Hydroxylated silicate + zeolite mixtures
print tql(f_encode( f_toEncode( f_minimum(f_BandDepthL(2295,2165,2364),f_BandDepthL(2480,2364,2570)), f_indexNN([2295,2165,2364,2480,2570])), 'unsigned char', '"jpg"'))

#Product #43: MIN2345_2537: Ca/Fe Carbonate overtone band depth and metal-OH band:
#Minimum[BD(2345,2250,2430), BD(2537,2430,2602)]
#Ca/Fe carbonates; both overtones must be present
#Caveats: Prehnite, Serpentine, Hydroxylated silicate+zeolite mixtures.
print tql(f_encode( f_toEncode( f_minimum(f_BandDepthL(2345,2250,2430),f_BandDepthL(2537,2430,2602)), f_indexNN([2250,2345,2430,2537,2602])), 'unsigned char', '"jpg"'))

#Product #44: BD2500_2: Mg Carbonate overtone band depth: BD(2480,2364,2570)
#Mg carbonates 
#Caveates: Some zeolites
print tql(f_encode( f_toEncodeBD3L(2480,2364,2570) , 'unsigned char', '"jpg"'))


#Product #45: BD3000: 3um H2O band depth:
#1-R3000/(R2530*(R2530/R2210))=1-(R3000*R2210)/(R2530*R2530)
#Bound H2O (accounts for spectral slope)
#No caveats
print tql(f_encode( f_toEncode( f_minus('1',f_over(f_times(f_Rl(3000),f_Rl(2210)),f_times(f_Rl(2530),f_Rl(2530)))), f_indexNN([3000,2210,2530,2530])), 'unsigned char', '"jpg"'))

#Product #46: BD3100: 3.1um H2O ice band depth: BD(3120,3000,3250)
#H2O ice
#No caveates
print tql(f_encode( f_toEncodeBD3L(3120,3000,3250) , 'unsigned char', '"jpg"'))

#Product #47: BD3200: 3.2um CO2 ice band depth: BD(3320,3250,3390)
#CO2 ice
#No caveates
print tql(f_encode( f_toEncodeSH3L(3320,3250,3390) , 'unsigned char', '"jpg"'))

#Product #48: BD3400_2: 3.4 um carbonate band depth: BD(3420,3250,3630)
#Carbonates
#No caveates
print tql(f_encode( f_toEncodeBD3L(3420,3250,3630) , 'unsigned char', '"jpg"'))

#Product #49: CINDEX2: Inverse lever rule to detect convexity at 3.6 um due to 3.4 um and 3.9 um absorptions
#SH(3610,3450,3875)
#Carbonates will be >'background' values > 0
print tql(f_encode( f_toEncodeSH3L(3610,3450,3875) , 'unsigned char', '"jpg"'))
print tql(f_encode( f_toEncode(f_ShoulderHeightL(3610,3450,3875), f_indexNN([3610,3450,3875])), 'unsigned char', '"jpg"'))

### ATMOSPHERIC PARAMETERS AND BROUWSE PRODUCT COMPONENTS # No caveats
#now is a good time to do some noise filtering, kernels are averaged by median, not mean.
#so we need to find the minimum value, maximum value, and take the one in-between.

#Product #50: R440 (kernel width 5)
#Clouds / Hazes
print tqs(f_encode( f_toEncode(f_med5s(440), f_med5sNN(440)), 'unsigned char', '"jpg"'))
print tqs(f_encode( f_med5s(440), 'float', '"tif"'))

#Product #51: R530 (kernel width 5)
#TRU browse product component
print tqs(f_encode( f_toEncode(f_med5s(530), f_med5sNN(530)), 'unsigned char', '"jpg"'))

#Product #52: R600 (kernel width 5)
#TRU browse product component
print tqs(f_encode( f_toEncode(f_med5s(600), f_med5sNN(600)), 'unsigned char', '"jpg"'))

#Product #53: IR ratio 1: R800 / R997 (kernel width 5)
#Aphelion ice clouds (>1) versus seasonal or dust (<1)
print tqs(f_encode( f_toEncode(f_med5s(800)+'/'+f_med5s(997), f_med5sNN(800)+'*'+f_med5sNN(997)), 'unsigned char', '"jpg"'))
print tqs(f_encode( '('+f_med5s(800)+'/'+f_med5s(997)+')*' + f_med5sNN(800)+'*'+f_med5sNN(997), 'float', '"tif"'))

#Product #54: R1080 (kernel width 5) 
#FAL browse product
print tql(f_encode( f_toEncode(f_med5l(1050), f_med5lNN(1050)), 'unsigned char', '"jpg"'))

#Product #55: R1506 (kernel width 5) 
#FAL browse product
print tql(f_encode( f_toEncode(f_med5l(1506), f_med5lNN(1506)), 'unsigned char', '"jpg"'))

#Product #56: R2529 (kernel width 5) 
#TAN browse product
print tql(f_encode( f_toEncode(f_med5l(2529), f_med5lNN(2529)), 'unsigned char', '"jpg"'))

#Product #57: BD2600 (kernel width 5): 2600,2530,2630
#H2O vapour (accounts for spectral slope

print tql(f_encode( f_toEncodeBD3L(2600,2530,2630) , 'unsigned char', '"jpg"'))
print tql(f_encode( f_toEncodeBD3L(2600,2530,2630) , 'float', '"tif"'))

print tql(f_encode( f_toEncode(f_BandDepthLMed(2600,2530,2630), f_BandDepthLMedNN(2600,2530,2630) ), 'unsigned char', '"jpg"'))
print tql(f_encode( f_toEncode(f_BandDepthLMed(2600,2530,2630), f_BandDepthLMedNN(2600,2530,2630) ), 'float', '"tif"'))
print tql(f_encode( f_BandDepthLMed(2600,2530,2630)+'*'+f_BandDepthLMedNN(2600,2530,2630), 'float', '"tif"'))
print tql(f_encode( f_BandDepthL(2600,2530,2630)+'*'+f_indexNN([2600,2530,2630]), 'float', '"tif"'))

print tql(f_encode(f_BandDepthLMed(3420,3250,3630) , 'float', '"tif"'))



print tql(f_encode( f_BandDepthRcLMed(3420,3250,3630) , 'float', '"tif"'))

print tql(f_encode( f_BandDepthInvLMed(3420,3250,3630) , 'float', '"tif"'))


#Product #58: IR ratio 2: R2530 / R2210 (kernel width 5)
#Aphelion ice clouds versus seasonal or dust
print tql(f_encode( '('+f_med5l(2530)+'/'+f_med5l(2210)+')*' + f_med5lNN(2530)+'*'+f_med5lNN(2210), 'float', '"tif"'))

#Product #59: IR ratio 3: R3500 / R3390 (kernel width 5)
#Aphelion ice clouds (higher values) versus seasonal or dust
print tql(f_encode( '('+f_med5l(3500)+'/'+f_med5l(3390)+')*' + f_med5lNN(3500)+'*'+f_med5lNN(3390), 'float', '"tif"'))
print tql(f_encode( f_toEncode(f_med5l(3500)+'/'+f_med5l(3390), f_med5lNN(3500)+'*'+f_med5lNN(3390)), 'unsigned char', '"jpg"'))

#Product #60: R3920 (kernel width 5) 
#IC2 browse product component
print tql(f_encode( f_med5l(3920)+'*'+ f_med5lNN(3920), 'float', '"tif"'))


print tql(f_encode( f_med5l(3920)+'*'+ f_med5lNN(3920), 'float', '"tif"'))

print tql(f_encode( f_toEncode1L(3920) , 'unsigned char', '"jpg"'))





print tql(f_encode( f_toEncode(f_med5l(2529), f_med5lNN(2529)), 'unsigned char', '"jpg"'))




######NOTES:
##TEST RUN RGB:

print tqs(f_encodeRGB(f_toEncodeBD3S(530,716,440),f_toEncodeSH3S(600,533,716),f_toEncode1S(770), 'unsigned char', '"jpg"')) 


print tqs(f_encodeRGB(k_BD530_2_toEncode,k_SH600_2_toEncode,k_R770_toEncode, 'unsigned char', '"jpg"')) #Produces very clear image with flows





print tqs(f_encodeRGB(k_SH770_toEncode+'*0.7',k_BD600_2_toEncode,k_BD530_2_toEncode, 'unsigned char', '"jpg"')) #Not very clear due to noise in SH770
print tqs(f_encodeRGB(k_BD640_2_toEncode,k_BD600_2_toEncode,k_BD530_2_toEncode, 'unsigned char', '"jpg"'))
print tqs(f_encodeRGB(k_BD920_2_toEncode,k_BD860_2_toEncode,k_SH770_toEncode, 'unsigned char', '"jpg"')) # This one looks pretty

##CRATERS:
#http://epn1.epn-vespa.jacobs-university.de:8080/subGranule/index.html?cov=hrl00005c6c_07_if182l_trr3&c1_min=22.336&c1_min=22.336&c1_max=22.598&c2_min=10.159&c2_max=10.56&E_px=424&N_px=653&sensor_id=l
#hrl00005c6c_07_if182l_trr3
tqs = lambda q: getQuery('hrl00005c6c_07_if182l_trr3', q)

tqs = lambda q: getQuery('frt00006867_07_if166s_trr3', q)
