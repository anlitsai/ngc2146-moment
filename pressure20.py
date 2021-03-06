#!/usr/bin/env python
# NGC 2146

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400
kpc=pc*1.0e3
ev=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
rad2as=180.0/math.pi*3600
#E_ion_ev=13.6	# [eV]
#E_bnd_ev=4.52	# [eV]
#  --- parameter -------------------------------	#
print "============"
print "NGC 2146"
print "============"
print "parameters"
print "------------"
i_deg=70.0
i_pi=i_deg/180.0*math.pi
sin_i=math.sin(i_pi)
cos_i=math.cos(i_pi)
D_Mpc=17.2
X_CO2H2=1.4/3.0
H22mol=1.36
XH=X_CO2H2*H22mol
print "inclination",i_pi,sin_i,cos_i
v_motf_kms=200.0 # km/s (Tsai et al. 2009)
v_sound_kms=1.0e3
T_mol=30.0 # K (Tsai et al. 2009)
T_xotf=1.0e6 # K
EI=8.0e62 # cm^-3 (Inui et al. 2005)
R_xotf_pc=6.3*1000*4.8/3.5 # (Inui et al. 2005)
R_xotf=R_xotf_pc*pc
V_xotf=(4.0/3.0*math.pi)*R_xotf**3 # (Inui et al. 2005)
V_xotf_Inui=(4.0/3.0*math.pi)*(6.3e3*pc)**3 # (Inui et al. 2005)
fill=0.01 # (Inui et al. 2005)
print "filling factor =", fill
n_mol=100.0 # cm^-3 (Tsai et al. 2009)
rho_mol=n_mol/N_A
n_xotf=(EI/V_xotf/fill)**(0.5) # cm^-3 (Iuni et al. 2005)
print "n_xotf =", n_xotf, "[cm^-3]"
print "n_xotf (Inui) =", 5.1e-3*fill**(-0.5), "[cm^-3]"
print "n_mol =", n_mol, "[cm^-3]"
print "rho_mol", '%.2e' %(rho_mol), "[g cm^-3]"
kT_xotf_ev=0.5e3
kT_xotf=kT_xotf_ev*ev
print "kT [ev] of xray outflow =", kT_xotf_ev,"ev"
print "kT [erg] of xray outflow =", kT_xotf,"erg"
print "V_xotf =", V_xotf
print "V_xotf (Inui) =", V_xotf_Inui
M_xotf=n_xotf*m_p*V_xotf*fill
M_xotf_Msun=M_xotf/Msun
M_xotf_Msun_Inui=1.3e8*fill**0.5
M_xotf_Inui=M_xotf_Msun_Inui*Msun
M_galdsk_Msun=8.67e10
M_galdsk_Msun=2.18e11
M_galdsk=M_galdsk_Msun*Msun
L_xotf=1.3e40 # (Inui et al. 2005)
E_xotf=1.0e56 # (Inui et al. 2005)
print "L_xotf =", L_xotf, "[erg/s]"
print "E_xotf =", E_xotf, "[erg]"
effi_x_thrm=0.3	# (Strickland & Stevens 2000)
effi_x_mech=0.01	# (Strickland & Stevens 2000)
R_motf=2.0e3*pc # (Tsai et al. 2009)
SFR=10.0 # Msun/yr (Greve et al. 2000)
SNrate= 0.15 # yr^-1 (Tarchi et al. 2000)
print "SN rate =", SNrate, "[yr^-1]"
effi_mass2rad=0.001 # (Thompson et al. 2005)
as2pc=80.0
px2as=0.2
bm2as2=3.3*2.8
bm2px=bm2as2/(px2as**2)
print bm2as2,bm2px
R_starburst_pc=700.0 # (@tau=1# Thompson et al. 2005)
# R_starburst_pc=1000.0 # (our data)
R_starburst_pc_greve=1250.0 # (Greve 2000)
R_conti_pc=2560.0/2 # (our data) (/iapetus/data/satoki_data/ngc2146/20100130.conti89GHz )
#V_starburst_pc3_greve=2.0e10 # (Greve 2000)
#z_starburst_pc=40.0	# (our calculation) (iapetus:/iapetus/thesis/phd/calculation/veldisp13.sh)
z_starburst_pc_greve=500.0	# (Greve 2000)
tau=10.0
d_mpc=17.2	# Mpc
alpha=1.0	# (Chevalier 1985)
beta=1.0	# (Chevalier 1985)
a1=0.3          # Tsai 2009
b1=0.32         # Tsai 2009
c1=256.39               # Tsai 2009
timescale=1.0e7	# [yr] ; ourdata
v_rms_kms=11.16
v_rms=v_rms_kms*1.0e5

