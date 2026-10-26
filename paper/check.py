P={'opt':dict(T=.5,C=.6,M=.1,P=.2,U=.2,H=.3,X=.2,A=.05,W=.05,F=.1),
   'mid':dict(T=.7,C=.8,M=.3,P=.3,U=.4,H=.5,X=.3,A=.1,W=.1,F=.2),
   'pes':dict(T=.9,C=.95,M=.8,P=.6,U=.8,H=.7,X=.6,A=.3,W=.3,F=.4)}
def parts(v):
    R=v['M']*v['P']*v['U']*v['H']*v['X']; S=v['A']*v['W']*v['F']
    d=v['T']*(1-(1-R)*(1-S))+(v['C']-v['T'])*S; return R,S,d
def pd(v): return parts(v)[2]
for n,v in P.items():
    R,S,d=parts(v); T,C=v['T'],v['C']
    er=T*R*(1-S)/d; em=S*(C-T*R)/d; eC=C*S/d
    # numeric elasticity
    h=1e-7; num=lambda k:(pd({**v,k:v[k]*(1+h)})-d)/(d*h)
    print(n,dict(R=R,S=S,Prog=T*R,Pmis=C*S,d=d,odds=1/d,er=er,em=em,eT=er,eC=eC,numM=num('M'),numA=num('A'),numT=num('T'),numC=num('C'),
      noC=T*(1-(1-R)*(1-S)),gap=T*(1-T)*R*S, halfM=pd({**v,'M':v['M']/2}),halfA=pd({**v,'A':v['A']/2}), R0floor=C*S, sumeps=er+em, check=1-T*R*S/d))
m=P['mid'];print('pes T.5', pd({**P['pes'],'T':.5}), 'old',1-(1-.5*parts(P['pes'])[0])*(1-.5*parts(P['pes'])[1]))
# presets
for n,v in {'g25':dict(T=.607,C=.607,M=.607,P=.607,U=.607,H=.607,X=.607,A=0,W=0,F=0),'g18':dict(T=1,C=1,M=.5493,P=.5493,U=.5493,H=.5493,X=.5493,A=0,W=0,F=0),
 'xs':dict(T=.7475,C=.7475,M=.3477,P=.3477,U=.3477,H=.3477,X=.3477,A=0,W=0,F=0),'xe':dict(T=.87,C=.87,M=.5099,P=.5099,U=.5099,H=.5099,X=.5099,A=0,W=0,F=0),
 'cs':dict(T=.52,C=.52,M=.4,P=.65,U=.4,H=1,X=.95,A=0,W=0,F=0)}.items(): print(n,pd(v))
