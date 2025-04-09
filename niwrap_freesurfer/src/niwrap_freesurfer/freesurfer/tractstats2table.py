# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TRACTSTATS2TABLE_METADATA = Metadata(
    id="deb2a42839930436dbac59d0fe2517f06e878809.boutiques",
    name="tractstats2table",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Tractstats2tableParameters = typing.TypedDict('Tractstats2tableParameters', {
    "__STYX_TYPE__": typing.Literal["tractstats2table"],
    "inputs": typing.NotRequired[list[str] | None],
    "load_pathstats_from_file": typing.NotRequired[InputPathType | None],
    "overall": bool,
    "byvoxel": bool,
    "byvoxel_measure": typing.NotRequired[typing.Literal["AD", "RD", "MD", "FA"] | None],
    "tablefile": InputPathType,
    "delimiter": typing.NotRequired[typing.Literal["tab", "comma", "space", "semicolon"] | None],
    "transpose": bool,
    "debug": bool,
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
        "tractstats2table": tractstats2table_cargs,
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
        "tractstats2table": tractstats2table_outputs,
    }.get(t)


class Tractstats2tableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tractstats2table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_tablefile: OutputPathType
    """The output table file."""


def tractstats2table_params(
    tablefile: InputPathType,
    inputs: list[str] | None = None,
    load_pathstats_from_file: InputPathType | None = None,
    overall: bool = False,
    byvoxel: bool = False,
    byvoxel_measure: typing.Literal["AD", "RD", "MD", "FA"] | None = None,
    delimiter: typing.Literal["tab", "comma", "space", "semicolon"] | None = "tab",
    transpose: bool = False,
    debug: bool = False,
) -> Tractstats2tableParameters:
    """
    Build parameters.
    
    Args:
        tablefile: The output table file.
        inputs: Specify input stat files.
        load_pathstats_from_file: Name of the file which has the list of\
            subjects (one subject per line).
        overall: Operate on the overall path statistics.
        byvoxel: Operate on the byvoxel path statistics.
        byvoxel_measure: Specify byvoxel measure. One of [AD, RD, MD, FA].\
            Required with --byvoxel option.
        delimiter: Delimiter between measures in the table. Default is tab (alt\
            comma, space, semicolon).
        transpose: Transpose the table (default is subject in rows and\
            measures/count in cols).
        debug: Increase verbosity.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tractstats2table",
        "overall": overall,
        "byvoxel": byvoxel,
        "tablefile": tablefile,
        "transpose": transpose,
        "debug": debug,
    }
    if inputs is not None:
        params["inputs"] = inputs
    if load_pathstats_from_file is not None:
        params["load_pathstats_from_file"] = load_pathstats_from_file
    if byvoxel_measure is not None:
        params["byvoxel_measure"] = byvoxel_measure
    if delimiter is not None:
        params["delimiter"] = delimiter
    return params


def tractstats2table_cargs(
    params: Tractstats2tableParameters,
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
    cargs.append("tractstats2table")
    if params.get("inputs") is not None:
        cargs.extend([
            "--inputs",
            *params.get("inputs")
        ])
    if params.get("load_pathstats_from_file") is not None:
        cargs.extend([
            "--load-pathstats-from-file",
            execution.input_file(params.get("load_pathstats_from_file"))
        ])
    if params.get("overall"):
        cargs.append("-o")
    if params.get("byvoxel"):
        cargs.append("-b")
    if params.get("byvoxel_measure") is not None:
        cargs.extend([
            "--byvoxel-measure",
            params.get("byvoxel_measure")
        ])
    cargs.extend([
        "-t",
        execution.input_file(params.get("tablefile"))
    ])
    if params.get("delimiter") is not None:
        cargs.extend([
            "-d",
            params.get("delimiter")
        ])
    if params.get("transpose"):
        cargs.append("--transpose")
    if params.get("debug"):
        cargs.append("-v")
    return cargs


def tractstats2table_outputs(
    params: Tractstats2tableParameters,
    execution: Execution,
) -> Tractstats2tableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tractstats2tableOutputs(
        root=execution.output_file("."),
        output_tablefile=execution.output_file(pathlib.Path(params.get("tablefile")).name),
    )
    return ret


def tractstats2table_execute(
    params: Tractstats2tableParameters,
    execution: Execution,
) -> Tractstats2tableOutputs:
    """
    Converts a track overall stats file created by tracula into a table used for
    group statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tractstats2tableOutputs`).
    """
    params = execution.params(params)
    cargs = tractstats2table_cargs(params, execution)
    ret = tractstats2table_outputs(params, execution)
    execution.run(cargs)
    return ret


def tractstats2table(
    tablefile: InputPathType,
    inputs: list[str] | None = None,
    load_pathstats_from_file: InputPathType | None = None,
    overall: bool = False,
    byvoxel: bool = False,
    byvoxel_measure: typing.Literal["AD", "RD", "MD", "FA"] | None = None,
    delimiter: typing.Literal["tab", "comma", "space", "semicolon"] | None = "tab",
    transpose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> Tractstats2tableOutputs:
    """
    Converts a track overall stats file created by tracula into a table used for
    group statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        tablefile: The output table file.
        inputs: Specify input stat files.
        load_pathstats_from_file: Name of the file which has the list of\
            subjects (one subject per line).
        overall: Operate on the overall path statistics.
        byvoxel: Operate on the byvoxel path statistics.
        byvoxel_measure: Specify byvoxel measure. One of [AD, RD, MD, FA].\
            Required with --byvoxel option.
        delimiter: Delimiter between measures in the table. Default is tab (alt\
            comma, space, semicolon).
        transpose: Transpose the table (default is subject in rows and\
            measures/count in cols).
        debug: Increase verbosity.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tractstats2tableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRACTSTATS2TABLE_METADATA)
    params = tractstats2table_params(
        inputs=inputs,
        load_pathstats_from_file=load_pathstats_from_file,
        overall=overall,
        byvoxel=byvoxel,
        byvoxel_measure=byvoxel_measure,
        tablefile=tablefile,
        delimiter=delimiter,
        transpose=transpose,
        debug=debug,
    )
    return tractstats2table_execute(params, execution)


__all__ = [
    "TRACTSTATS2TABLE_METADATA",
    "Tractstats2tableOutputs",
    "Tractstats2tableParameters",
    "tractstats2table",
    "tractstats2table_params",
]
