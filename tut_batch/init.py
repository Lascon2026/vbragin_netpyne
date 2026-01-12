from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise defaults are used
simConfig, netParams = sim.readCmdLineArgs()

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)