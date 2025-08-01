# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLSELECTVOLS_METADATA = Metadata(
    id="3851b87d000f13b8596f3b7395c673cd4e806921.boutiques",
    name="fslselectvols",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslselectvolsParameters = typing.TypedDict('FslselectvolsParameters', {
    "__STYXTYPE__": typing.Literal["fslselectvols"],
    "input_file": InputPathType,
    "output_file": str,
    "vols_list": str,
    "output_mean_flag": bool,
    "output_variance_flag": bool,
    "help_flag": bool,
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
        "fslselectvols": fslselectvols_cargs,
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
        "fslselectvols": fslselectvols_outputs,
    }.get(t)


class FslselectvolsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslselectvols(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_4d_image: OutputPathType
    """Output 4D image with selected volumes"""


def fslselectvols_params(
    input_file: InputPathType,
    output_file: str,
    vols_list: str,
    output_mean_flag: bool = False,
    output_variance_flag: bool = False,
    help_flag: bool = False,
) -> FslselectvolsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file name (4D image).
        output_file: Output file name (4D image).
        vols_list: List of volumes to extract (comma-separated list or ascii\
            file).
        output_mean_flag: Output mean instead of concatenation.
        output_variance_flag: Output variance instead of concatenation.
        help_flag: Display help text.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslselectvols",
        "input_file": input_file,
        "output_file": output_file,
        "vols_list": vols_list,
        "output_mean_flag": output_mean_flag,
        "output_variance_flag": output_variance_flag,
        "help_flag": help_flag,
    }
    return params


def fslselectvols_cargs(
    params: FslselectvolsParameters,
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
    cargs.append("fslselectvols")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    cargs.extend([
        "--vols",
        params.get("vols_list")
    ])
    if params.get("output_mean_flag"):
        cargs.append("-m")
    if params.get("output_variance_flag"):
        cargs.append("-v")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def fslselectvols_outputs(
    params: FslselectvolsParameters,
    execution: Execution,
) -> FslselectvolsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslselectvolsOutputs(
        root=execution.output_file("."),
        output_4d_image=execution.output_file(params.get("output_file")),
    )
    return ret


def fslselectvols_execute(
    params: FslselectvolsParameters,
    execution: Execution,
) -> FslselectvolsOutputs:
    """
    Select volumes from a 4D time series and output a subset 4D volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslselectvolsOutputs`).
    """
    params = execution.params(params)
    cargs = fslselectvols_cargs(params, execution)
    ret = fslselectvols_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslselectvols(
    input_file: InputPathType,
    output_file: str,
    vols_list: str,
    output_mean_flag: bool = False,
    output_variance_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslselectvolsOutputs:
    """
    Select volumes from a 4D time series and output a subset 4D volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file name (4D image).
        output_file: Output file name (4D image).
        vols_list: List of volumes to extract (comma-separated list or ascii\
            file).
        output_mean_flag: Output mean instead of concatenation.
        output_variance_flag: Output variance instead of concatenation.
        help_flag: Display help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslselectvolsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSELECTVOLS_METADATA)
    params = fslselectvols_params(
        input_file=input_file,
        output_file=output_file,
        vols_list=vols_list,
        output_mean_flag=output_mean_flag,
        output_variance_flag=output_variance_flag,
        help_flag=help_flag,
    )
    return fslselectvols_execute(params, execution)


__all__ = [
    "FSLSELECTVOLS_METADATA",
    "FslselectvolsOutputs",
    "FslselectvolsParameters",
    "fslselectvols",
    "fslselectvols_params",
]
