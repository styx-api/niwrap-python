# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MAKE_UCHAR_METADATA = Metadata(
    id="125a7b8010e7a6e47c1c93bba9839070d4e12157.boutiques",
    name="mri_make_uchar",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriMakeUcharParameters = typing.TypedDict('MriMakeUcharParameters', {
    "__STYXTYPE__": typing.Literal["mri_make_uchar"],
    "input_volume": InputPathType,
    "talairach_xform": InputPathType,
    "output_volume": str,
    "first_percentile": typing.NotRequired[float | None],
    "wm_percentile": typing.NotRequired[float | None],
    "max_radius": typing.NotRequired[float | None],
    "cumulative_histo": typing.NotRequired[str | None],
    "vradvol": typing.NotRequired[str | None],
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
        "mri_make_uchar": mri_make_uchar_cargs,
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
        "mri_make_uchar": mri_make_uchar_outputs,
    }.get(t)


class MriMakeUcharOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_make_uchar(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume from mri_make_uchar processing"""


def mri_make_uchar_params(
    input_volume: InputPathType,
    talairach_xform: InputPathType,
    output_volume: str,
    first_percentile: float | None = 0.01,
    wm_percentile: float | None = 0.9,
    max_radius: float | None = 50,
    cumulative_histo: str | None = None,
    vradvol: str | None = None,
) -> MriMakeUcharParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume file.
        talairach_xform: Talairach transformation file.
        output_volume: Output volume file.
        first_percentile: First percentile for histogram calculation (default\
            0.01).
        wm_percentile: White matter percentile for histogram calculation\
            (default 0.9).
        max_radius: Maximum radius for voxel consideration (default 50).
        cumulative_histo: Cumulative histogram file.
        vradvol: Volume file where everything outside MAX_R is set to 0.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_make_uchar",
        "input_volume": input_volume,
        "talairach_xform": talairach_xform,
        "output_volume": output_volume,
    }
    if first_percentile is not None:
        params["first_percentile"] = first_percentile
    if wm_percentile is not None:
        params["wm_percentile"] = wm_percentile
    if max_radius is not None:
        params["max_radius"] = max_radius
    if cumulative_histo is not None:
        params["cumulative_histo"] = cumulative_histo
    if vradvol is not None:
        params["vradvol"] = vradvol
    return params


def mri_make_uchar_cargs(
    params: MriMakeUcharParameters,
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
    cargs.append("mri_make_uchar")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("talairach_xform")))
    cargs.append(params.get("output_volume"))
    if params.get("first_percentile") is not None:
        cargs.extend([
            "-f",
            str(params.get("first_percentile"))
        ])
    if params.get("wm_percentile") is not None:
        cargs.extend([
            "-w",
            str(params.get("wm_percentile"))
        ])
    if params.get("max_radius") is not None:
        cargs.extend([
            "-r",
            str(params.get("max_radius"))
        ])
    if params.get("cumulative_histo") is not None:
        cargs.extend([
            "-h",
            params.get("cumulative_histo")
        ])
    if params.get("vradvol") is not None:
        cargs.extend([
            "-v",
            params.get("vradvol")
        ])
    return cargs


def mri_make_uchar_outputs(
    params: MriMakeUcharParameters,
    execution: Execution,
) -> MriMakeUcharOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMakeUcharOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_make_uchar_execute(
    params: MriMakeUcharParameters,
    execution: Execution,
) -> MriMakeUcharOutputs:
    """
    Tool to adjust intensity of brain MRI images using a Talairach transformation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMakeUcharOutputs`).
    """
    params = execution.params(params)
    cargs = mri_make_uchar_cargs(params, execution)
    ret = mri_make_uchar_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_make_uchar(
    input_volume: InputPathType,
    talairach_xform: InputPathType,
    output_volume: str,
    first_percentile: float | None = 0.01,
    wm_percentile: float | None = 0.9,
    max_radius: float | None = 50,
    cumulative_histo: str | None = None,
    vradvol: str | None = None,
    runner: Runner | None = None,
) -> MriMakeUcharOutputs:
    """
    Tool to adjust intensity of brain MRI images using a Talairach transformation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file.
        talairach_xform: Talairach transformation file.
        output_volume: Output volume file.
        first_percentile: First percentile for histogram calculation (default\
            0.01).
        wm_percentile: White matter percentile for histogram calculation\
            (default 0.9).
        max_radius: Maximum radius for voxel consideration (default 50).
        cumulative_histo: Cumulative histogram file.
        vradvol: Volume file where everything outside MAX_R is set to 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMakeUcharOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MAKE_UCHAR_METADATA)
    params = mri_make_uchar_params(
        input_volume=input_volume,
        talairach_xform=talairach_xform,
        output_volume=output_volume,
        first_percentile=first_percentile,
        wm_percentile=wm_percentile,
        max_radius=max_radius,
        cumulative_histo=cumulative_histo,
        vradvol=vradvol,
    )
    return mri_make_uchar_execute(params, execution)


__all__ = [
    "MRI_MAKE_UCHAR_METADATA",
    "MriMakeUcharOutputs",
    "MriMakeUcharParameters",
    "mri_make_uchar",
    "mri_make_uchar_params",
]
