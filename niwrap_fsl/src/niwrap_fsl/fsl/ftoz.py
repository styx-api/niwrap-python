# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FTOZ_METADATA = Metadata(
    id="718b41cdb8c184566bcb56e5205ff75364795c69.boutiques",
    name="ftoz",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FtozParameters = typing.TypedDict('FtozParameters', {
    "__STYX_TYPE__": typing.Literal["ftoz"],
    "input_file": InputPathType,
    "dof1": float,
    "dof2": float,
    "output_file": typing.NotRequired[str | None],
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
        "ftoz": ftoz_cargs,
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
        "ftoz": ftoz_outputs,
    }.get(t)


class FtozOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ftoz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_zscores: OutputPathType | None
    """File containing the converted Z-scores"""


def ftoz_params(
    input_file: InputPathType,
    dof1: float,
    dof2: float,
    output_file: str | None = "zstats",
    help_flag: bool = False,
) -> FtozParameters:
    """
    Build parameters.
    
    Args:
        input_file: File containing F-statistics.
        dof1: Degrees of freedom 1 for F-to-Z conversion.
        dof2: Degrees of freedom 2 for F-to-Z conversion.
        output_file: Output file for Z-scores.
        help_flag: Display this help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ftoz",
        "input_file": input_file,
        "dof1": dof1,
        "dof2": dof2,
        "help_flag": help_flag,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def ftoz_cargs(
    params: FtozParameters,
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
    cargs.append("ftoz")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(str(params.get("dof1")))
    cargs.append(str(params.get("dof2")))
    if params.get("output_file") is not None:
        cargs.extend([
            "-zout",
            params.get("output_file")
        ])
    if params.get("help_flag"):
        cargs.append("-help")
    return cargs


def ftoz_outputs(
    params: FtozParameters,
    execution: Execution,
) -> FtozOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FtozOutputs(
        root=execution.output_file("."),
        output_zscores=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def ftoz_execute(
    params: FtozParameters,
    execution: Execution,
) -> FtozOutputs:
    """
    Convert F-statistics to Z-scores.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FtozOutputs`).
    """
    params = execution.params(params)
    cargs = ftoz_cargs(params, execution)
    ret = ftoz_outputs(params, execution)
    execution.run(cargs)
    return ret


def ftoz(
    input_file: InputPathType,
    dof1: float,
    dof2: float,
    output_file: str | None = "zstats",
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FtozOutputs:
    """
    Convert F-statistics to Z-scores.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: File containing F-statistics.
        dof1: Degrees of freedom 1 for F-to-Z conversion.
        dof2: Degrees of freedom 2 for F-to-Z conversion.
        output_file: Output file for Z-scores.
        help_flag: Display this help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FtozOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FTOZ_METADATA)
    params = ftoz_params(
        input_file=input_file,
        dof1=dof1,
        dof2=dof2,
        output_file=output_file,
        help_flag=help_flag,
    )
    return ftoz_execute(params, execution)


__all__ = [
    "FTOZ_METADATA",
    "FtozOutputs",
    "FtozParameters",
    "ftoz",
    "ftoz_params",
]
