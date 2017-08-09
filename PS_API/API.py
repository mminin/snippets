COVERAGE = 'frt0000b385_07_if164'

#get band name from wavelength
bandsS = lambda nm: int((nm - 362    ) / 6.458 + 1.5)
bandsL = lambda nm: int((nm - 1001.35) / 6.55  + 1.5)# depricated (incorrect, use lookup table instead)
bandsLList=[1.00135, 1.0079, 1.01445, 1.021, 1.02755, 1.0341, 1.04065, 1.0472, 1.05375, 1.0603, 1.06685, 1.07341, 1.07996, 1.08651, 1.09307, 1.09962, 1.10617, 1.11273, 1.11928, 1.12584, 1.13239, 1.13895, 1.14551, 1.15206, 1.15862, 1.16518, 1.17173, 1.17829, 1.18485, 1.19141, 1.19797, 1.20453, 1.21109, 1.21765, 1.22421, 1.23077, 1.23733, 1.24389, 1.25045, 1.25701, 1.26357, 1.27014, 1.2767, 1.28326, 1.28983, 1.29639, 1.30295, 1.30952, 1.31608, 1.32265, 1.32921, 1.33578, 1.34234, 1.34891, 1.35548, 1.36205, 1.36861, 1.37518, 1.38175, 1.38832, 1.39489, 1.40145, 1.40802, 1.41459, 1.42116, 1.42773, 1.43431, 1.44088, 1.44745, 1.45402, 1.46059, 1.46716, 1.47374, 1.48031, 1.48688, 1.49346, 1.50003, 1.50661, 1.51318, 1.51976, 1.52633, 1.53291, 1.53948, 1.54606, 1.55264, 1.55921, 1.56579, 1.57237, 1.57895, 1.58552, 1.5921, 1.59868, 1.60526, 1.61184, 1.61842, 1.625, 1.63158, 1.63816, 1.64474, 1.65133, 1.65791, 1.66449, 1.67107, 1.67766, 1.68424, 1.69082, 1.69741, 1.70399, 1.71058, 1.71716, 1.72375, 1.73033, 1.73692, 1.74351, 1.75009, 1.75668, 1.76327, 1.76985, 1.77644, 1.78303, 1.78962, 1.79621, 1.8028, 1.80939, 1.81598, 1.82257, 1.82916, 1.83575, 1.84234, 1.84893, 1.85552, 1.86212, 1.86871, 1.8753, 1.8819, 1.88849, 1.89508, 1.90168, 1.90827, 1.91487, 1.92146, 1.92806, 1.93465, 1.94125, 1.94785, 1.95444, 1.96104, 1.96764, 1.97424, 1.98084, 1.98743, 1.99403, 2.00063, 2.00723, 2.01383, 2.02043, 2.02703, 2.03363, 2.04024, 2.04684, 2.05344, 2.06004, 2.06664, 2.07325, 2.07985, 2.08645, 2.09306, 2.09966, 2.10627, 2.11287, 2.11948, 2.12608, 2.13269, 2.1393, 2.1459, 2.15251, 2.15912, 2.16572, 2.17233, 2.17894, 2.18555, 2.19216, 2.19877, 2.20538, 2.21199, 2.2186, 2.22521, 2.23182, 2.23843, 2.24504, 2.25165, 2.25827, 2.26488, 2.27149, 2.2781, 2.28472, 2.29133, 2.29795, 2.30456, 2.31118, 2.31779, 2.32441, 2.33102, 2.33764, 2.34426, 2.35087, 2.35749, 2.36411, 2.37072, 2.37734, 2.38396, 2.39058, 2.3972, 2.40382, 2.41044, 2.41706, 2.42368, 2.4303, 2.43692, 2.44354, 2.45017, 2.45679, 2.46341, 2.47003, 2.47666, 2.48328, 2.4899, 2.49653, 2.50312, 2.50972, 2.51632, 2.52292, 2.52951, 2.53611, 2.54271, 2.54931, 2.55591, 2.56251, 2.56911, 2.57571, 2.58231, 2.58891, 2.59551, 2.60212, 2.60872, 2.61532, 2.62192, 2.62853, 2.63513, 2.64174, 2.64834, 2.65495, 2.66155, 2.66816, 2.67476, 2.68137, 2.68798, 2.69458, 2.70119, 2.76068, 2.76729, 2.7739, 2.78052, 2.78713, 2.79374, 2.80035, 2.80697, 2.81358, 2.8202, 2.82681, 2.83343, 2.84004, 2.84666, 2.85328, 2.85989, 2.86651, 2.87313, 2.87975, 2.88636, 2.89298, 2.8996, 2.90622, 2.91284, 2.91946, 2.92608, 2.9327, 2.93932, 2.94595, 2.95257, 2.95919, 2.96581, 2.97244, 2.97906, 2.98568, 2.99231, 2.99893, 3.00556, 3.01218, 3.01881, 3.02544, 3.03206, 3.03869, 3.04532, 3.05195, 3.05857, 3.0652, 3.07183, 3.07846, 3.08509, 3.09172, 3.09835, 3.10498, 3.11161, 3.11825, 3.12488, 3.13151, 3.13814, 3.14478, 3.15141, 3.15804, 3.16468, 3.17131, 3.17795, 3.18458, 3.19122, 3.19785, 3.20449, 3.21113, 3.21776, 3.2244, 3.23104, 3.23768, 3.24432, 3.25096, 3.2576, 3.26424, 3.27088, 3.27752, 3.28416, 3.2908, 3.29744, 3.30408, 3.31073, 3.31737, 3.32401, 3.33066, 3.3373, 3.34395, 3.35059, 3.35724, 3.36388, 3.37053, 3.37717, 3.38382, 3.39047, 3.39712, 3.40376, 3.41041, 3.41706, 3.42371, 3.43036, 3.43701, 3.44366, 3.45031, 3.45696, 3.46361, 3.47026, 3.47692, 3.48357, 3.49022, 3.49687, 3.50353, 3.51018, 3.51684, 3.52349, 3.53015, 3.5368, 3.54346, 3.55011, 3.55677, 3.56343, 3.57008, 3.57674, 3.5834, 3.59006, 3.59672, 3.60338, 3.61004, 3.6167, 3.62336, 3.63002, 3.63668, 3.64334, 3.65, 3.65667, 3.66333, 3.66999, 3.67665, 3.68332, 3.68998, 3.69665, 3.70331, 3.70998, 3.71664, 3.72331, 3.72998, 3.73664, 3.74331, 3.74998, 3.75665, 3.76331, 3.76998, 3.77665, 3.78332, 3.78999, 3.79666, 3.80333, 3.81, 3.81667, 3.82335, 3.83002, 3.83669, 3.84336, 3.85004, 3.85671, 3.86339, 3.87006, 3.87673, 3.88341, 3.89008, 3.89676, 3.90344, 3.91011, 3.91679, 3.92347, 3.93015, 3.93682, 4.0]
bandsLListA = [int(a*1000+0.5) for a in bandsLList]
bandsLListAw = lambda w: min(bandsLListA, key=lambda x:abs(x-w))
bandsL=lambda w: bandsLListA.index(bandsLListAw(w))+1


