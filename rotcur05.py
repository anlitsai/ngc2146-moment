#!/usr/bin/env python
# NGC 2146

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
pc2cm=3.26*3e10*365*86400
kpc2cm=pc2cm*1.0e3
ev2erg=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
c=3.0e10 # light speed
M_sun=1.99e33 # solar mass
L_sun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
N_A=6.02e23
Msun_pc2=M_sun/pc2cm**2
#  --- parameter ------------------------------	#
M_n2146_Msun=8.67e10	# Taramopoulos 2001
v_n2146_kms=250.0	# Taramopoulos 2001
r_n2146_kpc=15.0	# Taramopoulos 2001
a1=0.3		# Tsai 2009
b1=0.32		# Tsai 2009
c1=256.39		# Tsai 2009
n2146="NGC 2146"
r1=0.8
r2=1
r3=1.2
r4=1.5
r5=2
r6=3
r7=5
r8=10
r9=15
v_rms=11.2
r0_kpc=0.8
dyn2dsk=2
#dyn2dsk=1.75
# --------------------------------------------	#
print "------------"
# --- rotation curve --------------------------	#
def v_rot_n2146(r_kpc):
	r=r_kpc
	v_kms=r*c1/(r**a1+r**(1-b1))/dyn2dsk
	print n2146,"rotation speed =",'%.2f' %(v_kms),"[km/s] (z <",r_kpc,"kpc)"
	return v_kms
v1=v_rot_n2146(r1)
v2=v_rot_n2146(r2)
v3=v_rot_n2146(r3)
v4=v_rot_n2146(r4)
v5=v_rot_n2146(r5)
v6=v_rot_n2146(r6)
v7=v_rot_n2146(r7)
v8=v_rot_n2146(r8)
v9=v_rot_n2146(r9)
# --- dynamical mass --------------------------	#
def m_dyn(v_kms,r_kpc,name):
	r=r_kpc*kpc2cm
	v=v_kms*1.0e5
	m=r*v**2/G	# Orange book p.958
	m_Msun=m/M_sun
	print name, "dynamical mass =", '%.2e' %(m_Msun), "[M_sun] @",r_kpc,"[kpc]"
	return m_Msun
m1=m_dyn(v1,r1,"n2146 (NMA CO)")
m2=m_dyn(v2,r2,"n2146 (NMA CO)")
m3=m_dyn(v3,r3,"n2146 (NMA CO)")
m4=m_dyn(v4,r4,"n2146 (NMA CO)")
m5=m_dyn(v5,r5,"n2146 (NMA CO)")
m6=m_dyn(v6,r6,"n2146 (NMA CO)")
m7=m_dyn(v7,r7,"n2146 (NMA CO)")
m8=m_dyn(v8,r8,"n2146 (NMA CO)")
m9=m_dyn(v9,r9,"n2146 (NMA CO)")
m10=m_dyn(v_n2146_kms,r_n2146_kpc,"n2146 (Taramopoulos 2001)")
m11=m_dyn(220.0,2.0,"n3628 (NMA CO)")
m11=m_dyn(200.0,1.45,"n3628 (NMA CO)")

# --- dynamical density -----------------------	#
# rho=v^2/(4*pi*g*r^2)	# Orange book p.959
def rho_dyn(v_kms,r_kpc):
	v=v_kms*1.0e5
	r0=r0_kpc*kpc2cm
	if r_kpc > r0_kpc:
		r=r_kpc*kpc2cm
	else:
		r=0
	c0=v**2/(4*math.pi*G)
	c0_Msunkpc=c0/(M_sun/kpc2cm)
	rho=c0/(r0**2+r**2)
	rho_Msunpc3=rho/(M_sun/pc2cm**3)
	print '%.2e' %(rho_Msunpc3),"[Msun/pc^3]"
	print '%.2e' %(c0_Msunkpc),"[Msun/kpc]"
	return rho_Msunpc3
rho1=rho_dyn(v1,r1)
rho2=rho_dyn(v2,r2)
rho3=rho_dyn(v3,r3)
# --- escape velocity -------------------------	#
def v_esc(M_Msun,r_kpc,name):
	M=M_Msun*M_sun
	r=r_kpc*kpc2cm
	v=math.sqrt(2*G*M/r)/1.0e5
	print name,"escape velocity =",'%.2f' %(v),"[km/s]"
	return v
v=v_esc(M_n2146_Msun,2,n2146)
v=v_esc(M_n2146_Msun,1, n2146)
v=v_esc(m1,15, n2146)
# --- surface mass density --------------------	#
# v^2/R=GM/R^2
# surface mass density=M/R^2=v^2/RG
#def surf_den_dyn(v_kms,r_kpc,m_Msun,name):
def surf_den_dyn(m_Msun,r_kpc,name):
#	v=v_kms*1.0e5
	r=r_kpc*kpc2cm
	m_dyn=m_Msun*M_sun
	sd_dyn=m_dyn/(math.pi*r**2)
#	sd_dyn=v**2/(r*G)
	sd_dyn_Msunpc2=sd_dyn/Msun_pc2
	print name,"ttl.surf.mass den.=",'%.2f' %(sd_dyn_Msunpc2),"[M_sun/pc^2] (z <",r_kpc,"kpc)"
	return sd_dyn
sd1=surf_den_dyn(m1,r1,n2146)
sd2=surf_den_dyn(m2,r2,n2146)
sd3=surf_den_dyn(m3,r3,n2146)
sd4=surf_den_dyn(m4,r4,n2146)
sd5=surf_den_dyn(m5,r5,n2146)
sd6=surf_den_dyn(m6,r6,n2146)
sd7=surf_den_dyn(m7,r7,n2146)
sd8=surf_den_dyn(m8,r8,n2146)
sd9=surf_den_dyn(m9,r9,n2146)
# ---------------------------------------------	#


exit

# --- reference -------------------------------	#
# Taramopoulos et al 2001, AA, 365, 360
# Carroll & Ostlie 1996, Modern Astrophysics (Orange book)

