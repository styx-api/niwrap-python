# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

T4IMGS_4DFP_METADATA = Metadata(
    id="f59930980573ba4f92691ede7675eb588b9ae991.boutiques",
    name="t4imgs_4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


T4imgs4dfpParameters = typing.TypedDict('T4imgs4dfpParameters', {
    "__STYX_TYPE__": typing.Literal["t4imgs_4dfp"],
    "sqrt_normalize": bool,
    "cubic_spline": bool,
    "output_nan": bool,
    "convert_t4": bool,
    "nearest_neighbor": bool,
    "output_111_space": bool,
    "output_222_space": bool,
    "output_333n_space": typing.NotRequired[str | None],
    "duplicate_dimensions": typing.NotRequired[str | None],
    "big_endian": bool,
    "little_endian": bool,
    "input_images": list[InputPathType],
    "output_image": str,
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
        "t4imgs_4dfp": t4imgs_4dfp_cargs,
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
        "t4imgs_4dfp": t4imgs_4dfp_outputs,
    }.get(t)


class T4imgs4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `t4imgs_4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_image: OutputPathType
    """Transformed 4dfp image as output."""


def t4imgs_4dfp_params(
    input_images: list[InputPathType],
    output_image: str,
    sqrt_normalize: bool = False,
    cubic_spline: bool = False,
    output_nan: bool = False,
    convert_t4: bool = False,
    nearest_neighbor: bool = False,
    output_111_space: bool = False,
    output_222_space: bool = False,
    output_333n_space: str | None = None,
    duplicate_dimensions: str | None = None,
    big_endian: bool = False,
    little_endian: bool = False,
) -> T4imgs4dfpParameters:
    """
    Build parameters.
    
    Args:
        input_images: Input list of 4dfp images.
        output_image: Output file name for the transformed image.
        sqrt_normalize: Normalize by sqrt(n) rather than n (for z images).
        cubic_spline: Interpolate by 3D cubic spline (default is 3D linear).
        output_nan: Output NaN (default 0.0) for undefined values.
        convert_t4: Internally convert to_711-2A_t4->to_711-2B_t4.
        nearest_neighbor: Use nearest neighbor interpolation.
        output_111_space: Output in 111 space instead of default 333.0 space.
        output_222_space: Output in 222 space instead of default 333.0 space.
        output_333n_space: Output in 333.n space (y shifted up by n pixels).
        duplicate_dimensions: Duplicate dimensions of specified image.
        big_endian: Output in big endian format.
        little_endian: Output in little endian format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "t4imgs_4dfp",
        "sqrt_normalize": sqrt_normalize,
        "cubic_spline": cubic_spline,
        "output_nan": output_nan,
        "convert_t4": convert_t4,
        "nearest_neighbor": nearest_neighbor,
        "output_111_space": output_111_space,
        "output_222_space": output_222_space,
        "big_endian": big_endian,
        "little_endian": little_endian,
        "input_images": input_images,
        "output_image": output_image,
    }
    if output_333n_space is not None:
        params["output_333n_space"] = output_333n_space
    if duplicate_dimensions is not None:
        params["duplicate_dimensions"] = duplicate_dimensions
    return params


def t4imgs_4dfp_cargs(
    params: T4imgs4dfpParameters,
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
    cargs.append("t4imgs_4dfp")
    if params.get("sqrt_normalize"):
        cargs.append("-z")
    if params.get("cubic_spline"):
        cargs.append("-s")
    if params.get("output_nan"):
        cargs.append("-N")
    if params.get("convert_t4"):
        cargs.append("-B")
    if params.get("nearest_neighbor"):
        cargs.append("-n")
    if params.get("output_111_space"):
        cargs.append("-O111")
    if params.get("output_222_space"):
        cargs.append("-O222")
    if params.get("output_333n_space") is not None:
        cargs.extend([
            "-O333.n",
            params.get("output_333n_space")
        ])
    if params.get("duplicate_dimensions") is not None:
        cargs.extend([
            "-O",
            params.get("duplicate_dimensions")
        ])
    if params.get("big_endian"):
        cargs.append("-@b")
    if params.get("little_endian"):
        cargs.append("-@l")
    cargs.extend([execution.input_file(f) for f in params.get("input_images")])
    cargs.append(params.get("output_image"))
    return cargs


def t4imgs_4dfp_outputs(
    params: T4imgs4dfpParameters,
    execution: Execution,
) -> T4imgs4dfpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = T4imgs4dfpOutputs(
        root=execution.output_file("."),
        transformed_image=execution.output_file(params.get("output_image") + ".4dfp.img"),
    )
    return ret


def t4imgs_4dfp_execute(
    params: T4imgs4dfpParameters,
    execution: Execution,
) -> T4imgs4dfpOutputs:
    """
    Freesurfer tool for transforming images according to a specified T4 file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `T4imgs4dfpOutputs`).
    """
    params = execution.params(params)
    cargs = t4imgs_4dfp_cargs(params, execution)
    ret = t4imgs_4dfp_outputs(params, execution)
    execution.run(cargs)
    return ret


def t4imgs_4dfp(
    input_images: list[InputPathType],
    output_image: str,
    sqrt_normalize: bool = False,
    cubic_spline: bool = False,
    output_nan: bool = False,
    convert_t4: bool = False,
    nearest_neighbor: bool = False,
    output_111_space: bool = False,
    output_222_space: bool = False,
    output_333n_space: str | None = None,
    duplicate_dimensions: str | None = None,
    big_endian: bool = False,
    little_endian: bool = False,
    runner: Runner | None = None,
) -> T4imgs4dfpOutputs:
    """
    Freesurfer tool for transforming images according to a specified T4 file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_images: Input list of 4dfp images.
        output_image: Output file name for the transformed image.
        sqrt_normalize: Normalize by sqrt(n) rather than n (for z images).
        cubic_spline: Interpolate by 3D cubic spline (default is 3D linear).
        output_nan: Output NaN (default 0.0) for undefined values.
        convert_t4: Internally convert to_711-2A_t4->to_711-2B_t4.
        nearest_neighbor: Use nearest neighbor interpolation.
        output_111_space: Output in 111 space instead of default 333.0 space.
        output_222_space: Output in 222 space instead of default 333.0 space.
        output_333n_space: Output in 333.n space (y shifted up by n pixels).
        duplicate_dimensions: Duplicate dimensions of specified image.
        big_endian: Output in big endian format.
        little_endian: Output in little endian format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `T4imgs4dfpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(T4IMGS_4DFP_METADATA)
    params = t4imgs_4dfp_params(
        sqrt_normalize=sqrt_normalize,
        cubic_spline=cubic_spline,
        output_nan=output_nan,
        convert_t4=convert_t4,
        nearest_neighbor=nearest_neighbor,
        output_111_space=output_111_space,
        output_222_space=output_222_space,
        output_333n_space=output_333n_space,
        duplicate_dimensions=duplicate_dimensions,
        big_endian=big_endian,
        little_endian=little_endian,
        input_images=input_images,
        output_image=output_image,
    )
    return t4imgs_4dfp_execute(params, execution)


__all__ = [
    "T4IMGS_4DFP_METADATA",
    "T4imgs4dfpOutputs",
    "T4imgs4dfpParameters",
    "t4imgs_4dfp",
    "t4imgs_4dfp_params",
]
