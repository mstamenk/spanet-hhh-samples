# This file was automatically created by FeynRules $Revision: 634 $
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Wed 6 Jul 2011 14:07:37



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')



# Loop related parameters

lhv = Parameter(name = 'lhv',
                 nature = 'internal',
                 type = 'real',
                 value = '1.0',
                 texname = '\lambda_{HV}')

Ncol = Parameter(name = 'Ncol',
                 nature = 'internal',
                 type = 'real',
                 value = '3.0',
                 texname = 'N_{col}')

CA = Parameter(name = 'CA',
                 nature = 'internal',
                 type = 'real',
                 value = '3.0',
                 texname = 'C_{A}')

TF = Parameter(name = 'TF',
                 nature = 'internal',
                 type = 'real',
                 value = '0.5',
                 texname = 'T_{F}')

CF = Parameter(name = 'CF',
                 nature = 'internal',
                 type = 'real',
                 value = '(4.0/3.0)',
                 texname = 'C_{F}')

MU_R = Parameter(name = 'MU_R',
              nature = 'external',
              type = 'real',
              value = 91.188,
              texname = '\\text{\\mu_r}',
              lhablock = 'LOOP',
              lhacode = [ 1 ])

# User-defined parameters.

ctheta1 = Parameter(name = 'ctheta1',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = 'ctheta1',
               lhablock = 'BSM',
               lhacode = [ 12 ])

ctheta2 = Parameter(name = 'ctheta2',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = 'ctheta2',
               lhablock = 'BSM',
               lhacode = [ 13 ])

ctheta3 = Parameter(name = 'ctheta3',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = 'ctheta3',
               lhablock = 'BSM',
               lhacode = [ 14 ])

stheta1 = Parameter(name = 'stheta1',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1.-ctheta1**2)',
               texname = 'stheta1')

stheta2 = Parameter(name = 'stheta2',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1.-ctheta2**2)',
               texname = 'stheta2')

stheta3 = Parameter(name = 'stheta3',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1.-ctheta3**2)',
               texname = 'stheta3')

R23 = Parameter(name = 'R23',
                nature = 'internal',
                type = 'real',
                value = '-ctheta2 * stheta3',
                texname = 'R23')

R32 = Parameter(name = 'R32',
                nature = 'internal',
                type = 'real',
                value = 'ctheta1 * stheta3 - stheta1 * stheta2 * ctheta3',
                texname = 'R32')

R22 = Parameter(name = 'R22',
                nature = 'internal',
                type = 'real',
                value = 'ctheta1 * ctheta3 + stheta1 * stheta2 * stheta3',
                texname = 'R22')

R21 = Parameter(name = 'R21',
                nature = 'internal',
                type = 'real',
                value = 'stheta1 * ctheta3 - ctheta1 * stheta2 * stheta3',
                texname = 'R21')

R31 = Parameter(name = 'R31',
                nature = 'internal',
                type = 'real',
                value = 'ctheta1 * stheta2 * ctheta3 + stheta1 * stheta3',
                texname = 'R31')

R11 = Parameter(name = 'R11',
                nature = 'internal',
                type = 'real',
                value = 'ctheta1 * ctheta2',
                texname = 'R11')

R33 = Parameter(name = 'R33',
                nature = 'internal',
                type = 'real',
                value = 'ctheta2 * ctheta3',
                texname = 'R33')

R13 = Parameter(name = 'R13',
                nature = 'internal',
                type = 'real',
                value = '-stheta2',
                texname = 'R13')

R12 = Parameter(name = 'R12',
                nature = 'internal',
                type = 'real',
                value = '-stheta1 * ctheta2',
                texname = 'R12')

RH1 =  Parameter(name = 'RH1',
                nature = 'internal',
                type = 'real',
                value = 'R11',
                texname = 'RH1')

RH2 =  Parameter(name = 'RH2',
                nature = 'internal',
                type = 'real',
                value = 'R21',
                texname = 'RH2')

