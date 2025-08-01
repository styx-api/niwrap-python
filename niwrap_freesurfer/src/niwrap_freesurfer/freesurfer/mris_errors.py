# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ERRORS_METADATA = Metadata(
    id="84c4666dcea46df17569c6e5d435ebf2cb451d60.boutiques",
    name="mris_errors",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisErrorsParameters = typing.TypedDict('MrisErrorsParameters', {
    "__STYXTYPE__": typing.Literal["mris_errors"],
    "input_image_file": InputPathType,
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
        "mris_errors": mris_errors_cargs,
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


class MrisErrorsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_errors(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_errors_params(
    input_image_file: InputPathType,
) -> MrisErrorsParameters:
    """
    Build parameters.
    
    Args:
        input_image_file: Input image file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_errors",
        "input_image_file": input_image_file,
    }
    return params


def mris_errors_cargs(
    params: MrisErrorsParameters,
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
    cargs.append("mris_errors")
    cargs.append(execution.input_file(params.get("input_image_file")))
    return cargs


def mris_errors_outputs(
    params: MrisErrorsParameters,
    execution: Execution,
) -> MrisErrorsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisErrorsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_errors_execute(
    params: MrisErrorsParameters,
    execution: Execution,
) -> MrisErrorsOutputs:
    """
    This program will unfold an MRI on the surface of an ellipsoid.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisErrorsOutputs`).
    """
    params = execution.params(params)
    cargs = mris_errors_cargs(params, execution)
    ret = mris_errors_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_errors(
    input_image_file: InputPathType,
    runner: Runner | None = None,
) -> MrisErrorsOutputs:
    """
    This program will unfold an MRI on the surface of an ellipsoid.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image_file: Input image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisErrorsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ERRORS_METADATA)
    params = mris_errors_params(
        input_image_file=input_image_file,
    )
    return mris_errors_execute(params, execution)


__all__ = [
    "MRIS_ERRORS_METADATA",
    "MrisErrorsOutputs",
    "MrisErrorsParameters",
    "mris_errors",
    "mris_errors_params",
]
