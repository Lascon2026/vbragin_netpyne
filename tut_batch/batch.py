from netpyne.batch import Batch

params = {}

# fill in with parameters to explore and range of values (key has to coincide with those used in simConfig)
params['synMechTau2'] = [3.0, 5.0, 7.0]
params['connWeight'] = [0.005, 0.01, 0.15]

# create Batch object with parameters to modify, and specifying files to use
b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py',)

# Set output folder, grid method (all param combinations), and run configuration
b.saveFolder = 'data'
b.batchLabel = 'tauWeight'
b.method = 'grid' 
b.runCfg = {'type': 'mpi_bulletin',
            'script': 'init.py',
            'skip': True}

# Run batch simulations
b.run()