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
Options are specified separately for each queue partition. For example:

```toml
[normal]
cores = 56
max-nodes = 1280

[development]
cores = 56
max-nodes = 40
```

This sets the number of cores and maximum number of nodes per job for the
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
ezlaunch -J myjob 'echo "hello world"' -N 1 -n 1 -r 00:10:00 -p normal
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

The scripts slaunch and rlaunch run a given command on combinations of
subjects and runs. These scripts can optionally use the SUBJIDFORMAT
environment variable. This allows automatic conversion between subject
numbers (e.g., 5) and subject IDs (e.g., sub-05). For that example, you 
would set:

```bash
export SUBJIDFORMAT='sub-%02d'
```

Then subject number lists can be converted, for example `subjids 1:2:3` 
will produce `sub-01:sub-02:sub-03`. 

## Authors

* Neal Morton
* Russ Poldrack - wrote original launch script