def surf_den_dyn(r_kpc):
	v_kms=r_kpc*c1/(r_kpc**a1+r_kpc**(1-b1))/sin_i
	v=v_kms*1.0e5
	r=r_kpc*kpc
	r_pc=r_kpc*1000
	m_dyn=r*v**2/G      # Orange book p.958
	m_dyn_Msun=m_dyn/Msun
	sd_dyn=m_dyn/(math.pi*r**2)
	sd_dyn_Msunpc2=m_dyn_Msun/(math.pi*r_pc**2)
#	sd_dyn_Msunpc2=sd_dyn/Msun_pc2
	z_pc=(v_rms**2/(2*math.pi*G*sd_dyn))/pc
	print '%.2f' %(sd_dyn_Msunpc2),"[Msun/pc2] (r <",r_kpc,"kpc ; z =",'%.2f' %(z_pc),"pc)",'%.2f' %v_kms,"[km/s]", '%.2e' %(m_dyn_Msun),"[Msun]"
	return sd_dyn_Msunpc2,z_pc
sd05=surf_den_dyn(0.3)
sd05=surf_den_dyn(0.5)
sd08=surf_den_dyn(0.8)
sd10=surf_den_dyn(1.0)
sd12=surf_den_dyn(1.2)
sd15=surf_den_dyn(1.5)
sd24=surf_den_dyn(2.4)
sd28=surf_den_dyn(2.8)
sd30=surf_den_dyn(3.0)
sd32=surf_den_dyn(3.2)
sd_dyn=sd32[0]
z_starburst_pc=sd32[1]
#sd35=surf_den_dyn(3.5)
#sd50=surf_den_dyn(5)
#sd100=surf_den_dyn(10)
def surf_den_rv(r_kpc,v_kms,name):
	r=r_kpc*kpc
	r_pc=r_kpc*1000
	v=v_kms*1.0e5
	m=r*v**2/G
	m_Msun=m/Msun
	sd=m_Msun/(math.pi*r_pc**2)
	print '%.2f' %(sd),"[Msun/pc2] (r <",r_kpc,"kpc)",'%.2f' %v_kms,"[km/s]", '%.2e' %(m_Msun),"[Msun]",name
	return sd
sd=surf_den_rv(1,100,"?")
sd=surf_den_rv(1,136,"?")
sd=surf_den_rv(2,100,"?")
sd=surf_den_rv(2,50,"?")
sd=surf_den_rv(3,200,"?")
sd=surf_den_rv(4,200,"?")
sd=surf_den_rv(5,100,"M31")
sd=surf_den_rv(1,50,"M31")
sd=surf_den_rv(1,50,"M33")
# http://w3.iihe.ac.be/icecube/3_Activities/1_WIMPs%20Analysis/
sd=surf_den_rv(2,50,"?")
sd=surf_den_rv(10,150,"N3198")
sd=surf_den_rv(5,150,"N3198")
sd=surf_den_rv(2,100,"N3198")
sd=surf_den_rv(15,300,"N4378")
# http://bustard.phys.nd.edu/Phys171/lectures/dm.html
sd=surf_den_rv(4,120,"N6503")
# http://www.nicolascretton.ch/Astronomy/index_The_subject.html
# --- gravitational pressure (Gunn & Gott 1972) -------	#

