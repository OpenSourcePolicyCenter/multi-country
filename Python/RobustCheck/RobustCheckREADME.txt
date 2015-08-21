The purpose of this folder is save the stages of the code corresponding to the
sections within the step-by-step pdf documentation and check them, using parallel,
to see if the code holds up with multiple combinations of countries/cohort levels.

The .xls was complied from the .csv files that the code outputs. If the code runs
properly then "Yes" will be in the field and "No" if the code doesn't run properly.
Each sheet in the .xls file will correspond to a sigma value.

In general, the root processor is in charge of creating the .csv files and the individual
processors work through different combinations of countries and cohort levels. Originally,
these were designed to work on the Supercomputer, but were scaled down to work on multi-core
computers.

Stage 1-Basic Model (Meant for 7 processors)

Stage 2-Included Basic Demographics (Meant for 6 processors)
