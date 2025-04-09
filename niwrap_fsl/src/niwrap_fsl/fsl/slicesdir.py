# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICESDIR_METADATA = Metadata(
    id="0faf1984ca6378da79aa324f8001c8b0a0e662ba.boutiques",
    name="slicesdir",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SlicesdirParameters = typing.TypedDict('SlicesdirParameters', {
    "__STYX_TYPE__": typing.Literal["slicesdir"],
    "flag_filelist": bool,
    "outline_image": typing.NotRequired[InputPathType | None],
    "edge_threshold": typing.NotRequired[float | None],
    "slice_option": bool,
    "filelist": list[str],
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
        "slicesdir": slicesdir_cargs,
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


class SlicesdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicesdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slicesdir_params(
    filelist: list[str],
    flag_filelist: bool = False,
    outline_image: InputPathType | None = None,
    edge_threshold: float | None = None,
    slice_option: bool = False,
) -> SlicesdirParameters:
    """
    Build parameters.
    
    Args:
        filelist: List of image files to process.
        flag_filelist: Filelist contains pairs of images (underlying and\
            red-outline images).
        outline_image: Use the specified image as the red-outline image on top\
            of all images in the file list.
        edge_threshold: Use specified threshold for edges. If >0, use this\
            proportion of max-min; if <0, use the absolute value.
        slice_option: Output every second axial slice instead of 9 ortho slices.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slicesdir",
        "flag_filelist": flag_filelist,
        "slice_option": slice_option,
        "filelist": filelist,
    }
    if outline_image is not None:
        params["outline_image"] = outline_image
    if edge_threshold is not None:
        params["edge_threshold"] = edge_threshold
    return params


def slicesdir_cargs(
    params: SlicesdirParameters,
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
    cargs.append("slicesdir")
    if params.get("flag_filelist"):
        cargs.append("-o")
    if params.get("outline_image") is not None:
        cargs.extend([
            "-p",
            execution.input_file(params.get("outline_image"))
        ])
    if params.get("edge_threshold") is not None:
        cargs.extend([
            "-e",
            str(params.get("edge_threshold"))
        ])
    if params.get("slice_option"):
        cargs.append("-S")
    cargs.extend(params.get("filelist"))
    return cargs


def slicesdir_outputs(
    params: SlicesdirParameters,
    execution: Execution,
) -> SlicesdirOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicesdirOutputs(
        root=execution.output_file("."),
    )
    return ret


def slicesdir_execute(
    params: SlicesdirParameters,
    execution: Execution,
) -> SlicesdirOutputs:
    """
    slicesdir generates a directory containing orthogonal slices through a set of
    images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicesdirOutputs`).
    """
    params = execution.params(params)
    cargs = slicesdir_cargs(params, execution)
    ret = slicesdir_outputs(params, execution)
    execution.run(cargs)
    return ret


def slicesdir(
    filelist: list[str],
    flag_filelist: bool = False,
    outline_image: InputPathType | None = None,
    edge_threshold: float | None = None,
    slice_option: bool = False,
    runner: Runner | None = None,
) -> SlicesdirOutputs:
    """
    slicesdir generates a directory containing orthogonal slices through a set of
    images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filelist: List of image files to process.
        flag_filelist: Filelist contains pairs of images (underlying and\
            red-outline images).
        outline_image: Use the specified image as the red-outline image on top\
            of all images in the file list.
        edge_threshold: Use specified threshold for edges. If >0, use this\
            proportion of max-min; if <0, use the absolute value.
        slice_option: Output every second axial slice instead of 9 ortho slices.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICESDIR_METADATA)
    params = slicesdir_params(
        flag_filelist=flag_filelist,
        outline_image=outline_image,
        edge_threshold=edge_threshold,
        slice_option=slice_option,
        filelist=filelist,
    )
    return slicesdir_execute(params, execution)


__all__ = [
    "SLICESDIR_METADATA",
    "SlicesdirOutputs",
    "SlicesdirParameters",
    "slicesdir",
    "slicesdir_params",
]
