# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMG2STDCOORD_METADATA = Metadata(
    id="1d7099e68b2ebab0fcf6f19fecfa832c5ec7908f.boutiques",
    name="img2stdcoord",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Img2stdcoordParameters = typing.TypedDict('Img2stdcoordParameters', {
    "__STYX_TYPE__": typing.Literal["img2stdcoord"],
    "coordinate_file": str,
    "input_image": InputPathType,
    "standard_image": typing.NotRequired[InputPathType | None],
    "affine_transform": typing.NotRequired[InputPathType | None],
    "warp_field": typing.NotRequired[InputPathType | None],
    "prewarp_affine_transform": typing.NotRequired[InputPathType | None],
    "voxel_flag": bool,
    "mm_flag": bool,
    "verbose_flag_1": bool,
    "verbose_flag_2": bool,
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
        "img2stdcoord": img2stdcoord_cargs,
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


class Img2stdcoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `img2stdcoord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def img2stdcoord_params(
    coordinate_file: str,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    voxel_flag: bool = False,
    mm_flag: bool = False,
    verbose_flag_1: bool = False,
    verbose_flag_2: bool = False,
    help_flag: bool = False,
) -> Img2stdcoordParameters:
    """
    Build parameters.
    
    Args:
        coordinate_file: Filename containing coordinates. If '-' is used,\
            coordinates are read from standard input.
        input_image: Filename of input image.
        standard_image: Filename of standard image.
        affine_transform: Filename of affine transform (e.g.,\
            example_func2standard.mat).
        warp_field: Filename of warp field (e.g.,\
            highres2standard_warp.nii.gz).
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.,\
            example_func2highres.mat). Default is identity.
        voxel_flag: Input coordinates in voxels (default).
        mm_flag: Input coordinates in mm.
        verbose_flag_1: Verbose output.
        verbose_flag_2: More verbose output.
        help_flag: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "img2stdcoord",
        "coordinate_file": coordinate_file,
        "input_image": input_image,
        "voxel_flag": voxel_flag,
        "mm_flag": mm_flag,
        "verbose_flag_1": verbose_flag_1,
        "verbose_flag_2": verbose_flag_2,
        "help_flag": help_flag,
    }
    if standard_image is not None:
        params["standard_image"] = standard_image
    if affine_transform is not None:
        params["affine_transform"] = affine_transform
    if warp_field is not None:
        params["warp_field"] = warp_field
    if prewarp_affine_transform is not None:
        params["prewarp_affine_transform"] = prewarp_affine_transform
    return params


def img2stdcoord_cargs(
    params: Img2stdcoordParameters,
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
    cargs.append("img2stdcoord")
    cargs.append(params.get("coordinate_file"))
    cargs.extend([
        "-img",
        execution.input_file(params.get("input_image"))
    ])
    if params.get("standard_image") is not None:
        cargs.extend([
            "-std",
            execution.input_file(params.get("standard_image"))
        ])
    if params.get("affine_transform") is not None:
        cargs.extend([
            "-xfm",
            execution.input_file(params.get("affine_transform"))
        ])
    if params.get("warp_field") is not None:
        cargs.extend([
            "-warp",
            execution.input_file(params.get("warp_field"))
        ])
    if params.get("prewarp_affine_transform") is not None:
        cargs.extend([
            "-premat",
            execution.input_file(params.get("prewarp_affine_transform"))
        ])
    if params.get("voxel_flag"):
        cargs.append("-vox")
    if params.get("mm_flag"):
        cargs.append("-mm")
    if params.get("verbose_flag_1"):
        cargs.append("-v")
    if params.get("verbose_flag_2"):
        cargs.append("-verbose")
    if params.get("help_flag"):
        cargs.append("-help")
    return cargs


def img2stdcoord_outputs(
    params: Img2stdcoordParameters,
    execution: Execution,
) -> Img2stdcoordOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Img2stdcoordOutputs(
        root=execution.output_file("."),
    )
    return ret


def img2stdcoord_execute(
    params: Img2stdcoordParameters,
    execution: Execution,
) -> Img2stdcoordOutputs:
    """
    Transforms image coordinates using standard space transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Img2stdcoordOutputs`).
    """
    params = execution.params(params)
    cargs = img2stdcoord_cargs(params, execution)
    ret = img2stdcoord_outputs(params, execution)
    execution.run(cargs)
    return ret


def img2stdcoord(
    coordinate_file: str,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    voxel_flag: bool = False,
    mm_flag: bool = False,
    verbose_flag_1: bool = False,
    verbose_flag_2: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> Img2stdcoordOutputs:
    """
    Transforms image coordinates using standard space transformations.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        coordinate_file: Filename containing coordinates. If '-' is used,\
            coordinates are read from standard input.
        input_image: Filename of input image.
        standard_image: Filename of standard image.
        affine_transform: Filename of affine transform (e.g.,\
            example_func2standard.mat).
        warp_field: Filename of warp field (e.g.,\
            highres2standard_warp.nii.gz).
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.,\
            example_func2highres.mat). Default is identity.
        voxel_flag: Input coordinates in voxels (default).
        mm_flag: Input coordinates in mm.
        verbose_flag_1: Verbose output.
        verbose_flag_2: More verbose output.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Img2stdcoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMG2STDCOORD_METADATA)
    params = img2stdcoord_params(
        coordinate_file=coordinate_file,
        input_image=input_image,
        standard_image=standard_image,
        affine_transform=affine_transform,
        warp_field=warp_field,
        prewarp_affine_transform=prewarp_affine_transform,
        voxel_flag=voxel_flag,
        mm_flag=mm_flag,
        verbose_flag_1=verbose_flag_1,
        verbose_flag_2=verbose_flag_2,
        help_flag=help_flag,
    )
    return img2stdcoord_execute(params, execution)


__all__ = [
    "IMG2STDCOORD_METADATA",
    "Img2stdcoordOutputs",
    "Img2stdcoordParameters",
    "img2stdcoord",
    "img2stdcoord_params",
]
