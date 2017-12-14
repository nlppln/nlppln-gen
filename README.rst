# nlppln-gen

Command line tool to create boilerplate Python commands and CWL steps for [nlppln](https://github.com/nlppln/nlppln).

## Generating command line NLP tool boilerplate and cwl steps

NLP Pipeline contains functionality to generate command line NLP tools and CWL
steps. To generate a command line tool and/or CWL step run:

    python -m nlpplngen.generate

This command starts a command line interface that asks you to specify the inputs and outputs of the tool:

```
> python -m nlppln.generate
Generate python command? [y]:
Generate cwl step? [y]:
Command name [command]:
Metadata input file? [n]: y
Multiple input files? [y]:
Multiple output files? [y]:
Extension of output files? [json]:
Metadata output file? [n]: y
Save python command to [nlppln/command.py]:
Save metadata to? [metadata_out.csv]:
Save cwl step to [cwl/steps/command.cwl]:
```
