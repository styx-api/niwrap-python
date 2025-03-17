# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RTVIEW_METADATA = Metadata(
    id="d1062fc3fcb7c8d781138ed45f8feb4a04671369.boutiques",
    name="rtview",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


RtviewParameters = typing.TypedDict('RtviewParameters', {
    "__STYX_TYPE__": typing.Literal["rtview"],
    "subject": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[str | None],
    "left_hemi": bool,
    "right_hemi": bool,
    "eccen": bool,
    "polar": bool,
    "real_file": typing.NotRequired[InputPathType | None],
    "imag_file": typing.NotRequired[InputPathType | None],
    "fsig_file": typing.NotRequired[InputPathType | None],
    "reg_file": typing.NotRequired[InputPathType | None],
    "flat_display": bool,
    "patch": typing.NotRequired[str | None],
    "tcl_file": typing.NotRequired[InputPathType | None],
    "no_cleanup": bool,
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
        "rtview": rtview_cargs,
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


class RtviewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rtview(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rtview_params(
    subject: str | None = None,
    hemi: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    eccen: bool = False,
    polar: bool = False,
    real_file: InputPathType | None = None,
    imag_file: InputPathType | None = None,
    fsig_file: InputPathType | None = None,
    reg_file: InputPathType | None = None,
    flat_display: bool = False,
    patch: str | None = None,
    tcl_file: InputPathType | None = None,
    no_cleanup: bool = False,
) -> RtviewParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject to use as display.
        hemi: Hemisphere to display: 'lh' for left hemisphere or 'rh' for right\
            hemisphere.
        left_hemi: Display left hemisphere.
        right_hemi: Display right hemisphere.
        eccen: Display eccentricity data.
        polar: Display polar data.
        real_file: File containing real (cosine) values.
        imag_file: File containing imaginary (sine) values.
        fsig_file: File containing significance values.
        reg_file: Registration file for when real/imag/fsig are volumes.
        flat_display: Display on occip.patch.flat.
        patch: Display on specified patchname.
        tcl_file: Use your own TCL command file.
        no_cleanup: Don't delete temporary directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rtview",
        "left_hemi": left_hemi,
        "right_hemi": right_hemi,
        "eccen": eccen,
        "polar": polar,
        "flat_display": flat_display,
        "no_cleanup": no_cleanup,
    }
    if subject is not None:
        params["subject"] = subject
    if hemi is not None:
        params["hemi"] = hemi
    if real_file is not None:
        params["real_file"] = real_file
    if imag_file is not None:
        params["imag_file"] = imag_file
    if fsig_file is not None:
        params["fsig_file"] = fsig_file
    if reg_file is not None:
        params["reg_file"] = reg_file
    if patch is not None:
        params["patch"] = patch
    if tcl_file is not None:
        params["tcl_file"] = tcl_file
    return params


def rtview_cargs(
    params: RtviewParameters,
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
    cargs.append("rtview")
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            params.get("hemi")
        ])
    if params.get("left_hemi"):
        cargs.append("--lh")
    if params.get("right_hemi"):
        cargs.append("--rh")
    if params.get("eccen"):
        cargs.append("--eccen")
    if params.get("polar"):
        cargs.append("--polar")
    if params.get("real_file") is not None:
        cargs.extend([
            "--real",
            execution.input_file(params.get("real_file"))
        ])
    if params.get("imag_file") is not None:
        cargs.extend([
            "--imag",
            execution.input_file(params.get("imag_file"))
        ])
    if params.get("fsig_file") is not None:
        cargs.extend([
            "--fsig",
            execution.input_file(params.get("fsig_file"))
        ])
    if params.get("reg_file") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("reg_file"))
        ])
    if params.get("flat_display"):
        cargs.append("--flat")
    if params.get("patch") is not None:
        cargs.extend([
            "--patch",
            params.get("patch")
        ])
    if params.get("tcl_file") is not None:
        cargs.extend([
            "--tcl",
            execution.input_file(params.get("tcl_file"))
        ])
    if params.get("no_cleanup"):
        cargs.append("--no-cleanup")
    return cargs


def rtview_outputs(
    params: RtviewParameters,
    execution: Execution,
) -> RtviewOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RtviewOutputs(
        root=execution.output_file("."),
    )
    return ret


def rtview_execute(
    params: RtviewParameters,
    execution: Execution,
) -> RtviewOutputs:
    """
    View FSFAST version 5 retinotopy data using the color wheel. This is a front-end
    for tksurfer, setting up the environment for using the color wheel.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RtviewOutputs`).
    """
    params = execution.params(params)
    cargs = rtview_cargs(params, execution)
    ret = rtview_outputs(params, execution)
    execution.run(cargs)
    return ret


def rtview(
    subject: str | None = None,
    hemi: str | None = None,
    left_hemi: bool = False,
    right_hemi: bool = False,
    eccen: bool = False,
    polar: bool = False,
    real_file: InputPathType | None = None,
    imag_file: InputPathType | None = None,
    fsig_file: InputPathType | None = None,
    reg_file: InputPathType | None = None,
    flat_display: bool = False,
    patch: str | None = None,
    tcl_file: InputPathType | None = None,
    no_cleanup: bool = False,
    runner: Runner | None = None,
) -> RtviewOutputs:
    """
    View FSFAST version 5 retinotopy data using the color wheel. This is a front-end
    for tksurfer, setting up the environment for using the color wheel.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to use as display.
        hemi: Hemisphere to display: 'lh' for left hemisphere or 'rh' for right\
            hemisphere.
        left_hemi: Display left hemisphere.
        right_hemi: Display right hemisphere.
        eccen: Display eccentricity data.
        polar: Display polar data.
        real_file: File containing real (cosine) values.
        imag_file: File containing imaginary (sine) values.
        fsig_file: File containing significance values.
        reg_file: Registration file for when real/imag/fsig are volumes.
        flat_display: Display on occip.patch.flat.
        patch: Display on specified patchname.
        tcl_file: Use your own TCL command file.
        no_cleanup: Don't delete temporary directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RtviewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RTVIEW_METADATA)
    params = rtview_params(
        subject=subject,
        hemi=hemi,
        left_hemi=left_hemi,
        right_hemi=right_hemi,
        eccen=eccen,
        polar=polar,
        real_file=real_file,
        imag_file=imag_file,
        fsig_file=fsig_file,
        reg_file=reg_file,
        flat_display=flat_display,
        patch=patch,
        tcl_file=tcl_file,
        no_cleanup=no_cleanup,
    )
    return rtview_execute(params, execution)


__all__ = [
    "RTVIEW_METADATA",
    "RtviewOutputs",
    "RtviewParameters",
    "rtview",
    "rtview_params",
]