bandName = lambda band: 'data.band_' + str(band)
f_R = lambda w: bandName(bandsL(w))

WCPSaccess = 'http://access.planetserver.eu:8080/rasdaman/ows?service=WCS&version=2.0.1&request=ProcessCoverages&query='
getQuery = lambda c, q: WCPSaccess + 'for data in ( ' + c + ' ) return ' + q + ';'
tql = lambda q: getQuery(COVERAGE + 'l_trr3', q)
tqs = lambda q: getQuery(COVERAGE + 's_trr3', q)

f_add     = lambda d: 'add(' + d + ')'# total sum of all points #these should be replaced with maps
f_avg     = lambda d: 'avg(' + d + ')'
f_min     = lambda d: 'min(' + d + ')'
f_max     = lambda d: 'max(' + d + ')'

#f_count   = lambda d: 'count(' + d + ')' # number of points in b ==> i think this counts how many elements are not zero. It doesn't quite work
#f_some    = lambda d: 'some(' + d + ')'  # is there any point in b with value true ==> no idea what this does
#f_all     = lambda d: 'all(' + d + ')'  # is there any point in b with value true  ==> no idea what that does either

f_sq      = lambda d: '((' + d + ') * (' + d + '))'
f_sqrt    = lambda d: 'sqrt(' + d + ')'
f_isnot   = lambda d, n: '(' + d + '!=' + n + ')'