#def surf_den_skmt99(S_CO_JyBmMSpx,px,i_deg,D_Mpc):
def surf_den_skmt99_old(S_CO_JyBmMS,px,type):
	n_bm=px/bm2px
	n_as=px*px2as**2
	S_CO=S_CO_JyBmMS/1000*n_bm
	I_CO=S_CO/n_as
	sd_Msunpc2=(5.0e2*cos_i*I_CO)*XH
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
	print '%.2f' %I_CO,"[Jy km/s as-2]", '%.2f' %sd_Msunpc2,"[Msun/pc2]",'%.2e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas
sd=surf_den_skmt99_old(4.1472E+02,11022,"motf")
sd=surf_den_skmt99_old(1.429E+03,84370,"motf")
sd=surf_den_skmt99_old(7.481E+02,46830,"motf")
sd=surf_den_skmt99_old(1.327E+03,69990,"motf")
sd=surf_den_skmt99_old(6.669E+02,57300,"motf")
sd_motf_Msunpc2=sd[0]
M_motf=sd[1]
sd=surf_den_skmt99_old(1.1243E+04,38685,"unkown")
sd=surf_den_skmt99_old(1.3559E+04,30802,"45as")
sd=surf_den_skmt99_old(1.3182E+04,31100,"mdsk")
sd=surf_den_skmt99_old(3.730E+03,53030,"mbbl")

def surf_den_skmt99_new(S_CO_JyBmMS,blc1,blc2,trc1,trc2,type):
	n_px=(blc1-trc1)*(blc2-trc2)
	n_bm=n_px/bm2px
	n_as=n_px*px2as**2
	S_CO=S_CO_JyBmMS/1000*n_bm
	I_CO=S_CO/n_as
	sd_Msunpc2=(5.0e2*cos_i*I_CO)*XH
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
	print '%.2f' %I_CO,"[Jy km/s as-2]", '%.2f' %sd_Msunpc2,"[Msun/pc2]",'%.2e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas

#sd=surf_den_skmt99_new(2.054E+04,,"mdsk")
#sd=surf_den_skmt99_new(2.111E+04,,"mdsk")
#sd=surf_den_skmt99_new(4.769E+04,,"0.3kpc")
#sd=surf_den_skmt99_new(3.523E+04,,"0.5kpc")
sd=surf_den_skmt99_new(3.356E+04,455,482,559,542,"0.8kpc")
sd=surf_den_skmt99_new(3.652E+04,457,484,557,537,"0.8kpc")
sd=surf_den_skmt99_new(3.049E+04,430,484,583,544,"1.2kpc")
sd=surf_den_skmt99_new(2.431E+04,430,468,582,551,"1.2kpc")
sd=surf_den_skmt99_new(2.139E+04,407,466,609,547,"1.6kpc")
sd=surf_den_skmt99_new(1.723E+04,407,457,609,566,"1.6kpc")
sd=surf_den_skmt99_new(1.579E+04,357,461,659,550,"2.4kpc")
sd=surf_den_skmt99_new(1.381E+04,384,447,663,570,"2.4kpc")
sd=surf_den_skmt99_new(1.466E+04,357,458,659,558,"2.4kpc")
sd=surf_den_skmt99_new(1.364E+04,334,458,684,558,"2.8kpc")



sd=surf_den_skmt99_old(4.1472E+02,11022,"motf")
sd_motf=sd_motf_Msunpc2*Msun_pc2
sd_xotf=sd_motf*(n_xotf/n_mol)*(M_xotf/M_motf)
sd_xotf_Msunpc2=sd_xotf*Msun_pc2


