# launch
Programs for managing job submission through slurm.

These scripts can be used to submit jobs for a cluster running the
slurm scheduler. Some scripts are designed with neuroimaging data in
mind, for example running a single command to process data from multiple
participants in an experiment can be done using `slaunch`.

## Installation

Add `launch/bin` to your PATH. Set BATCHDIR to indicate the directory
in which job commands, slurm options, and job output should be saved.
If a job is called "myjob", then running a job will produce:

```bash
$BATCHDIR/myjob1.sh     # job commands 
$BATCHDIR/myjob1.slurm  # slurm options (run time, number of nodes, etc.)
$BATCHDIR/myjob1.out    # output from all commands
```

If you run another job named "myjob", that will be saved under 
"myjob2.sh", etc.

You may also define SUBJIDFORMAT. This allows automatic conversion 
between subject numbers (e.g., 5) and subject IDs (e.g., sub-05).
For that example, you would set:

```bash
export SUBJIDFORMAT='sub-%02d'
```

Then subject number lists can be converted, for example `subjids 1:2:3` 
will produce `sub-01:sub-02:sub-03`. 

## Authors

* Neal Morton
* Russ Poldrack - wrote original launch script