#encoding
f_encode = lambda d, o_type, o_format: ' encode(' + '(' + o_type +') ' + d + ', ' + o_format + ',"nodata=null")'
f_channelRGB = lambda r,g,b,t: '{red:'+'('+t+')('+r+');green:'+'('+t+')('+g+');blue:'+'('+t+')('+b+')}'
f_encodeRGB = lambda r,g,b,o_type,o_format: ' encode('+f_channelRGB(r,g,b,o_type)+',' + o_format + ',"nodata=null")'

#arithmetic
f_times = lambda a,b: '(' + a + ' * ' + b + ')'
f_over  = lambda a,b: '(' + a + ' / ' + b + ')'
f_minus = lambda a,b: '(' + a + ' - ' + b + ')'
f_plus  = lambda a,b: '(' + a + ' + ' + b + ')'


# USER EXPANSION:
NODATA = '65535' 	#assuming null value of 65535
f_isNotNull = lambda d: f_isnot(d, NODATA)         # return ARRAY of bool, TRUE if NOT null 
f_nnVal     = lambda d: f_isNotNull(d) + ' * ' + d  # return ARRAY of not null values
f_nnMask    = lambda d, m: f_isNotNull(m) + ' * ' + d  # return ARRAY of values in data where mask is not null
f_nnSum     = lambda d: f_add( f_nnVal(d) )         # return SUM   of not null values
f_nnCount   = lambda d: f_add( f_isNotNull(d) )     # return COUNT of not null values
f_meanNnVal = lambda d: '(' + f_nnSum(d) + ' / ' + f_nnCount(d) + ')' # null-ignoring mean of the array #number

# compute Standard Deviation on a dataset with null values of 65535
f_devNnVal      = lambda d: f_nnMask(f_nnVal( d ) + ' - ' + f_meanNnVal( d ), d) #array
f_sqDevNnVal    = lambda d: f_sq( f_devNnVal(d) ) #array
f_sumSqDevNnVal = lambda d: f_add( f_sqDevNnVal(d) ) #number
f_varianceNnVal = lambda d: '(' + f_sumSqDevNnVal(d) + ' / ' + f_nnCount(d) + ')' #number
f_stdNnVal      = lambda d: f_sqrt( f_varianceNnVal(d) ) #number

#normalization:
f_normalize = lambda d, sigma: '(255 / ( 2 * ' + str(sigma) + ' * ' + f_stdNnVal(d) + ') * ( ' + d + ' - '  + f_min(d) + '))'

#stretch:
f_stretchMoveBottom=lambda d, n: f_minus(d,f_min( d ))+' * '+n
f_stretchStretchTop=lambda d, n: f_over('255', f_max(f_stretchMoveBottom(d,n)))
f_stretch= lambda d,n: f_times(f_stretchMoveBottom(d,n),f_stretchStretchTop(d,n))

#no data mask
nnMask_3  = lambda a,b,c: '('+a+' * '+b+' * '+c+')' #TRUE IF NOT NULL
nnMaskWL_3  = lambda s,l,c: '('+f_isNotNull(bandName(bandsL(s)))+' * '+f_isNotNull(bandName(bandsL(l)))+' * '+f_isNotNull(bandName(bandsL(c)))+')'
nnMaskWS_3  = lambda s,l,c: '('+f_isNotNull(bandName(bandsS(s)))+' * '+f_isNotNull(bandName(bandsS(l)))+' * '+f_isNotNull(bandName(bandsS(c)))+')'
okMaskWS_3 = lambda s,l,c: '( 1 - ' + nnMaskWS_3(s,l,c) + ')' #TRUE IF NULL

#wave ratio (commonly used by derived products)
f_waveRatio = lambda c,s,l: float(c-s)/float(l-s) #f_waveRatio(c,s,l)

