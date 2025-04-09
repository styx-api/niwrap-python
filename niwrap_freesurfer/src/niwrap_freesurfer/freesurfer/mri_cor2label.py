# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COR2LABEL_METADATA = Metadata(
    id="1d2d54df5aac2096dd47a33b09dc9c5904fb89f4.boutiques",
    name="mri_cor2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCor2labelParameters = typing.TypedDict('MriCor2labelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_cor2label"],
    "input_file": InputPathType,
    "label_id": float,
    "label_file": str,
    "threshold": typing.NotRequired[float | None],
    "volume_file": typing.NotRequired[str | None],
    "surface_overlay": typing.NotRequired[list[str] | None],
    "surface_path": typing.NotRequired[str | None],
    "optimize": typing.NotRequired[list[str] | None],
    "remove_holes_islands": bool,
    "dilate": typing.NotRequired[float | None],
    "erode": typing.NotRequired[float | None],
    "help": bool,
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
        "mri_cor2label": mri_cor2label_cargs,
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
        "mri_cor2label": mri_cor2label_outputs,
    }.get(t)


class MriCor2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cor2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Generated label file."""
    output_volume_file: OutputPathType | None
    """Written volume label if specified."""


def mri_cor2label_params(
    input_file: InputPathType,
    label_id: float,
    label_file: str,
    threshold: float | None = None,
    volume_file: str | None = None,
    surface_overlay: list[str] | None = None,
    surface_path: str | None = None,
    optimize: list[str] | None = None,
    remove_holes_islands: bool = False,
    dilate: float | None = None,
    erode: float | None = None,
    help_: bool = False,
) -> MriCor2labelParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input volume or surface overlay file.
        label_id: Value to match in the input data.
        label_file: Name of the output label file.
        threshold: Threshold the input to make label, e.g., input values must\
            be greater than the threshold.
        volume_file: Write the label volume to a file.
        surface_overlay: Interpret input as a surface overlay, specifying\
            subject, hemisphere, and surface.
        surface_path: Specify surface path rather than subject/hemisphere.
        optimize: Treat input as a probability map and optimize thresholding.
        remove_holes_islands: Remove holes in label and islands (only valid\
            with --surf).
        dilate: Dilate label with specified number of dilations (only valid\
            with --surf).
        erode: Erode label with specified number of erosions (only valid with\
            --surf).
        help_: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cor2label",
        "input_file": input_file,
        "label_id": label_id,
        "label_file": label_file,
        "remove_holes_islands": remove_holes_islands,
        "help": help_,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if volume_file is not None:
        params["volume_file"] = volume_file
    if surface_overlay is not None:
        params["surface_overlay"] = surface_overlay
    if surface_path is not None:
        params["surface_path"] = surface_path
    if optimize is not None:
        params["optimize"] = optimize
    if dilate is not None:
        params["dilate"] = dilate
    if erode is not None:
        params["erode"] = erode
    return params


def mri_cor2label_cargs(
    params: MriCor2labelParameters,
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
    cargs.append("mri_cor2label")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-id",
        str(params.get("label_id"))
    ])
    cargs.extend([
        "-l",
        params.get("label_file")
    ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("threshold"))
        ])
    if params.get("volume_file") is not None:
        cargs.extend([
            "--v",
            params.get("volume_file")
        ])
    if params.get("surface_overlay") is not None:
        cargs.extend([
            "--surf",
            *params.get("surface_overlay")
        ])
    if params.get("surface_path") is not None:
        cargs.extend([
            "--surf-path",
            params.get("surface_path")
        ])
    if params.get("optimize") is not None:
        cargs.extend([
            "--opt",
            *params.get("optimize")
        ])
    if params.get("remove_holes_islands"):
        cargs.append("--remove-holes-islands")
    if params.get("dilate") is not None:
        cargs.extend([
            "--dilate",
            str(params.get("dilate"))
        ])
    if params.get("erode") is not None:
        cargs.extend([
            "--erode",
            str(params.get("erode"))
        ])
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_cor2label_outputs(
    params: MriCor2labelParameters,
    execution: Execution,
) -> MriCor2labelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCor2labelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(params.get("label_file")),
        output_volume_file=execution.output_file(params.get("volume_file")) if (params.get("volume_file") is not None) else None,
    )
    return ret


def mri_cor2label_execute(
    params: MriCor2labelParameters,
    execution: Execution,
) -> MriCor2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label. Designed to convert
    parcellation volumes stored in mri format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCor2labelOutputs`).
    """
    params = execution.params(params)
    cargs = mri_cor2label_cargs(params, execution)
    ret = mri_cor2label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cor2label(
    input_file: InputPathType,
    label_id: float,
    label_file: str,
    threshold: float | None = None,
    volume_file: str | None = None,
    surface_overlay: list[str] | None = None,
    surface_path: str | None = None,
    optimize: list[str] | None = None,
    remove_holes_islands: bool = False,
    dilate: float | None = None,
    erode: float | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriCor2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label. Designed to convert
    parcellation volumes stored in mri format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume or surface overlay file.
        label_id: Value to match in the input data.
        label_file: Name of the output label file.
        threshold: Threshold the input to make label, e.g., input values must\
            be greater than the threshold.
        volume_file: Write the label volume to a file.
        surface_overlay: Interpret input as a surface overlay, specifying\
            subject, hemisphere, and surface.
        surface_path: Specify surface path rather than subject/hemisphere.
        optimize: Treat input as a probability map and optimize thresholding.
        remove_holes_islands: Remove holes in label and islands (only valid\
            with --surf).
        dilate: Dilate label with specified number of dilations (only valid\
            with --surf).
        erode: Erode label with specified number of erosions (only valid with\
            --surf).
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCor2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COR2LABEL_METADATA)
    params = mri_cor2label_params(
        input_file=input_file,
        label_id=label_id,
        label_file=label_file,
        threshold=threshold,
        volume_file=volume_file,
        surface_overlay=surface_overlay,
        surface_path=surface_path,
        optimize=optimize,
        remove_holes_islands=remove_holes_islands,
        dilate=dilate,
        erode=erode,
        help_=help_,
    )
    return mri_cor2label_execute(params, execution)


__all__ = [
    "MRI_COR2LABEL_METADATA",
    "MriCor2labelOutputs",
    "MriCor2labelParameters",
    "mri_cor2label",
    "mri_cor2label_params",
]