RH3 =  Parameter(name = 'RH3',
                nature = 'internal',
                type = 'real',
                value = 'R31',
                texname = 'RH3')
                
kap111  = Parameter(name = 'kap111',
                nature = 'external',
                type = 'real',
                value = 2.0,
                lhablock = 'BSM',
                lhacode = [ 15 ],
                texname = '\\text{kap111}')

kap112  = Parameter(name = 'kap112',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 16 ],
                texname = '\\text{kap112}')

kap122  = Parameter(name = 'kap122',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 17 ],
                texname = '\\text{kap122}')

kap222  = Parameter(name = 'kap222',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 18 ],
                texname = '\\text{kap222}')

kap133  = Parameter(name = 'kap133',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 24 ],
                texname = '\\text{kap133}')

kap113  = Parameter(name = 'kap113',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 25 ],
                texname = '\\text{kap113}')

kap123  = Parameter(name = 'kap123',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 26 ],
                texname = '\\text{kap123}')

kap333 = Parameter(name = 'kap333',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 27 ],
                texname = '\\text{kap333}')

kap233 = Parameter(name = 'kap233',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 28 ],
                texname = '\\text{kap233}')


kap223 = Parameter(name = 'kap223',
                nature = 'external',
                type = 'real',
                value = 4.0,
                lhablock = 'BSM',
                lhacode = [ 29 ],
                texname = '\\text{kap223}')


kap1111  = Parameter(name = 'kap1111',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 19 ],
                texname = '\\text{kap1111}')

kap1112  = Parameter(name = 'kap1112',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 20 ],
                texname = '\\text{kap1112}')

kap1122  = Parameter(name = 'kap1122',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 21 ],
                texname = '\\text{kap1122}')

kap1222  = Parameter(name = 'kap1222',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 22 ],
                texname = '\\text{kap1222}')

kap2222  = Parameter(name = 'kap2222',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 23 ],
                texname = '\\text{kap2222}')

kap1113  = Parameter(name = 'kap1113',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 30 ],
                texname = '\\text{kap1113}')

kap1133 = Parameter(name = 'kap1133',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 31 ],
                texname = '\\text{kap1133}')

kap1333  = Parameter(name = 'kap1333',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 32 ],
                texname = '\\text{kap1333}')

kap3333  = Parameter(name = 'kap3333',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 33 ],
                texname = '\\text{kap3333}')

kap2223  = Parameter(name = 'kap2223',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 34 ],
                texname = '\\text{kap2223}')

kap2333  = Parameter(name = 'kap2333',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 35 ],
                texname = '\\text{kap2333}')

kap2233  = Parameter(name = 'kap2233',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 36 ],
                texname = '\\text{kap2233}')

kap1233  = Parameter(name = 'kap1233',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 37 ],
                texname = '\\text{kap1233}')

kap1223  = Parameter(name = 'kap1223',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 38 ],
                texname = '\\text{kap1223}')

kap1123  = Parameter(name = 'kap1123',
                nature = 'external',
                type = 'real',
                value = 3.0,
                lhablock = 'BSM',
                lhacode = [ 39 ],
                texname = '\\text{kap1123}')

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 132.50698,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116639,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

lamWS = Parameter(name = 'lamWS',
                  nature = 'external',
                  type = 'real',
                  value = 0.2253,
                  texname = '\\text{lamWS}',
                  lhablock = 'Wolfenstein',
                  lhacode = [ 1 ])

AWS = Parameter(name = 'AWS',
                nature = 'external',
                type = 'real',
                value = 0.808,
                texname = '\\text{AWS}',
                lhablock = 'Wolfenstein',
                lhacode = [ 2 ])

rhoWS = Parameter(name = 'rhoWS',
                  nature = 'external',
                  type = 'real',
                  value = 0.132,
                  texname = '\\text{rhoWS}',
                  lhablock = 'Wolfenstein',
                  lhacode = [ 3 ])

