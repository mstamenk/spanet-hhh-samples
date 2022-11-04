# Samples for SPANet HHH studies
Framework to generate events to produce HHH 14 TeV samples to run with SPANet

# Setting up Madgraph

Download latest Madgraph version 3.4 from [launchpad|https://launchpad.net/mg5amcnlo]

```
source /cvmfs/sft.cern.ch/lcg/views/LCG_99/x86_64-centos7-gcc10-opt/setup.sh
git clone git@github.com:mstamenk/spanet-hhh-samples.git
tar -xf MG5_aMC_v3.4.1.tar
cd MG5_aMC_v3_4_1 
./bin/mg5_aMC
install pythia8
install Delphes
```

Copy the model to generate HHH samples:

```
cp -r custom-models/loop_sm_* MG5_aMC_v3_4_1/models/
```









