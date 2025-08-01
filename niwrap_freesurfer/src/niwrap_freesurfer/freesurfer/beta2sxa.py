# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BETA2SXA_METADATA = Metadata(
    id="f0f822c3fdfc6946f2efbf9d1eba0fc23f0154a3.boutiques",
    name="beta2sxa",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Beta2sxaParameters = typing.TypedDict('Beta2sxaParameters', {
    "__STYXTYPE__": typing.Literal["beta2sxa"],
    "beta_files": list[InputPathType],
    "number_of_conditions": float,
    "number_of_per_subjects": float,
    "sxa_output": typing.NotRequired[str | None],
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
        "beta2sxa": beta2sxa_cargs,
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
        "beta2sxa": beta2sxa_outputs,
    }.get(t)


class Beta2sxaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `beta2sxa(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sxa_output_file: OutputPathType
    """Output file for tkmedit or tksurfer visualization."""


def beta2sxa_params(
    beta_files: list[InputPathType],
    number_of_conditions: float,
    number_of_per_subjects: float,
    sxa_output: str | None = "h.beta",
) -> Beta2sxaParameters:
    """
    Build parameters.
    
    Args:
        beta_files: Input beta files, e.g., data.nii.
        number_of_conditions: Number of groups or conditions.
        number_of_per_subjects: Number of subjects per group.
        sxa_output: Output sxa file. Default is h.beta.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "beta2sxa",
        "beta_files": beta_files,
        "number_of_conditions": number_of_conditions,
        "number_of_per_subjects": number_of_per_subjects,
    }
    if sxa_output is not None:
        params["sxa_output"] = sxa_output
    return params


def beta2sxa_cargs(
    params: Beta2sxaParameters,
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
    cargs.append("beta2sxa")
    cargs.extend([
        "--b",
        *[execution.input_file(f) for f in params.get("beta_files")]
    ])
    cargs.extend([
        "--nc",
        str(params.get("number_of_conditions"))
    ])
    cargs.extend([
        "--nper",
        str(params.get("number_of_per_subjects"))
    ])
    if params.get("sxa_output") is not None:
        cargs.extend([
            "--o",
            params.get("sxa_output")
        ])
    return cargs


def beta2sxa_outputs(
    params: Beta2sxaParameters,
    execution: Execution,
) -> Beta2sxaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Beta2sxaOutputs(
        root=execution.output_file("."),
        sxa_output_file=execution.output_file("h.[MASK].nii"),
    )
    return ret


def beta2sxa_execute(
    params: Beta2sxaParameters,
    execution: Execution,
) -> Beta2sxaOutputs:
    """
    A script to create files for plotting in tkmedit or tksurfer based on tabular
    data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Beta2sxaOutputs`).
    """
    params = execution.params(params)
    cargs = beta2sxa_cargs(params, execution)
    ret = beta2sxa_outputs(params, execution)
    execution.run(cargs)
    return ret


def beta2sxa(
    beta_files: list[InputPathType],
    number_of_conditions: float,
    number_of_per_subjects: float,
    sxa_output: str | None = "h.beta",
    runner: Runner | None = None,
) -> Beta2sxaOutputs:
    """
    A script to create files for plotting in tkmedit or tksurfer based on tabular
    data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        beta_files: Input beta files, e.g., data.nii.
        number_of_conditions: Number of groups or conditions.
        number_of_per_subjects: Number of subjects per group.
        sxa_output: Output sxa file. Default is h.beta.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Beta2sxaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BETA2SXA_METADATA)
    params = beta2sxa_params(
        beta_files=beta_files,
        number_of_conditions=number_of_conditions,
        number_of_per_subjects=number_of_per_subjects,
        sxa_output=sxa_output,
    )
    return beta2sxa_execute(params, execution)


__all__ = [
    "BETA2SXA_METADATA",
    "Beta2sxaOutputs",
    "Beta2sxaParameters",
    "beta2sxa",
    "beta2sxa_params",
]