#band depth
f_BandDepthRcL = lambda c,s,l: f_plus(f_times(str(1-f_waveRatio(c,s,l)),bandName(bandsL(s))),f_times(str(f_waveRatio(c,s,l)),bandName(bandsL(l)))) #Rc=(a*Rs+b*Rl)
f_BandDepthRcS = lambda c,s,l: f_plus(f_times(str(1-f_waveRatio(c,s,l)),bandName(bandsS(s))),f_times(str(f_waveRatio(c,s,l)),bandName(bandsS(l)))) #Rc=(a*Rs+b*Rl)
f_BandDepthInvL = lambda c,s,l: f_over(bandName(bandsL(c)),f_BandDepthRcL(c,s,l))
f_BandDepthInvS = lambda c,s,l: f_over(bandName(bandsS(c)),f_BandDepthRcS(c,s,l))
f_BandDepthL = lambda c,s,l: f_minus('1', f_BandDepthInvL(c,s,l))
f_BandDepthS = lambda c,s,l: f_minus('1', f_BandDepthInvS(c,s,l))

#shoulder height
f_waveRatio = lambda c,s,l: float(c-s)/float(l-s)
f_ShoulderHeightRcL = lambda c,s,l: f_plus(f_times(str(1-f_waveRatio(c,s,l)),bandName(bandsL(s))),f_times(str(f_waveRatio(c,s,l)),bandName(bandsL(l)))) #Rc=(a*Rs+b*Rl)
f_ShoulderHeightRcS = lambda c,s,l: f_plus(f_times(str(1-f_waveRatio(c,s,l)),bandName(bandsS(s))),f_times(str(f_waveRatio(c,s,l)),bandName(bandsS(l)))) #Rc=(a*Rs+b*Rl)
f_ShoulderHeightInvL = lambda c,s,l: f_over(f_ShoulderHeightRcL(c,s,l),bandName(bandsL(c)))
f_ShoulderHeightInvS = lambda c,s,l: f_over(f_ShoulderHeightRcS(c,s,l),bandName(bandsS(c)))
f_ShoulderHeightL = lambda c,s,l: f_minus('1', f_ShoulderHeightInvL(c,s,l))
f_ShoulderHeightS = lambda c,s,l: f_minus('1', f_ShoulderHeightInvS(c,s,l))

#min/max stretch
f_toStretch   = lambda d,n: f_plus(f_times(d,n), f_times('( 1 - ' + n + ')',NODATA)) 
f_toEncode    = lambda d,n:  f_stretch(f_toStretch(d,n),n)
f_toEncode1S   = lambda c: f_toEncode( bandName(bandsS(c)), f_isNotNull( bandName(bandsS(c)) ))
f_toEncode1L   = lambda c: f_stretch( bandName(bandsL(c)), f_isNotNull( bandName(bandsL(c)) ))
f_toEncodeBD3S = lambda c,s,l: f_toEncode( f_BandDepthS(c,s,l),      nnMaskWS_3(c,s,l))
f_toEncodeSH3S = lambda c,s,l: f_toEncode( f_ShoulderHeightS(c,s,l), nnMaskWS_3(c,s,l))
f_toEncodeBD3L = lambda c,s,l: f_toEncode( f_BandDepthL(c,s,l),      nnMaskWL_3(c,s,l))
f_toEncodeSH3L = lambda c,s,l: f_toEncode( f_ShoulderHeightL(c,s,l), nnMaskWL_3(c,s,l))
f_toEncodeBD3Sinv = lambda c,s,l: f_toEncode( "1-" + f_BandDepthS(c,s,l),      nnMaskWS_3(c,s,l))
f_toEncodeSH3Sinv = lambda c,s,l: f_toEncode( "1-" + f_ShoulderHeightS(c,s,l), nnMaskWS_3(c,s,l))
f_toEncodeBD3Linv = lambda c,s,l: f_toEncode( "1-" + f_BandDepthL(c,s,l),      nnMaskWL_3(c,s,l))
f_toEncodeSH3Linv = lambda c,s,l: f_toEncode( "1-" + f_ShoulderHeightL(c,s,l), nnMaskWL_3(c,s,l))

