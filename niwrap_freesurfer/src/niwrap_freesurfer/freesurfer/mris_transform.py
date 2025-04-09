# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_TRANSFORM_METADATA = Metadata(
    id="e6c41caaf057c6f68a1db006d796ff5fd5cf374b.boutiques",
    name="mris_transform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisTransformParameters = typing.TypedDict('MrisTransformParameters', {
    "__STYX_TYPE__": typing.Literal["mris_transform"],
    "input_surface": InputPathType,
    "transform": InputPathType,
    "output_surface": str,
    "trx_src": typing.NotRequired[InputPathType | None],
    "trx_dst": typing.NotRequired[InputPathType | None],
    "is_inverse": bool,
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
        "mris_transform": mris_transform_cargs,
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
        "mris_transform": mris_transform_outputs,
    }.get(t)


class MrisTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output_surface: OutputPathType
    """Transformed output surface file."""


def mris_transform_params(
    input_surface: InputPathType,
    transform: InputPathType,
    output_surface: str,
    trx_src: InputPathType | None = None,
    trx_dst: InputPathType | None = None,
    is_inverse: bool = False,
) -> MrisTransformParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file, e.g., lh.pial.
        transform: Image-to-image transform file, e.g., LTA or M3Z.
        output_surface: Output surface file, e.g., lh.out.pial.
        trx_src: Specify the source geometry if the transform was created by\
            MNI/mritotal or FSL/flirt.
        trx_dst: Specify the destination geometry if the transform does not\
            include this information or the path in the M3Z is invalid.
        is_inverse: Use this option when using a transform from destination to\
            source space.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_transform",
        "input_surface": input_surface,
        "transform": transform,
        "output_surface": output_surface,
        "is_inverse": is_inverse,
    }
    if trx_src is not None:
        params["trx_src"] = trx_src
    if trx_dst is not None:
        params["trx_dst"] = trx_dst
    return params


def mris_transform_cargs(
    params: MrisTransformParameters,
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
    cargs.append("mris_transform")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("transform")))
    cargs.append(params.get("output_surface"))
    if params.get("trx_src") is not None:
        cargs.extend([
            "--trx-src",
            execution.input_file(params.get("trx_src"))
        ])
    if params.get("trx_dst") is not None:
        cargs.extend([
            "--trx-dst",
            execution.input_file(params.get("trx_dst"))
        ])
    if params.get("is_inverse"):
        cargs.append("--is-inverse")
    return cargs


def mris_transform_outputs(
    params: MrisTransformParameters,
    execution: Execution,
) -> MrisTransformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisTransformOutputs(
        root=execution.output_file("."),
        transformed_output_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_transform_execute(
    params: MrisTransformParameters,
    execution: Execution,
) -> MrisTransformOutputs:
    """
    A tool to transform surfaces from one space to another using image transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisTransformOutputs`).
    """
    params = execution.params(params)
    cargs = mris_transform_cargs(params, execution)
    ret = mris_transform_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_transform(
    input_surface: InputPathType,
    transform: InputPathType,
    output_surface: str,
    trx_src: InputPathType | None = None,
    trx_dst: InputPathType | None = None,
    is_inverse: bool = False,
    runner: Runner | None = None,
) -> MrisTransformOutputs:
    """
    A tool to transform surfaces from one space to another using image transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file, e.g., lh.pial.
        transform: Image-to-image transform file, e.g., LTA or M3Z.
        output_surface: Output surface file, e.g., lh.out.pial.
        trx_src: Specify the source geometry if the transform was created by\
            MNI/mritotal or FSL/flirt.
        trx_dst: Specify the destination geometry if the transform does not\
            include this information or the path in the M3Z is invalid.
        is_inverse: Use this option when using a transform from destination to\
            source space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_TRANSFORM_METADATA)
    params = mris_transform_params(
        input_surface=input_surface,
        transform=transform,
        output_surface=output_surface,
        trx_src=trx_src,
        trx_dst=trx_dst,
        is_inverse=is_inverse,
    )
    return mris_transform_execute(params, execution)


__all__ = [
    "MRIS_TRANSFORM_METADATA",
    "MrisTransformOutputs",
    "MrisTransformParameters",
    "mris_transform",
    "mris_transform_params",
]
