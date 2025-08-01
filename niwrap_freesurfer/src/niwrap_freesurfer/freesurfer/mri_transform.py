# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_TRANSFORM_METADATA = Metadata(
    id="22b17ef4c1a157e2633827e670c9f3297b49ab98.boutiques",
    name="mri_transform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriTransformParameters = typing.TypedDict('MriTransformParameters', {
    "__STYXTYPE__": typing.Literal["mri_transform"],
    "input_volume": InputPathType,
    "lta_file": InputPathType,
    "output_file": str,
    "out_like": typing.NotRequired[InputPathType | None],
    "invert": bool,
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
        "mri_transform": mri_transform_cargs,
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
        "mri_transform": mri_transform_outputs,
    }.get(t)


class MriTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output: OutputPathType
    """Transformed output volume"""


def mri_transform_params(
    input_volume: InputPathType,
    lta_file: InputPathType,
    output_file: str,
    out_like: InputPathType | None = None,
    invert: bool = False,
) -> MriTransformParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input MRI volume.
        lta_file: Linear Transform Array (LTA) file.
        output_file: Output file for the transformed MRI volume.
        out_like: Set output volume parameters like the reference volume.
        invert: Invert transform coordinates.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_transform",
        "input_volume": input_volume,
        "lta_file": lta_file,
        "output_file": output_file,
        "invert": invert,
    }
    if out_like is not None:
        params["out_like"] = out_like
    return params


def mri_transform_cargs(
    params: MriTransformParameters,
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
    cargs.append("mri_transform")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("lta_file")))
    cargs.append(params.get("output_file"))
    if params.get("out_like") is not None:
        cargs.extend([
            "-out_like",
            execution.input_file(params.get("out_like"))
        ])
    if params.get("invert"):
        cargs.append("-I")
    return cargs


def mri_transform_outputs(
    params: MriTransformParameters,
    execution: Execution,
) -> MriTransformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriTransformOutputs(
        root=execution.output_file("."),
        transformed_output=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_transform_execute(
    params: MriTransformParameters,
    execution: Execution,
) -> MriTransformOutputs:
    """
    Applies a linear transform to an MRI volume and writes out the result.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriTransformOutputs`).
    """
    params = execution.params(params)
    cargs = mri_transform_cargs(params, execution)
    ret = mri_transform_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_transform(
    input_volume: InputPathType,
    lta_file: InputPathType,
    output_file: str,
    out_like: InputPathType | None = None,
    invert: bool = False,
    runner: Runner | None = None,
) -> MriTransformOutputs:
    """
    Applies a linear transform to an MRI volume and writes out the result.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MRI volume.
        lta_file: Linear Transform Array (LTA) file.
        output_file: Output file for the transformed MRI volume.
        out_like: Set output volume parameters like the reference volume.
        invert: Invert transform coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TRANSFORM_METADATA)
    params = mri_transform_params(
        input_volume=input_volume,
        lta_file=lta_file,
        output_file=output_file,
        out_like=out_like,
        invert=invert,
    )
    return mri_transform_execute(params, execution)


__all__ = [
    "MRI_TRANSFORM_METADATA",
    "MriTransformOutputs",
    "MriTransformParameters",
    "mri_transform",
    "mri_transform_params",
]