#index products, i.e. broad absorption bands
f_R = lambda w: bandName(bandsL(w))
f_Rl = lambda w: bandName(bandsL(w))
f_Rs = lambda w: bandName(bandsS(w))
f_RCx = lambda c,s,l: f_plus( f_times(str(f_waveRatio(c,s,l)),f_minus(f_R(l),f_R(s))),f_R(s) )
f_RBx = lambda c,s,l: f_over(f_minus(f_RCx(c,s,l),f_R(c)), f_RCx(c,s,l)  )
f_indexRAW = lambda waveListTup,s,l: '(' + '+'.join( map(lambda t: f_RBx(t[0],s,l) + '*' + str(t[1]), waveListTup )) + ')'
f_indexAllNNBandsList = lambda d,s,l: [item[0] for s in d] + [s,l]
#f_indexNN = lambda waveListTup,s,l: '(' + ' * '.join( map(lambda t: f_isNotNull(bandName(bandsL(t))), [j[0] for j in waveListTup] + [s,l] )) + ')'
f_indexNN = lambda waveList: '(' + ' * '.join( map(lambda c: f_isNotNull(f_R(c)), waveList )) + ')'
f_indexNNl = lambda waveList: '(' + ' * '.join( map(lambda c: f_isNotNull(f_Rl(c)), waveList )) + ')'
f_indexNNs = lambda waveList: '(' + ' * '.join( map(lambda c: f_isNotNull(f_Rs(c)), waveList )) + ')'
f_toEncodeIndex = lambda waveListTup,s,l: f_toEncode(f_indexRAW(waveListTup,s,l),f_indexNN(waveListTup,s,l))

# R/RC products
f_RRCx = lambda c,s,l: f_over(f_RCx(c,s,l), f_R(c))
f_sumRRCx = lambda cList, s, l: '+'.join(map(lambda c: f_RRCx(c,s,l),cList))

#minimum products
f_compare = lambda less, more: '(' + less + '<' + more + ')*' + less #returns less if less, returns zero if less is more
f_minimum = lambda A,B: f_plus(f_compare(A,B), f_compare(B,A)) #returns lowest of the two

#spectral median for 5 channel kernel
f_isMed5 = lambda a,b,c,d,e: f_times(f_Rs(a),'(2=((0.0+('+f_Rs(a)+'<'+f_Rs(b)+')+('+f_Rs(a)+'<'+f_Rs(c)+')+('+f_Rs(a)+'<'+f_Rs(d)+')+('+f_Rs(a)+'<'+f_Rs(e)+'))))')
f_med5 = lambda a,b,c,d,e: '('+f_isMed5(a,b,c,d,e)+'+'+f_isMed5(b,a,c,d,e)+'+'+f_isMed5(c,a,b,d,e)+'+'+f_isMed5(d,a,b,c,e)+'+'+f_isMed5(e,a,b,c,d)+')'
f_med5s = lambda w: f_med5(w-2*6.458,w-6.458,w,w+6.458,w+2*6.458)
f_med5sNN = lambda w: f_indexNNs([w-2*6.458,w-6.458,w,w+6.458,w+2*6.458])


f_isMed5l = lambda a,b,c,d,e: f_times(f_Rl(a),'(2=((0.0+('+f_Rl(a)+'<'+f_Rl(b)+')+('+f_Rl(a)+'<'+f_Rl(c)+')+('+f_Rl(a)+'<'+f_Rl(d)+')+('+f_Rl(a)+'<'+f_Rl(e)+'))))')
f_med5lprep = lambda a,b,c,d,e: '('+f_isMed5l(a,b,c,d,e)+'+'+f_isMed5l(b,a,c,d,e)+'+'+f_isMed5l(c,a,b,d,e)+'+'+f_isMed5l(d,a,b,c,e)+'+'+f_isMed5l(e,a,b,c,d)+')'
f_med5l = lambda w: f_med5lprep(w-2*6.6,w-6.6,w,w+6.6,w+2*6.6)
f_med5lNN = lambda w: f_indexNNl([w-2*6.6,w-6.6,w,w+6.6,w+2*6.6])

#band depth spectral median with 5 channel kernels
f_BandDepthRcLMed = lambda c,s,l: f_plus(f_times(str(1-f_waveRatio(c,s,l)),f_med5l(s)),f_times(str(f_waveRatio(c,s,l)),f_med5l(l)))
f_BandDepthInvLMed = lambda c,s,l: f_over(f_med5l(c),f_BandDepthRcLMed(c,s,l))
f_BandDepthLMed = lambda c,s,l: f_minus('1', f_BandDepthInvLMed(c,s,l))
f_BandDepthLMedNN = lambda c,s,l: '('+f_med5lNN(c)+'*'+f_med5lNN(s)+'*'+f_med5lNN(l)+')'



###########################\ API ENDS /###################