etaWS = Parameter(name = 'etaWS',
                  nature = 'external',
                  type = 'real',
                  value = 0.341,
                  texname = '\\text{etaWS}',
                  lhablock = 'Wolfenstein',
                  lhacode = [ 4 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.2,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 164.5,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.188,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Meta = Parameter(name = 'Meta',
                 nature = 'external',
                 type = 'real',
                 value = 450,
                 texname = '\\text{Meta}',
                 lhablock = 'MASS',
                 lhacode = [ 99925 ])

Weta = Parameter(name = 'Weta',
                 nature = 'external',
                 type = 'real',
                 value = 5.,
                 texname = '\\text{Weta}',
                 lhablock = 'DECAY',
                 lhacode = [ 99925 ])

Miota = Parameter(name = 'Miota',
                 nature = 'external',
                 type = 'real',
                 value = 950,
                 texname = '\\text{Miota}',
                 lhablock = 'MASS',
                 lhacode = [ 99926 ])

Wiota = Parameter(name = 'Wiota',
                 nature = 'external',
                 type = 'real',
                 value = 10.,
                 texname = '\\text{Wiota}',
                 lhablock = 'DECAY',
                 lhacode = [ 99926 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.44140351,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.04759951,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 6.38233934e-03,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WTau = Parameter(name = 'WTau',
                 nature = 'external',
                 type = 'real',
                 value = 2.27e-12,
                 texname = '\\text{WTau}',
                 lhablock = 'DECAY',
                 lhacode = [ 15 ])



CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = '1 - lamWS**2/2.',
                  texname = '\\text{CKM11}')

CKM12 = Parameter(name = 'CKM12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'lamWS',
                  texname = '\\text{CKM12}')

CKM13 = Parameter(name = 'CKM13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'AWS*lamWS**3*(-(etaWS*complex(0,1)) + rhoWS)',
                  texname = '\\text{CKM13}')

CKM21 = Parameter(name = 'CKM21',
                  nature = 'internal',
                  type = 'complex',
                  value = '-lamWS',
                  texname = '\\text{CKM21}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = '1 - lamWS**2/2.',
                  texname = '\\text{CKM22}')

CKM23 = Parameter(name = 'CKM23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'AWS*lamWS**2',
                  texname = '\\text{CKM23}')

CKM31 = Parameter(name = 'CKM31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'AWS*lamWS**3*(1 - etaWS*complex(0,1) - rhoWS)',
                  texname = '\\text{CKM31}')

CKM32 = Parameter(name = 'CKM32',
                  nature = 'internal',
                  type = 'complex',
                  value = '-(AWS*lamWS**2)',
                  texname = '\\text{CKM32}')

CKM33 = Parameter(name = 'CKM33',
                  nature = 'internal',
                  type = 'complex',
                  value = '1',
                  texname = '\\text{CKM33}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(2*MW*sw)/ee',
              texname = 'v')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu')

# Higgs-photon-photon

AH = Parameter(name = 'AH',
               nature = 'internal',
               type = 'real',
               value = '(47*ee**2*(1 - (2*MH**4)/(987.*MT**4) - (14*MH**2)/(705.*MT**2) + (213*MH**12)/(2.634632e7*MW**12) + (5*MH**10)/(119756.*MW**10) + (41*MH**8)/(180950.*MW**8) + (87*MH**6)/(65800.*MW**6) + (57*MH**4)/(6580.*MW**4) + (33*MH**2)/(470.*MW**2)))/(72.*cmath.pi**2*v)',
               texname = 'A_H')



# To facilitate R2 writings

AxialZUp = Parameter(name = 'AxialZUp',
              nature = 'internal',
              type = 'real',
              value = '(3.0/2.0)*(-(ee*sw)/(6.*cw))-(1.0/2.0)*((cw*ee)/(2.*sw))',
              texname = 'AxialZUp')

AxialZDown = Parameter(name = 'AxialZDown',
              nature = 'internal',
              type = 'real',
              value = '(-1.0/2.0)*(-(cw*ee)/(2.*sw))+(-3.0/2.0)*(-(ee*sw)/(6.*cw))',
              texname = 'AxialZdown')

VectorZUp = Parameter(name = 'VectorZUp',
              nature = 'internal',                      
              type = 'real',
              value = '(1.0/2.0)*((cw*ee)/(2.*sw))+(5.0/2.0)*(-(ee*sw)/(6.*cw))',
              texname = 'AxialZUp')

VectorZDown = Parameter(name = 'VectorZDown',
              nature = 'internal',                        
              type = 'real',
              value = '(1.0/2.0)*(-(cw*ee)/(2.*sw))+(-1.0/2.0)*(-(ee*sw)/(6.*cw))',
              texname = 'AxialZdown')

VectorAUp = Parameter(name = 'VectorAUp',
              nature = 'internal',                      
              type = 'real',
              value = '(2*ee)/3.',
              texname = 'VectorAUp')

VectorADown = Parameter(name = 'VectorADown',
              nature = 'internal',                        
              type = 'real',
              value = '-(ee)/3.',
              texname = 'VectorADown')

VectorWmDxU = Parameter(name = 'VectorWmDxU',
              nature = 'internal',                        
              type = 'real',
              value = '(1.0/2.0)*((ee)/(sw*cmath.sqrt(2)))',
              texname = 'VectorWmDxU')

AxialWmDxU = Parameter(name = 'AxialWmDxU',
              nature = 'internal',                        
              type = 'real',
              value = '(-1.0/2.0)*((ee)/(sw*cmath.sqrt(2)))',
              texname = 'AxialWmDxU')

VectorWpUxD = Parameter(name = 'VectorWpUxD',
              nature = 'internal',                        
              type = 'real',
              value = '(1.0/2.0)*((ee)/(sw*cmath.sqrt(2)))',
              texname = 'VectorWpUxD')

AxialWpUxD = Parameter(name = 'AxialWpUxD',
              nature = 'internal',                        
              type = 'real',
              value = '-(1.0/2.0)*((ee)/(sw*cmath.sqrt(2)))',
              texname = 'AxialWpUxD')



# == Additional parameters for goldstones

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - lamWS**2/2.',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'lamWS',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'AWS*lamWS**3*(-(etaWS*complex(0,1)) + rhoWS)',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-lamWS',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - lamWS**2/2.',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'AWS*lamWS**2',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'AWS*lamWS**3*(1 - etaWS*complex(0,1) - rhoWS)',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(AWS*lamWS**2)',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

I1x31 = Parameter(name = 'I1x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1x31}')

I1x32 = Parameter(name = 'I1x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1x32}')

I1x33 = Parameter(name = 'I1x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1x33}')

I2x12 = Parameter(name = 'I2x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2x12}')

I2x13 = Parameter(name = 'I2x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2x13}')

I2x22 = Parameter(name = 'I2x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2x22}')

I2x23 = Parameter(name = 'I2x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2x23}')

I2x32 = Parameter(name = 'I2x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2x32}')

I2x33 = Parameter(name = 'I2x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2x33}')

I3x21 = Parameter(name = 'I3x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3x21}')

I3x22 = Parameter(name = 'I3x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3x22}')

I3x23 = Parameter(name = 'I3x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3x23}')

I3x31 = Parameter(name = 'I3x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3x31}')

I3x32 = Parameter(name = 'I3x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3x32}')

I3x33 = Parameter(name = 'I3x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3x33}')

I4x13 = Parameter(name = 'I4x13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4x13}')

I4x23 = Parameter(name = 'I4x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4x23}')

I4x33 = Parameter(name = 'I4x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4x33}')

Vector_ubGp = Parameter(name = 'Vector_ubGp',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I1x31',
                  texname = '\\text{Vector_ubGp}')

Vector_cdGp = Parameter(name = 'Vector_cdGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x12',
                  texname = '\\text{Vector_cdGp}')

Vector_csGp = Parameter(name = 'Vector_csGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x22',
                  texname = '\\text{Vector_csGp}')

Vector_cbGp = Parameter(name = 'Vector_cbGp',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I1x32-I2x32',
                  texname = '\\text{Vector_cbGp}')

Vector_tdGp = Parameter(name = 'Vector_tdGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x13',
                  texname = '\\text{Vector_tdGp}')

Vector_tsGp = Parameter(name = 'Vector_tsGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x23',
                  texname = '\\text{Vector_tsGp}')

Vector_tbGp = Parameter(name = 'Vector_tbGp',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I1x33-I2x33',
                  texname = '\\text{Vector_tbGp}')

Axial_ubGp = Parameter(name = 'Axial_ubGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I1x31',
                  texname = '\\text{Axial_ubGp}')

Axial_cdGp = Parameter(name = 'Axial_cdGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x12',
                  texname = '\\text{Axial_cdGp}')

Axial_csGp = Parameter(name = 'Axial_csGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x22',
                  texname = '\\text{Axial_csGp}')

Axial_cbGp = Parameter(name = 'Axial_cbGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x32-I1x32',
                  texname = '\\text{Axial_cbGp}')

Axial_tdGp = Parameter(name = 'Axial_tdGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x13',
                  texname = '\\text{Axial_tdGp}')

Axial_tsGp = Parameter(name = 'Axial_tsGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x23',
                  texname = '\\text{Axial_tsGp}')

Axial_tbGp = Parameter(name = 'Axial_tbGp',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I2x33-I1x33',
                  texname = '\\text{Axial_tbGp}')

Vector_ubGm = Parameter(name = 'Vector_ubGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I4x13',
                  texname = '\\text{Vector_ubGm}')

Vector_cdGm = Parameter(name = 'Vector_cdGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x21',
                  texname = '\\text{Vector_cdGm}')

Vector_csGm = Parameter(name = 'Vector_csGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x22',
                  texname = '\\text{Vector_csGm}')

Vector_cbGm = Parameter(name = 'Vector_cbGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x23-I4x23',
                  texname = '\\text{Vector_cbGm}')

Vector_tdGm = Parameter(name = 'Vector_tdGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x31',
                  texname = '\\text{Vector_tdGm}')

Vector_tsGm = Parameter(name = 'Vector_tsGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x32',
                  texname = '\\text{Vector_tsGm}')

Vector_tbGm = Parameter(name = 'Vector_tbGm',
                  nature = 'internal',
                  type = 'complex',
                  value = 'I3x33-I4x33',
                  texname = '\\text{Vector_tbGm}')

Axial_ubGm = Parameter(name = 'Axial_ubGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I4x13',
                  texname = '\\text{Axial_ubGm}')

Axial_cdGm = Parameter(name = 'Axial_cdGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I3x21',
                  texname = '\\text{Axial_cdGm}')

Axial_csGm = Parameter(name = 'Axial_csGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I3x22',
                  texname = '\\text{Axial_csGm}')

Axial_cbGm = Parameter(name = 'Axial_cbGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I4x23-I3x23',
                  texname = '\\text{Axial_cbGm}')

Axial_tdGm = Parameter(name = 'Axial_tdGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I3x31',
                  texname = '\\text{Axial_tdGm}')

Axial_tsGm = Parameter(name = 'Axial_tsGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I3x32',
                  texname = '\\text{Axial_tsGm}')

Axial_tbGm = Parameter(name = 'Axial_tbGm',
                  nature = 'internal',
                  type = 'complex',
                  value = '-I4x33-I3x33',
                  texname = '\\text{Axial_tbGm}')

