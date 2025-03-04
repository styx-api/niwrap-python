# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLCC_METADATA = Metadata(
    id="39e2d4230b27cc7b8202577c5ebeea8323d5f9cd.boutiques",
    name="fslcc",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslccParameters = typing.TypedDict('FslccParameters', {
    "__STYX_TYPE__": typing.Literal["fslcc"],
    "first_input": InputPathType,
    "second_input": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "noabs_flag": bool,
    "nodemean_flag": bool,
    "threshold": typing.NotRequired[float | None],
    "decimal_places": typing.NotRequired[float | None],
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
        "fslcc": fslcc_cargs,
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


class FslccOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslcc_params(
    first_input: InputPathType,
    second_input: InputPathType,
    mask: InputPathType | None = None,
    noabs_flag: bool = False,
    nodemean_flag: bool = False,
    threshold: float | None = 0.1,
    decimal_places: float | None = 2,
) -> FslccParameters:
    """
    Build parameters.
    
    Args:
        first_input: First input time-series.
        second_input: Second input time-series.
        mask: Mask file name.
        noabs_flag: Don't return absolute values (keep sign).
        nodemean_flag: Don't demean the input files.
        threshold: Threshold (default 0.1).
        decimal_places: Number of decimal places to display in output (default\
            2).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslcc",
        "first_input": first_input,
        "second_input": second_input,
        "noabs_flag": noabs_flag,
        "nodemean_flag": nodemean_flag,
    }
    if mask is not None:
        params["mask"] = mask
    if threshold is not None:
        params["threshold"] = threshold
    if decimal_places is not None:
        params["decimal_places"] = decimal_places
    return params


def fslcc_cargs(
    params: FslccParameters,
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
    cargs.append("fslcc")
    cargs.append(execution.input_file(params.get("first_input")))
    cargs.append(execution.input_file(params.get("second_input")))
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask"))
        ])
    if params.get("noabs_flag"):
        cargs.append("--noabs")
    if params.get("nodemean_flag"):
        cargs.append("--nodemean")
    if params.get("threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("threshold"))
        ])
    if params.get("decimal_places") is not None:
        cargs.extend([
            "-p",
            str(params.get("decimal_places"))
        ])
    return cargs


def fslcc_outputs(
    params: FslccParameters,
    execution: Execution,
) -> FslccOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslccOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslcc_execute(
    params: FslccParameters,
    execution: Execution,
) -> FslccOutputs:
    """
    Cross-correlate two time-series, timepoint by timepoint.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslccOutputs`).
    """
    params = execution.params(params)
    cargs = fslcc_cargs(params, execution)
    ret = fslcc_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslcc(
    first_input: InputPathType,
    second_input: InputPathType,
    mask: InputPathType | None = None,
    noabs_flag: bool = False,
    nodemean_flag: bool = False,
    threshold: float | None = 0.1,
    decimal_places: float | None = 2,
    runner: Runner | None = None,
) -> FslccOutputs:
    """
    Cross-correlate two time-series, timepoint by timepoint.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        first_input: First input time-series.
        second_input: Second input time-series.
        mask: Mask file name.
        noabs_flag: Don't return absolute values (keep sign).
        nodemean_flag: Don't demean the input files.
        threshold: Threshold (default 0.1).
        decimal_places: Number of decimal places to display in output (default\
            2).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslccOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCC_METADATA)
    params = fslcc_params(
        first_input=first_input,
        second_input=second_input,
        mask=mask,
        noabs_flag=noabs_flag,
        nodemean_flag=nodemean_flag,
        threshold=threshold,
        decimal_places=decimal_places,
    )
    return fslcc_execute(params, execution)


__all__ = [
    "FSLCC_METADATA",
    "FslccOutputs",
    "FslccParameters",
    "fslcc",
    "fslcc_params",
]