def mass(S_Jy_ms,lamb_cm,px,D_Mpc,region):
	bm_as=px*px2as**2
	T=13.6*(lamb_cm*10)**2*bm_as*S_Jy_ms/1000
	colden=T*1.4e20
	sd=colden*m_p/Msun_pc2
	D=D_Mpc*1.0e6*pc
	A_cm2=bm_as*(D/rad2as)**2
	A_pc2=A_cm2/pc**2
	m=sd*A_pc2
	print '%.2e' %sf,"[Msun/pc2]", '%.2e' %m,"[Msun]",region
	return sd
mass(2.431E+04,0.26,128520,17.2,"1.2kpc")
mass(1.364E+04,0.26,306950,17.2,"1.2kpc")


print "------------"
print "calculation results"
print "------------"
print "+[ grav P = 2*pi*G*(surf_den_xry)*(surf_den_dynamical_mass) ]+"
def p_grav(sd,type):
	gravP=2*math.pi*G*sd*sd_dyn*Msun_pc2
	print " o", type, "grav P:", '%.2e' %(gravP)
	return gravP

p_grav_motf=p_grav(sd_motf,"mol. outflow")
p_grav_xotf=p_grav(sd_xotf, "xray outflow")
# unit checked

# --- ram pressure (Gunn & Gott 1972) -----------------	#
print "------------"
print "+[ ram P = rho*(relative velocity)^2 ]+"
def v_esc(M_Msun,R_kpc):
	v=math.sqrt(2*G*M_Msun*Msun/(R_kpc*1.0e3*pc))/1.0e5
	print "escape velocity",v,"[km/s]"
	return v
v_2kpc=v_esc(8.67e10,2)
v_1kpc=v_esc(8.67e10,1)
#E_bnd_ion_particle=(E_bnd_ev+E_ion_ev)*ev
#E_bnd_ion_mass=E_bnd_ion_particle*N_A*M_xotf_g
def ramP(effi_x1,effi_x2,type1,type2):
	print "   ", type1, effi_x1
	print "   ", type2, effi_x2
	effi_x=effi_x1*effi_x2
	E_ttl=E_xotf/effi_x
	print "    total Energy =",'%.2f' %(E_ttl), "[erg]"
	E_mech=E_ttl*(1-effi_x)
	v_xry_kms=math.sqrt(E_mech*2/M_xotf)/1.0e5
	print "    v_xry = ",  '%.2f' %(v_xry_kms), "[km/s]"
	v_rel_kms=v_xry_kms-v_motf_kms
	v_rel=v_rel_kms*1.0e5
	p=rho_mol*v_rel**2
	p_K=p/k_B
	print "    v_rel = ",  '%.2f' %(v_rel_kms), "[km/s]"
	print " o ram P: ", '%.2e' %(p),"[dyne cm^-2]"
	print " o ram P: ", '%.2e' %(p_K), "[K cm^-3]"
	return p
# unit checked
type2="Lx increasing factor"
print "the total energy released by SNe and stellar winds (doesn't include the K.E)"
p_ram1=ramP(0.1,1,"thermalization efficiency (lower)",type2)
p_ram1=ramP(0.3,1,"thermalization efficiency",type2)
p_ram1=ramP(0.5,1,"thermalization efficiency",type2)
p_ram1=ramP(1,1,"thermalization efficiency (upper)",type2)
print "radiating the mechanical energy supplied by the starburst"
p_ram1=ramP(0.01,10,"starburst energy injection rate (thin-disk)",type2)
p_ram1=ramP(0.05,3,"starburst energy injection rate (thick-disk, lower)",type2)
p_ram1=ramP(0.2,3,"starburst energy injection rate (thick-disk, upper)",type2)

# --- SN explosions pressure effect on hot ISM (Thompson et al 2005) --	#
print "------------"
print "+[ shock P = 10^-12*E_xry^(17/14)*n_mol^(-4/7)*SNrate/Vol ]+"
def A_pc2(R):
	A=math.pi*R**2
#	print "Starburst Area = ", '%.2e' %(A) , "[pc^2]"
	return A

def V_pc3(R,z):
	V=math.pi*R**2*z
	return V
