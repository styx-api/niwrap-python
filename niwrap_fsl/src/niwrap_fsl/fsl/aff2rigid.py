# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AFF2RIGID_METADATA = Metadata(
    id="1c5bd7f0035a88c49ed0e7fc0bc2b90357a5176f.boutiques",
    name="aff2rigid",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Aff2rigidParameters = typing.TypedDict('Aff2rigidParameters', {
    "__STYXTYPE__": typing.Literal["aff2rigid"],
    "input_transform": InputPathType,
    "output_transform": str,
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
        "aff2rigid": aff2rigid_cargs,
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


class Aff2rigidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aff2rigid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def aff2rigid_params(
    input_transform: InputPathType,
    output_transform: str,
) -> Aff2rigidParameters:
    """
    Build parameters.
    
    Args:
        input_transform: Input FLIRT transform (12 DOF) from the input image to\
            standard space.
        output_transform: Output matrix which will convert the input image to\
            standard space using a 6 DOF transformation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "aff2rigid",
        "input_transform": input_transform,
        "output_transform": output_transform,
    }
    return params


def aff2rigid_cargs(
    params: Aff2rigidParameters,
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
    cargs.append("aff2rigid")
    cargs.append(execution.input_file(params.get("input_transform")))
    cargs.append(params.get("output_transform"))
    return cargs


def aff2rigid_outputs(
    params: Aff2rigidParameters,
    execution: Execution,
) -> Aff2rigidOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Aff2rigidOutputs(
        root=execution.output_file("."),
    )
    return ret


def aff2rigid_execute(
    params: Aff2rigidParameters,
    execution: Execution,
) -> Aff2rigidOutputs:
    """
    Tool for converting affine transformations to rigid transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Aff2rigidOutputs`).
    """
    params = execution.params(params)
    cargs = aff2rigid_cargs(params, execution)
    ret = aff2rigid_outputs(params, execution)
    execution.run(cargs)
    return ret


def aff2rigid(
    input_transform: InputPathType,
    output_transform: str,
    runner: Runner | None = None,
) -> Aff2rigidOutputs:
    """
    Tool for converting affine transformations to rigid transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_transform: Input FLIRT transform (12 DOF) from the input image to\
            standard space.
        output_transform: Output matrix which will convert the input image to\
            standard space using a 6 DOF transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aff2rigidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFF2RIGID_METADATA)
    params = aff2rigid_params(
        input_transform=input_transform,
        output_transform=output_transform,
    )
    return aff2rigid_execute(params, execution)


__all__ = [
    "AFF2RIGID_METADATA",
    "Aff2rigidOutputs",
    "Aff2rigidParameters",
    "aff2rigid",
    "aff2rigid_params",
]
