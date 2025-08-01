# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AVSCALE_METADATA = Metadata(
    id="0e38b15f172b6816bad2fcced45ef761f1d72adf.boutiques",
    name="avscale",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


AvscaleParameters = typing.TypedDict('AvscaleParameters', {
    "__STYXTYPE__": typing.Literal["avscale"],
    "allparams_flag": bool,
    "inverteddies_flag": bool,
    "matrix_file": InputPathType,
    "non_reference_volume": typing.NotRequired[InputPathType | None],
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
        "avscale": avscale_cargs,
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


class AvscaleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `avscale(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: list[str]
    """output affine transfomration file"""


def avscale_params(
    matrix_file: InputPathType,
    allparams_flag: bool = False,
    inverteddies_flag: bool = False,
    non_reference_volume: InputPathType | None = None,
) -> AvscaleParameters:
    """
    Build parameters.
    
    Args:
        matrix_file: The path to the matrix file.
        allparams_flag: Flag for all parameters.
        inverteddies_flag: Flag for inverted eddies.
        non_reference_volume: The path to the non-reference volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "avscale",
        "allparams_flag": allparams_flag,
        "inverteddies_flag": inverteddies_flag,
        "matrix_file": matrix_file,
    }
    if non_reference_volume is not None:
        params["non_reference_volume"] = non_reference_volume
    return params


def avscale_cargs(
    params: AvscaleParameters,
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
    cargs.append("avscale")
    if params.get("allparams_flag"):
        cargs.append("--allparams")
    if params.get("inverteddies_flag"):
        cargs.append("--inverteddies")
    cargs.append(execution.input_file(params.get("matrix_file")))
    if params.get("non_reference_volume") is not None:
        cargs.append(execution.input_file(params.get("non_reference_volume")))
    return cargs


def avscale_outputs(
    params: AvscaleParameters,
    execution: Execution,
) -> AvscaleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AvscaleOutputs(
        root=execution.output_file("."),
        output=[],
    )
    return ret


def avscale_execute(
    params: AvscaleParameters,
    execution: Execution,
) -> AvscaleOutputs:
    """
    A command line tool for computing affine transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AvscaleOutputs`).
    """
    params = execution.params(params)
    cargs = avscale_cargs(params, execution)
    ret = avscale_outputs(params, execution)
    execution.run(cargs, handle_stdout=lambda s: ret.output.append(s))
    return ret


def avscale(
    matrix_file: InputPathType,
    allparams_flag: bool = False,
    inverteddies_flag: bool = False,
    non_reference_volume: InputPathType | None = None,
    runner: Runner | None = None,
) -> AvscaleOutputs:
    """
    A command line tool for computing affine transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        matrix_file: The path to the matrix file.
        allparams_flag: Flag for all parameters.
        inverteddies_flag: Flag for inverted eddies.
        non_reference_volume: The path to the non-reference volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AvscaleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AVSCALE_METADATA)
    params = avscale_params(
        allparams_flag=allparams_flag,
        inverteddies_flag=inverteddies_flag,
        matrix_file=matrix_file,
        non_reference_volume=non_reference_volume,
    )
    return avscale_execute(params, execution)


__all__ = [
    "AVSCALE_METADATA",
    "AvscaleOutputs",
    "AvscaleParameters",
    "avscale",
    "avscale_params",
]
