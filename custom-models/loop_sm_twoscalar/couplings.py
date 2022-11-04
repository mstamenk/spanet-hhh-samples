# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (November 11, 2008)
# Date: Fri 18 Mar 2011 18:40:51


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec

GC_HAA = Coupling(name = 'GC_HAA',
                value = '-(AH*RH1*complex(0,1))',
                order = {'QED':3})

GC_30 = Coupling(name = 'GC_30',
                    value = '-6*complex(0,1)*kap111',
                 order = {'QED':1})

GC_930 = Coupling(name = 'GC_930',
                 value = '-6*complex(0,1)*kap222',
                 order = {'QED':1})

GC_HHeta0 = Coupling(name = 'GC_HHeta0',
                 value = '-2*complex(0,1)*kap112',
                 order = {'QED':1})

GC_Heta0eta0 = Coupling(name = 'GC_Heta0eta0',
                value = '-2*complex(0,1)*kap122',
                 order = {'QED':1})

GC_HHHH = Coupling(name = 'GC_HHHH',
                 value = '-24*complex(0,1)*kap1111',
                order = {'QED':2})

GC_eta0eta0eta0eta0 = Coupling(name = 'GC_eta0eta0eta0eta0',
                 value = '-24*complex(0,1)*kap2222',
                order = {'QED':2})

GC_HHeta0eta0 = Coupling(name = 'GC_HHeta0eta0',
                 value = '-4*complex(0,1)*kap1122',
                order = {'QED':2})

GC_HHHeta0 = Coupling(name = 'GC_HHHeta0',
                 value = '-6*complex(0,1)*kap1112',
                order = {'QED':2})

GC_Heta0eta0eta0 = Coupling(name = 'GC_Heta0eta0eta0',
                 value = '-6*complex(0,1)*kap1222',
                order = {'QED':2})

GC_iota0iota0iota0iota0 = Coupling(name = 'GC_iota0iota0iota0iota0', #3333
                                    value = '-24*complex(0,1)*kap3333',
                                    order = {'QED':2})

GC_Hiota0iota0iota0 = Coupling(name = 'GC_Hiota0iota0iota0', #1333
                                   value = '-6*complex(0,1)*kap1333',
                                   order = {'QED':2})
                                   
GC_HHiota0iota0 = Coupling(name = 'GC_HHiota0iota0', # 1133
                               value = '-4*complex(0,1)*kap1133',
                               order = {'QED':2})

GC_HHHiota0 = Coupling(name = 'GC_HHHiota0', #1113
                           value = '-6*complex(0,1)*kap1113',
                           order = {'QED':2})
                           
GC_eta0iota0iota0iota0 = Coupling(name = 'GC_eta0iota0iota0iota0', #2333
                        value = '-6*complex(0,1)*kap2333',
                        order = {'QED':2})
                                      
GC_eta0eta0iota0iota0 = Coupling(name = 'GC_eta0eta0iota0iota0', #2233
                            value = '-4*complex(0,1)*kap2233',
                            order = {'QED':2})
                                     
GC_iota0eta0eta0eta0 = Coupling(name = 'GC_iota0eta0eta0eta0', #2223
                            value = '-6*complex(0,1)*kap2223',
                            order = {'QED':2})
                                    
GC_Heta0iota0iota0 = Coupling(name = 'GC_Heta0iota0iota0', #1233
                            value = '-2*complex(0,1)*kap1233',
                            order = {'QED':2})
                                  
GC_HHeta0iota0 = Coupling(name = 'GC_HHeta0iota0', #1123
                            value = '-2*complex(0,1)*kap1123',
                            order = {'QED':2})

GC_Heta0eta0iota0 = Coupling(name = 'GC_Heta0eta0iota0', #1223
                            value = '-2*complex(0,1)*kap1223',
                            order = {'QED':2})

GC_HHiota0 = Coupling(name = 'GC_HHiota0', #113
                            value = '-2*complex(0,1)*kap113',
                            order = {'QED':2})

GC_Hiota0iota0 = Coupling(name = 'GC_Hiota0iota0', #133
                            value = '-2*complex(0,1)*kap133',
                            order = {'QED':2})
                              
GC_Hiota0eta0 = Coupling(name = 'GC_Hiota0eta0', #123
                             value = '-1*complex(0,1)*kap123',
                             order = {'QED':2})

GC_iota0iota0iota0 = Coupling(name = 'GC_iota0iota0iota0', #333
                            value = '-6*complex(0,1)*kap333',
                            order = {'QED':2})
                                  
GC_eta0iota0iota0 = Coupling(name = 'GC_eta0iota0iota0', #233
                            value = '-2*complex(0,1)*kap233',
                            order = {'QED':2})
                                 
