# Samples for SPANet HHH studies
Framework to generate events to produce HHH 14 TeV samples to run with SPANet

# Setting up Madgraph

Download latest Madgraph version 3.4 from [launchpad|https://launchpad.net/mg5amcnlo]

```
source /cvmfs/sft.cern.ch/lcg/views/LCG_99/x86_64-centos7-gcc10-opt/setup.sh
git clone git@github.com:mstamenk/spanet-hhh-samples.git
cd spanet-hhh-samples
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

Launch HHH from cards

```
./bin/mg5_aMC
!cat ../production-cards/GF_HHH_SM_loop_sm_c3d4_proc_card.dat
# copy the information there in the shell
launch
# provide path to run_card
../production-cards/GF_HHH_SM_loop_sm_c3d4_run_card.dat
```


# Cheat sheet

```
export MYROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHIA8DATA=$MYROOT/MG5_aMC_v3_4_1/HEPTools/pythia8/share/Pythia8/xmldoc/
```

```
set spinmode none # near the set lines
decay h > all all # near the decay lines
```

```
display diagrams # in mg5_aMC shell
```

```
generate p p > h h h [noborn=QCD]
```


```
set param_card tripcoup 4 0.000
set param_card quartcoup 6 0.000
```


```
set spinmode none 
decay h > b b~
```
