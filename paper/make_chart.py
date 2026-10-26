# Figure 1: sensitivity of P(doom) to f_M and f_U, all other factors at the illustrative "Middle" preset.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.serif":["Source Serif Pro","DejaVu Serif"],"font.size":9,"svg.fonttype":"path","mathtext.fontset":"stix"})
mid=dict(T=.7,C=.8,M=.3,P=.3,U=.4,H=.5,X=.3,A=.1,W=.1,F=.2)
def pdoom(v):
    R=v['M']*v['P']*v['U']*v['H']*v['X']; M=v['A']*v['W']*v['F']; return v['T']*(1-(1-R)*(1-M))+(v['C']-v['T'])*M
fm=np.linspace(0,1,201)
fig,ax=plt.subplots(figsize=(5.6,3.0))
for fu,ls in zip([0.1,0.2,0.4,0.8,1.0],[':','-.','-','--',(0,(5,1))]):
    y=[pdoom({**mid,'M':x,'U':fu})*100 for x in fm]
    ax.plot(fm,y,ls=ls,lw=1.5 if fu==0.4 else 1.1,color='k' if fu==0.4 else '0.35',label=f"$f_U={fu:g}$"+(" (Middle)" if fu==0.4 else ""))
ax.plot([0.3],[pdoom(mid)*100],'o',color='#b03a2e',ms=5,zorder=5,label="Middle preset")
floor=mid['C']*mid['A']*mid['W']*mid['F']*100
ax.axhline(floor,color='#b03a2e',lw=0.8,ls=(0,(2,2)))
ax.text(0.99,floor-0.04,"misuse-only floor $f_C S$ = 0.16%",ha='right',va='top',fontsize=7.5,color='#b03a2e')
ax.set_xlabel("$f_M$ (misalignment)"); ax.set_ylabel("P(doom), %")
ax.set_xlim(0,1); ax.set_ylim(-0.3,3.5); ax.grid(alpha=.25,lw=.5)
ax.legend(fontsize=7.5,frameon=False,loc='upper left',ncol=2)
for s in ['top','right']: ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig("fig1_sensitivity.svg"); fig.savefig("fig1_sensitivity.png",dpi=200)
print(pdoom(mid), pdoom({**mid,'M':1,'U':1}))
