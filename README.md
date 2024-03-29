# launch
Programs for managing job submission through slurm.

These scripts can be used to submit jobs for a cluster running the
slurm scheduler. Some scripts are designed with neuroimaging data in
mind, for example running a single command to process data from multiple
participants in an experiment can be done using `slaunch`.

## Installation

To install the most recent release from PyPI, run:

```bash
pip install ezlaunch
```

To install the latest version on GitHub, run:

```bash
pip install git+https://github.com/prestonlab/launch
```

Verify installation by running `launch -h`.

## Configuration

The launch programs can use information about cluster configuration to
fill in blanks (e.g., the number of cores available on each node) and
to make sure you're not going over limits of the queue you're submitting
to (e.g., a maximum number of nodes).

The configuration is specified using TOML files, which have a simple format.
Global settings should go under a `[global]` heading, while partition-specific
settings should go under a heading with the name of that partition.
For example (here, "normal" and "development" are two partitions):

```toml
[global]
account = "myAccountName"

[normal]
cores = 56
max-nodes = 1280

[development]
cores = 56
max-nodes = 40
```

This sets the default account to use when submitting jobs. It also sets the number of 
cores and the maximum number of nodes per job for the
normal and development partitions. You may also set a `max-cores` option to
restrict the number of total cores used by a job.

The launch programs will look for a configuration file at `$HOME/.launch.toml`.
If you set the `LAUNCH_CONFIG` environment variable, launch will look there
instead.

### EZ Launch

In contrast to launch, which is relatively low level, ezlaunch manages 
command, batch script, and output files automatically.
To use ezlaunch, set the BATCHDIR environment variable to indicate the 
directory in which job commands, slurm options, and output should be saved.

For example, you could submit a job to a slurm cluster using something like:

```bash
ezlaunch -J myjob 'echo "hello world"' -N 1 -n 1 -r 00:10:00
```

After the job runs, you would have the following files: 

```bash
$BATCHDIR/myjob1.sh     # job commands 
$BATCHDIR/myjob1.slurm  # slurm options (run time, number of nodes, etc.)
$BATCHDIR/myjob1.out    # output from all commands
```

If you run another job named "myjob", that will be saved under 
"myjob2.sh", etc.

### Running a command for multiple subjects

The slaunch command makes it quick to process data from multiple subjects 
in parallel. As a toy example, we can run commands to greet each individual
subject:

```bash
slaunch -J greet 'echo "hello sub-{}"' 101:102:103 -N 1 -n 3 -r 00:10:00
```

This will generate three commands corresponding to the three subjects (101, 102, and 103)
and run the commands in parallel on different cores. Any `{}` in the command will be
replaced with the subject ID. Subject IDs must be in a list that is separated by colons (`:`).
Optionally, the subject list can be assigned to an environment variable for easier access
when running slaunch:

```bash
SUBJIDS=101:102:103:104:107:108:110:111
slaunch 'script1 {}' $SUBJIDS -N 1 -n 4 -r 01:00:00
slaunch 'script2 {}' $SUBJIDS -N 1 -n 4 -r 02:00:00
```

Note that the `-n` flag doesn't have to match the number of subjects. Here, the 8 subjects
will be run in two batches, 4 subjects at a time.

The slaunch command can optionally use the SUBJIDFORMAT
environment variable. This allows automatic conversion between subject
numbers (e.g., 5) and subject IDs (e.g., sub-05). For that example, you 
would set:

```bash
export SUBJIDFORMAT='sub-%02d'
```

Then subject number lists can be converted, for example `subjids 1:2:3` 
will produce `sub-01:sub-02:sub-03`. Use the `-g` flag when running slaunch
to use generated IDs instead of the raw IDs.

### Running subjects and runs in parallel

Similarly to slaunch, the rlaunch command can be used to run combinations
of subjects and runs in parallel. Here, instead of `{}`, you use `{s}` and
`{r}` to indicate where the subject and run numbers, respectively, should be 
substituted in the run command. For example:

```bash
rlaunch 'myscript {s} {r}' 101:102:103 1:2:3:4 -N 1 -n 12 -r 02:00:00
```

This will generate 12 commands with all combinations of subjects and runs and
run those commands in parallel.

## Authors

* Neal Morton
* Russ Poldrack - wrote original launch script
