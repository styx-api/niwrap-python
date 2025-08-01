# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CSVPRINT_METADATA = Metadata(
    id="88fe426126aea1052da673cfeee9f2078fb01491.boutiques",
    name="csvprint",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


CsvprintParameters = typing.TypedDict('CsvprintParameters', {
    "__STYXTYPE__": typing.Literal["csvprint"],
    "infile": InputPathType,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "csvprint": csvprint_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class CsvprintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `csvprint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def csvprint_params(
    infile: InputPathType,
) -> CsvprintParameters:
    """
    Build parameters.
    
    Args:
        infile: Input CSV file to be printed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "csvprint",
        "infile": infile,
    }
    return params


def csvprint_cargs(
    params: CsvprintParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("csvprint")
    cargs.append(execution.input_file(params.get("infile")))
    return cargs


def csvprint_outputs(
    params: CsvprintParameters,
    execution: Execution,
) -> CsvprintOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CsvprintOutputs(
        root=execution.output_file("."),
    )
    return ret


def csvprint_execute(
    params: CsvprintParameters,
    execution: Execution,
) -> CsvprintOutputs:
    """
    Command-line tool for printing CSV files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CsvprintOutputs`).
    """
    params = execution.params(params)
    cargs = csvprint_cargs(params, execution)
    ret = csvprint_outputs(params, execution)
    execution.run(cargs)
    return ret


def csvprint(
    infile: InputPathType,
    runner: Runner | None = None,
) -> CsvprintOutputs:
    """
    Command-line tool for printing CSV files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input CSV file to be printed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CsvprintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CSVPRINT_METADATA)
    params = csvprint_params(
        infile=infile,
    )
    return csvprint_execute(params, execution)


__all__ = [
    "CSVPRINT_METADATA",
    "CsvprintOutputs",
    "CsvprintParameters",
    "csvprint",
    "csvprint_params",
]
