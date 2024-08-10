# Samples for SPANet HHH studies
Framework to generate events to produce HHH 14 TeV samples to run with SPANet

# Setting up Madgraph

Download latest Madgraph version 3.4 from [launchpad](https://launchpad.net/mg5amcnlo) or directly from [GitHub](https://github.com/mg5amcnlo/mg5amcnlo)

```bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_99/x86_64-centos7-gcc10-opt/setup.sh
git clone git@github.com:mstamenk/spanet-hhh-samples.git
cd spanet-hhh-samples
git clone git@ggithub.com/mg5amcnlo/mg5amcnlo -b v3.4.1 MG5_aMC_v3_4_1
cd MG5_aMC_v3_4_1 
./bin/mg5_aMC
install pythia8
install Delphes
```

Copy the model to generate HHH samples:

```bash
cp -r custom-models/loop_sm_* MG5_aMC_v3_4_1/models/
```

Launch HHH from cards

```bash
./bin/mg5_aMC
convert model ./models/loop_sm_c3d4
!cat ../production-cards/GF_HHH_SM_loop_sm_c3d4_proc_card.dat
# copy the information there in the shell
launch
# provide path to run_card
../production-cards/GF_HHH_SM_loop_sm_c3d4_run_card.dat
```


# Cheat sheet

```bash
export MYROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHIA8DATA=$MYROOT/MG5_aMC_v3_4_1/HEPTools/pythia8/share/Pythia8/xmldoc/
```

```bash
set spinmode none # near the set lines
decay h > all all # near the decay lines
```

```bash
display diagrams # in mg5_aMC shell
```

```bash
generate p p > h h h [noborn=QCD]
```


```bash
set param_card tripcoup 4 0.000
set param_card quartcoup 6 0.000
```


```bash
set spinmode none 
decay h > b b~
```
