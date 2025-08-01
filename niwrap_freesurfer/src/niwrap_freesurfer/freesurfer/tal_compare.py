# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TAL_COMPARE_METADATA = Metadata(
    id="48a87dd18545a8514cefe13e747f2239a4b0468e.boutiques",
    name="tal_compare",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TalCompareParameters = typing.TypedDict('TalCompareParameters', {
    "__STYXTYPE__": typing.Literal["tal_compare"],
    "ref_file": InputPathType,
    "moving_file": InputPathType,
    "output_file": str,
    "verbose": bool,
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
        "tal_compare": tal_compare_cargs,
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
        "tal_compare": tal_compare_outputs,
    }.get(t)


class TalCompareOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tal_compare(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    comparison_results: OutputPathType
    """Comparison results output file."""


def tal_compare_params(
    ref_file: InputPathType,
    moving_file: InputPathType,
    output_file: str,
    verbose: bool = False,
) -> TalCompareParameters:
    """
    Build parameters.
    
    Args:
        ref_file: Reference TAL database file.
        moving_file: Moving TAL database file to compare against the reference.
        output_file: Output file to store comparison results.
        verbose: Enable verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tal_compare",
        "ref_file": ref_file,
        "moving_file": moving_file,
        "output_file": output_file,
        "verbose": verbose,
    }
    return params


def tal_compare_cargs(
    params: TalCompareParameters,
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
    cargs.append("tal_compare")
    cargs.append(execution.input_file(params.get("ref_file")))
    cargs.append(execution.input_file(params.get("moving_file")))
    cargs.append(params.get("output_file"))
    if params.get("verbose"):
        cargs.append("-v")
    return cargs


def tal_compare_outputs(
    params: TalCompareParameters,
    execution: Execution,
) -> TalCompareOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TalCompareOutputs(
        root=execution.output_file("."),
        comparison_results=execution.output_file(params.get("output_file")),
    )
    return ret


def tal_compare_execute(
    params: TalCompareParameters,
    execution: Execution,
) -> TalCompareOutputs:
    """
    Tool for comparing TAL databases.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TalCompareOutputs`).
    """
    params = execution.params(params)
    cargs = tal_compare_cargs(params, execution)
    ret = tal_compare_outputs(params, execution)
    execution.run(cargs)
    return ret


def tal_compare(
    ref_file: InputPathType,
    moving_file: InputPathType,
    output_file: str,
    verbose: bool = False,
    runner: Runner | None = None,
) -> TalCompareOutputs:
    """
    Tool for comparing TAL databases.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        ref_file: Reference TAL database file.
        moving_file: Moving TAL database file to compare against the reference.
        output_file: Output file to store comparison results.
        verbose: Enable verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalCompareOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TAL_COMPARE_METADATA)
    params = tal_compare_params(
        ref_file=ref_file,
        moving_file=moving_file,
        output_file=output_file,
        verbose=verbose,
    )
    return tal_compare_execute(params, execution)


__all__ = [
    "TAL_COMPARE_METADATA",
    "TalCompareOutputs",
    "TalCompareParameters",
    "tal_compare",
    "tal_compare_params",
]
