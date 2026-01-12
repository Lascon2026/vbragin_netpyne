from netpyne import specs

# Simulation options
cfg = specs.SimConfig()       # object of class SimConfig to store simulation configuration

cfg.duration = 1*1e3          # Duration of the simulation, in ms
cfg.dt = 0.01                # Internal integration timestep to use
cfg.verbose = False           # Show detailed messages
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.1          # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'tut_oscillation'  # Set file output name
cfg.savePickle = True


# simConfig.analysis['plotTraces'] = {'include': [1], 'saveFig': True}  # Plot recorded traces for this list of cells
cfg.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
# cfg.analysis['plotSpikeHist'] = {'include': ['E', 'I'], 'showFig': True}
cfg.analysis['plotRateSpectrogram'] = {'include': ['all'], 'saveFig': True}