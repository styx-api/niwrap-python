# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLASCII2IMG_METADATA = Metadata(
    id="7d9563406793caa4f2d7330380671357bb8fb341.boutiques",
    name="fslascii2img",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Fslascii2imgParameters = typing.TypedDict('Fslascii2imgParameters', {
    "__STYXTYPE__": typing.Literal["fslascii2img"],
    "infile": InputPathType,
    "xsize": int,
    "ysize": int,
    "zsize": int,
    "tsize": int,
    "xdim": float,
    "ydim": float,
    "zdim": float,
    "tr": float,
    "outfile": str,
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
        "fslascii2img": fslascii2img_cargs,
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
        "fslascii2img": fslascii2img_outputs,
    }.get(t)


class Fslascii2imgOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslascii2img(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Converted NIfTI file from ASCII input"""


def fslascii2img_params(
    infile: InputPathType,
    xsize: int,
    ysize: int,
    zsize: int,
    tsize: int,
    xdim: float,
    ydim: float,
    zdim: float,
    tr: float,
    outfile: str = "output",
) -> Fslascii2imgParameters:
    """
    Build parameters.
    
    Args:
        infile: Input ASCII file.
        xsize: Size in the x dimension (in voxels).
        ysize: Size in the y dimension (in voxels).
        zsize: Size in the z dimension (in voxels).
        tsize: Size in the t dimension (in voxels).
        xdim: Dimension size in the x dimension (in mm).
        ydim: Dimension size in the y dimension (in mm).
        zdim: Dimension size in the z dimension (in mm).
        tr: Repetition time (TR) in seconds.
        outfile: Output NIfTI file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslascii2img",
        "infile": infile,
        "xsize": xsize,
        "ysize": ysize,
        "zsize": zsize,
        "tsize": tsize,
        "xdim": xdim,
        "ydim": ydim,
        "zdim": zdim,
        "tr": tr,
        "outfile": outfile,
    }
    return params


def fslascii2img_cargs(
    params: Fslascii2imgParameters,
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
    cargs.append("fslascii2img")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(str(params.get("xsize")))
    cargs.append(str(params.get("ysize")))
    cargs.append(str(params.get("zsize")))
    cargs.append(str(params.get("tsize")))
    cargs.append(str(params.get("xdim")))
    cargs.append(str(params.get("ydim")))
    cargs.append(str(params.get("zdim")))
    cargs.append(str(params.get("tr")))
    cargs.append(params.get("outfile"))
    return cargs


def fslascii2img_outputs(
    params: Fslascii2imgParameters,
    execution: Execution,
) -> Fslascii2imgOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fslascii2imgOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("outfile")),
    )
    return ret


def fslascii2img_execute(
    params: Fslascii2imgParameters,
    execution: Execution,
) -> Fslascii2imgOutputs:
    """
    Convert data from ASCII format to NIfTI format.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fslascii2imgOutputs`).
    """
    params = execution.params(params)
    cargs = fslascii2img_cargs(params, execution)
    ret = fslascii2img_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslascii2img(
    infile: InputPathType,
    xsize: int,
    ysize: int,
    zsize: int,
    tsize: int,
    xdim: float,
    ydim: float,
    zdim: float,
    tr: float,
    outfile: str = "output",
    runner: Runner | None = None,
) -> Fslascii2imgOutputs:
    """
    Convert data from ASCII format to NIfTI format.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input ASCII file.
        xsize: Size in the x dimension (in voxels).
        ysize: Size in the y dimension (in voxels).
        zsize: Size in the z dimension (in voxels).
        tsize: Size in the t dimension (in voxels).
        xdim: Dimension size in the x dimension (in mm).
        ydim: Dimension size in the y dimension (in mm).
        zdim: Dimension size in the z dimension (in mm).
        tr: Repetition time (TR) in seconds.
        outfile: Output NIfTI file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslascii2imgOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLASCII2IMG_METADATA)
    params = fslascii2img_params(
        infile=infile,
        xsize=xsize,
        ysize=ysize,
        zsize=zsize,
        tsize=tsize,
        xdim=xdim,
        ydim=ydim,
        zdim=zdim,
        tr=tr,
        outfile=outfile,
    )
    return fslascii2img_execute(params, execution)


__all__ = [
    "FSLASCII2IMG_METADATA",
    "Fslascii2imgOutputs",
    "Fslascii2imgParameters",
    "fslascii2img",
    "fslascii2img_params",
]