GC_eta0eta0iota0 = Coupling(name = 'GC_eta0eta0iota0', #223
                            value = '-2*complex(0,1)*kap223',
                            order = {'QED':2})                                
                                

GC_1 = Coupling(name = 'GC_1',
                 value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-G',
                order = {'QCD':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_7 = Coupling(name = 'GC_7',
                value = 'cw*complex(0,1)*gw',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)*gw**2)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'cw**2*complex(0,1)*gw**2',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(ee**2*complex(0,1))*RH1**2/(2.*sw**2)',
                 order = {'QED':2})

GC_910 = Coupling(name = 'GC_910',
                 value = '(ee**2*complex(0,1))*RH2**2/(2.*sw**2)',
                 order = {'QED':2})

GC_710 = Coupling(name = 'GC_710',
                 value = '(ee**2*complex(0,1))*RH3**2/(2.*sw**2)',
                 order = {'QED':2})

GC_410 = Coupling(name = 'GC_410',
                 value = '(ee**2*complex(0,1))*RH1*RH2/(2.*sw**2)',
                 order = {'QED':2})

GC_510 = Coupling(name = 'GC_510',
                 value = '(ee**2*complex(0,1))*RH1*RH3/(2.*sw**2)',
                 order = {'QED':2})

GC_610 = Coupling(name = 'GC_610',
                 value = '(ee**2*complex(0,1))*RH2*RH3/(2.*sw**2)',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CKM11*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(CKM12*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(CKM13*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CKM21*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(CKM22*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(CKM23*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(CKM31*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(CKM32*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(CKM33*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)*gw*sw',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-2*cw*complex(0,1)*gw**2*sw',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = 'complex(0,1)*gw**2*sw**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cw*ee*complex(0, 1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH1**2',
                 order = {'QED':2})

GC_929 = Coupling(name = 'GC_929',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH2**2',
                 order = {'QED':2})

GC_729 = Coupling(name = 'GC_729',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH3**2',
                 order = {'QED':2})

GC_429 = Coupling(name = 'GC_429',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH1*RH2',
                 order = {'QED':2})

GC_529 = Coupling(name = 'GC_529',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH1*RH3',
                 order = {'QED':2})

GC_629 = Coupling(name = 'GC_629',
                 value = '(ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2))*RH2*RH3',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee**2*complex(0,1)*v)*RH1/(2.*sw**2)',
                 order = {'QED':1})

GC_931 = Coupling(name = 'GC_931',
                 value = '(ee**2*complex(0,1)*v)*RH2/(2.*sw**2)',
                 order = {'QED':1})

GC_731 = Coupling(name = 'GC_731',
                 value = '(ee**2*complex(0,1)*v)*RH3/(2.*sw**2)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2))*RH1',
                 order = {'QED':1})

GC_932 = Coupling(name = 'GC_932',
                 value = '(ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2))*RH2',
                 order = {'QED':1})

GC_732 = Coupling(name = 'GC_732',
                 value = '(ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2))*RH3',
                 order = {'QED':1})


GC_33 = Coupling(name = 'GC_33',
                 value = '-((complex(0,1)*yb)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_933 = Coupling(name = 'GC_933',
                 value = '-((complex(0,1)*yb)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_733 = Coupling(name = 'GC_733',
                 value = '-((complex(0,1)*yb)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((complex(0,1)*yc)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_934 = Coupling(name = 'GC_934',
                 value = '-((complex(0,1)*yc)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_734 = Coupling(name = 'GC_734',
                 value = '-((complex(0,1)*yc)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((complex(0,1)*ye)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_935 = Coupling(name = 'GC_935',
                 value = '-((complex(0,1)*ye)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_735 = Coupling(name = 'GC_735',
                 value = '-((complex(0,1)*ye)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((complex(0,1)*ym)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_936 = Coupling(name = 'GC_936',
                 value = '-((complex(0,1)*ym)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_736 = Coupling(name = 'GC_736',
                 value = '-((complex(0,1)*ym)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-((complex(0,1)*yt)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_937 = Coupling(name = 'GC_937',
                 value = '-((complex(0,1)*yt)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_737 = Coupling(name = 'GC_737',
                 value = '-((complex(0,1)*yt)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((complex(0,1)*ytau)*RH1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_938 = Coupling(name = 'GC_938',
                 value = '-((complex(0,1)*ytau)*RH2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_738 = Coupling(name = 'GC_738',
                 value = '-((complex(0,1)*ytau)*RH3/cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(ee*complex(0,1)*complexconjugate(CKM11))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee*complex(0,1)*complexconjugate(CKM12))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1)*complexconjugate(CKM13))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(ee*complex(0,1)*complexconjugate(CKM21))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee*complex(0,1)*complexconjugate(CKM22))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*complexconjugate(CKM23))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1)*complexconjugate(CKM31))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*complexconjugate(CKM32))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ee*complex(0,1)*complexconjugate(CKM33))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})


# == Additional coupling for the goldstones for Feynman gauge

GC_1033 = Coupling(name = 'GC_1033',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_1031 = Coupling(name = 'GC_1031',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_1032 = Coupling(name = 'GC_1032',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_1068 = Coupling(name = 'GC_1068',
                 value = '-2*complex(0,1)*lam*v',
                 order = {'QED':1})

GC_1006 = Coupling(name = 'GC_1006',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_1003 = Coupling(name = 'GC_1003',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                 value = '-(ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_1054 = Coupling(name = 'GC_1054',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_1074 = Coupling(name = 'GC_1074',
                 value = '-(ee**2*v)/(2.*sw)',
                 order = {'QED':1})

GC_1039 = Coupling(name = 'GC_1039',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                 value = '-ee/(2.*sw)',
                 order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_1075 = Coupling(name = 'GC_1075',
                 value = '(ee**2*v)/(2.*sw)',
                 order = {'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                 value = '-(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_1063 = Coupling(name = 'GC_1063',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_1060 = Coupling(name = 'GC_1060',
                 value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_1061 = Coupling(name = 'GC_1061',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_1008 = Coupling(name = 'GC_1008',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_1009 = Coupling(name = 'GC_1009',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_1067 = Coupling(name = 'GC_1067',
                 value = '(ee**2*v)/(2.*cw)',
                 order = {'QED':1})

GC_1007 = Coupling(name = 'GC_1007',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_1066 = Coupling(name = 'GC_1066',
                 value = '-(ee**2*v)/(2.*cw)',
                 order = {'QED':1})

GC_1065 = Coupling(name = 'GC_1065',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_1064 = Coupling(name = 'GC_1064',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_1082 = Coupling(name = 'GC_1082',
                 value = '-(yb/cmath.sqrt(2))',
                 order = {'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                 value = '-I2x12',
                 order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                 value = '-I2x13',
                 order = {'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                 value = '-I2x22',
                 order = {'QED':1})

GC_1019 = Coupling(name = 'GC_1019',
                 value = '-I2x23',
                 order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                 value = 'I1x31',
                 order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                 value = 'I1x32',
                 order = {'QED':1})

GC_1020 = Coupling(name = 'GC_1020',
                 value = '-I2x32',
                 order = {'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                 value = 'I1x33',
                 order = {'QED':1})

GC_1021 = Coupling(name = 'GC_1021',
                 value = '-I2x33',
                 order = {'QED':1})

GC_1088 = Coupling(name = 'GC_1088',
                 value = '-(ye/cmath.sqrt(2))',
                 order = {'QED':1})

GC_1092 = Coupling(name = 'GC_1092',
                 value = '-(ym/cmath.sqrt(2))',
                 order = {'QED':1})

GC_1098 = Coupling(name = 'GC_1098',
                 value = '-(ytau/cmath.sqrt(2))',
                 order = {'QED':1})

GC_1087 = Coupling(name = 'GC_1087',
                 value = 'ye',
                 order = {'QED':1})

GC_1091 = Coupling(name = 'GC_1091',
                 value = 'ym',
                 order = {'QED':1})

GC_1097 = Coupling(name = 'GC_1097',
                 value = 'ytau',
                 order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                 value = '-I4x13',
                 order = {'QED':1})

GC_1022 = Coupling(name = 'GC_1022',
                 value = 'I3x21',
                 order = {'QED':1})

GC_1023 = Coupling(name = 'GC_1023',
                 value = 'I3x22',
                 order = {'QED':1})

GC_1024 = Coupling(name = 'GC_1024',
                 value = 'I3x23',
                 order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                 value = 'I3x31',
                 order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                 value = '-I4x23',
                 order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                 value = 'I3x32',
                 order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                 value = 'I3x33',
                 order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                 value = '-I4x33',
                 order = {'QED':1})

GC_1085 = Coupling(name = 'GC_1085',
                 value = 'yc/cmath.sqrt(2)',
                 order = {'QED':1})

GC_1095 = Coupling(name = 'GC_1095',
                 value = 'yt/cmath.sqrt(2)',
                 order = {'QED':1})

GC_1086 = Coupling(name = 'GC_1086',
                 value = '-ye',
                 order = {'QED':1})

GC_1090 = Coupling(name = 'GC_1090',
                 value = '-ym',
                 order = {'QED':1})

GC_1096 = Coupling(name = 'GC_1096',
                 value = '-ytau',
                 order = {'QED':1})








