

shower_moliere_radius = 2.3 # cms
shower_radiation_length = 0.968 # cm
shower_critical_energy = 5.36 # Mev

#mean layer energy profile, taken from TP studies for35 GeV Pt electrons
#to simulate 28-layers V7 geometry, group the first two layers and drop the last one according to:
#https://indico.cern.ch/event/458374/contribution/9/attachments/1179028/1828217/Andreev_29Oct2015.pdf 
shower_layers_energy = [40.0,69.8,119.6,178.9,248.8,315.1,382.0,431.6,477.7,
                        498.7,533.6,514.8,490.0,435.1,386.7,325.4,277.9,
                        224.4,186.5, 145.3,108.7,73.7,52.1,33.0,22.5,13.1,8.6,4.8]


#evolution vs depth described by a parabolic function
#set from TP studies (AMM), accuracy better than 5%
shower_transverse_parameters = dict(
  a0=9.-(18./63.),
  a1=135./630.,
  a2=45./630.
)

#longitudinal parameters, from TP studies https://indico.cern.ch/event/353342/contributions/830862/attachments/699977/961072/20141118CharlotHGCAL.ppt.pdf
shower_longitudinal_parameters = dict(
    meant0=-1.396,
    meant1=1.007,
    meanalpha0=-0.0433,
    meanalpha1=0.540,
    sigmalnt0=-2.506,
    sigmalnt1=1.245,
    sigmalnalpha0=-0.08442,
    sigmalnalpha1=0.7904,
    corrlnalphalnt0=0.7858,
    corrlnalphalnt1=-0.0232
)

# the sampling parameter, determines nhitspergev if fluctuation is true
shower_alpha = 0.25