# SNrate_V=SNrate/V_starburst
V_conti=V_pc3(R_conti_pc,z_starburst_pc)
V_greve1=V_pc3(R_starburst_pc_greve,z_starburst_pc_greve)
V_greve2=2.0e10 # (Greve 2000)
E_init=E_xotf
n_ambi=n_mol

def p_SNhot(V,type):
	rate_V=SNrate/V
	P=1.0e-12*(E_init/1.0e51)**(17.0/14)*(n_ambi/0.01)**(-4.0/7)*(rate_V/1.0e-13) # [erg cm^-3]
	print "    data from", type
	print "    starburst Volume = ", '%.2e' %(V), "[pc^3]"
	print " o SN shock-heated P: ",  '%.2e' %(P)
#	print "SN explosion P (shock-heated hot ISM): ", P
	return P
# E_init [erg]
# n_ambi [cm^-3]
# SNrate_V [yr^-1 pc^-3]
# SNrate_V=SNrateate per volume
p_SNhot_conti=p_SNhot(V_conti,"89GHz Continuum")
p_SNhot_greve1=p_SNhot(V_greve1,"Greve 2000 (1)")
p_SNhot_greve2=p_SNhot(V_greve2, "Greve 2000 (2)")

# unit checked

# --- thermal pressure --------------------------------	#
print "------------"
print "+[ thermal P = n*k*T ]+"
p_thm_mol=n_mol*k_B*T_mol
#p1=1000*k_B*100
#p2=100*k_B*10
#print "pppp",p1,p2
p_thm_xotf=2*n_xotf*kT_xotf
p_thm_xotf_inui=4.9e-12*fill**(-0.5)
print " o molecular gas thermal P: ", p_thm_mol
print " o ionized gas thermal P: ",  '%.2e' %(p_thm_xotf)
print " o ionized gas thermal P (Inui): ", p_thm_xotf_inui
# unit checked

# --- radiation pressure (Thompson et al 2005) --------	#
print "------------"
print "+[ radiation P = effic*SFR/Area*c ]+"
# SFR_A=SFR/(A_starburst)
A_starburst=A_pc2(R_conti_pc)*pc**2
SFR_A=SFR/(A_starburst)
# when tau << 1
p_rad_thin=c*effi_mass2rad*SFR_A
# when tau >= 1
p_rad_thick=c*effi_mass2rad*SFR_A*(1.0/2)*tau
#print " o optically thin radiation P: ",  '%.2e' %(p_rad_thin)
print " o optically thick radiation P: ",  '%.2e' %(p_rad_thick)
# unit checked

# --- SN explosion pressure affect on cold ISM (Thompson et al 2005) --	#
print "------------"
print "+[ SN explosion P = 5*n_mol^(-1/4)*E_xry^(13/14)*P_rad ]+"
# E_init=E_xotf
# n_ambi=n_mol
p_SN_cold=5*(n_ambi/1.0)**(-1.0/4)*(E_init/1.0e51)**(13.0/14)*p_rad_thick
print " o SN explosion P (cold ISM): ",  '%.2e' %(p_SN_cold)
print "------------"
# unit checked

# ---------------------------------------------	#

# --- reference -------------------------------	#
# Chevalier et al. 2001, ApJ, 558, L27
# Chevalier et al. 1985, Nature, 317, 44
# Greve et al. 2000, AA, 364, 409
# Gunn & Gott 1972, ApJ, 176, 1
# Inui et al. 2005, P: ASJ, 57, 135
# Sakamoto et al. 1995, AJ, 110, 2075
# Strickland & Stevens 2000, MNRAS, 314, 511
# Tarchi et al. 2000, 358, 95
# Tsai et al. 2009, P: ASJ, 61, 237
# Thompson et al. 2005, ApJ, 630, 167
# Vollmer et al. 2001, ApJ, 561, 708
# Vollmer et al. 2005, AA, 441, 473

exit

